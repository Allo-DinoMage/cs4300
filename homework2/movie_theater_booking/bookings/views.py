from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Movie model.
    Handles list, create, retrieve, update, and delete operations on movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Seat model.
    Handles seat availability and booking status operations.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Booking model.
    Allows authenticated users to book seats and view their booking history.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns only the bookings belonging to the currently logged-in user.
        """
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assigns the logged-in user when a new booking is created.
        """
        serializer.save(user=self.request.user)


def movie_list(request):
    """
    Template view that displays all available movies.
    """
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    """
    Template view that displays available seats for a specific movie,
    organized into rows by the first letter of the seat number.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')
    
    # Organize seats into rows by letter
    rows = {}
    for seat in seats:
        row_letter = seat.seat_number[0]
        if row_letter not in rows:
            rows[row_letter] = []
        rows[row_letter].append(seat)
    
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'rows': rows
    })

@login_required
def booking_history(request):
    """
    Template view that displays the logged-in user's booking history.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

@login_required
def confirm_booking(request, movie_id, seat_id):
    """
    Handles booking confirmation and marks the seat as booked.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    if not seat.is_booked:
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        seat.is_booked = True
        seat.save()
    return render(request, 'bookings/booking_history.html', {
        'bookings': Booking.objects.filter(user=request.user)
    })
def signup(request):
    """
    Allows a new user to create an account.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
