from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime


class MovieModelTest(TestCase):
    """
    Unit tests for the Movie model.
    """

    def setUp(self):
        """
        Set up test data for Movie model tests.
        """
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description.",
            release_date=datetime.date(2025, 1, 1),
            duration=120
        )

    def test_movie_creation(self):
        """
        Test that a movie is created correctly.
        """
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)

    def test_movie_str(self):
        """
        Test string representation of Movie.
        """
        self.assertIsNotNone(self.movie.title)


class SeatModelTest(TestCase):
    """
    Unit tests for the Seat model.
    """

    def setUp(self):
        """
        Set up test data for Seat model tests.
        """
        self.seat = Seat.objects.create(
            seat_number="A1",
            is_booked=False
        )

    def test_seat_creation(self):
        """
        Test that a seat is created correctly.
        """
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)

    def test_seat_booking_status(self):
        """
        Test that seat booking status can be updated.
        """
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)


class BookingModelTest(TestCase):
    """
    Unit tests for the Booking model.
    """

    def setUp(self):
        """
        Set up test data for Booking model tests.
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Description",
            release_date=datetime.date(2025, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="B2", is_booked=False)
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_booking_creation(self):
        """
        Test that a booking is created correctly.
        """
        self.assertEqual(self.booking.movie.title, "Test Movie")
        self.assertEqual(self.booking.seat.seat_number, "B2")
        self.assertEqual(self.booking.user.username, "testuser")


class MovieAPITest(APITestCase):
    """
    Integration tests for the Movie API endpoints.
    """

    def setUp(self):
        """
        Set up test data for API tests.
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="API test description.",
            release_date=datetime.date(2025, 6, 1),
            duration=90
        )

    def test_get_movies(self):
        """
        Test that the movies API returns a 200 status code.
        """
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        """
        Test that a movie can be created via the API.
        """
        data = {
            'title': 'New Movie',
            'description': 'New description',
            'release_date': '2025-08-01',
            'duration': 110
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SeatAPITest(APITestCase):
    """
    Integration tests for the Seat API endpoints.
    """

    def setUp(self):
        """
        Set up test data for Seat API tests.
        """
        self.seat = Seat.objects.create(seat_number="C3", is_booked=False)

    def test_get_seats(self):
        """
        Test that the seats API returns a 200 status code.
        """
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingAPITest(APITestCase):
    """
    Integration tests for the Booking API endpoints.
    """

    def setUp(self):
        """
        Set up test data for Booking API tests.
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(
            title="Booking Test Movie",
            description="Description",
            release_date=datetime.date(2025, 1, 1),
            duration=100
        )
        self.seat = Seat.objects.create(seat_number="D4", is_booked=False)

    def test_get_bookings(self):
        """
        Test that authenticated users can view their bookings.
        """
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_bookings(self):
        """
        Test that unauthenticated users cannot access bookings.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
