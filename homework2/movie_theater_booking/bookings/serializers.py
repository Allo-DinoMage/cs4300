from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for the Movie model.
    Converts Movie objects to and from JSON format for the API.
    """
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'duration']

class SeatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Seat model.
    Converts Seat objects to and from JSON format for the API.
    """
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Converts Booking objects to and from JSON format for the API.
    User field is set to read-only as it is assigned automatically.
    """
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'booking_date']
        read_only_fields = ['user', 'booking_date']
