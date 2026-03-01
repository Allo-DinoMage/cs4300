from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """
    Model representing a movie in the theater.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    """
    Model representing a seat in the theater.
    """
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    """
    Model representing a booking made by a user.
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
