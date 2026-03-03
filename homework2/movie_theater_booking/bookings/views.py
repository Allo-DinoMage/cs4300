from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        seat_id = request.data.get('seat')
        movie_id = request.data.get('movie')

        try:
            seat = Seat.objects.get(id=seat_id)
        except Seat.DoesNotExist:
            return Response({'error': 'Seat not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Keep this for the test that sets is_booked=True directly
        if seat.is_booked:
            return Response({'error': 'Seat is already booked'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if this seat is already booked for this specific movie
        if Booking.objects.filter(seat=seat, movie_id=movie_id).exists():
            return Response({'error': 'Seat is already booked for this movie'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if this user already booked this seat for this movie
        if Booking.objects.filter(seat=seat, user=request.user, movie_id=movie_id).exists():
            return Response({'error': 'You already booked this seat'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.seat.is_booked = False
        booking.seat.save()
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()

        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        if len(username) > 150:
            return Response({'error': 'Username too long'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)


# Keep the original template-based signup for the HTML form
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')
    
    # Get seat IDs already booked for THIS movie
    booked_seat_ids = Booking.objects.filter(movie_id=movie_id).values_list('seat_id', flat=True)

    rows = {}
    for seat in seats:
        seat.is_booked = seat.id in booked_seat_ids  # override per-movie
        row_letter = seat.seat_number[0]
        if row_letter not in rows:
            rows[row_letter] = []
        rows[row_letter].append(seat)

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'rows': rows})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})


@login_required
def confirm_booking(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    if not seat.is_booked:
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        seat.is_booked = True
        seat.save()
    return render(request, 'bookings/booking_history.html', {
        'bookings': Booking.objects.filter(user=request.user)
    })