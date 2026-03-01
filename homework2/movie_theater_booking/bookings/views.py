from rest_framework import viewsets, permissions
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