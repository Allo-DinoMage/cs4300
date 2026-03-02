from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime


class MovieModelTest(TestCase):
    """
    Unit tests for the Movie model, including edge cases.
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
        Test string representation of Movie is not empty.
        """
        self.assertIsNotNone(self.movie.title)

    def test_movie_zero_duration(self):
        """
        Edge case: Test movie with zero duration.
        """
        movie = Movie.objects.create(
            title="Zero Duration Movie",
            description="No duration.",
            release_date=datetime.date(2025, 1, 1),
            duration=0
        )
        self.assertEqual(movie.duration, 0)

    def test_movie_very_long_title(self):
        """
        Edge case: Test movie with maximum length title.
        """
        long_title = "A" * 200
        movie = Movie.objects.create(
            title=long_title,
            description="Long title movie.",
            release_date=datetime.date(2025, 1, 1),
            duration=90
        )
        self.assertEqual(len(movie.title), 200)

    def test_movie_future_release_date(self):
        """
        Edge case: Test movie with a far future release date.
        """
        movie = Movie.objects.create(
            title="Future Movie",
            description="Not out yet.",
            release_date=datetime.date(2099, 12, 31),
            duration=100
        )
        self.assertEqual(movie.release_date, datetime.date(2099, 12, 31))

    def test_movie_empty_description(self):
        """
        Edge case: Test movie with empty description.
        """
        movie = Movie.objects.create(
            title="No Description Movie",
            description="",
            release_date=datetime.date(2025, 1, 1),
            duration=100
        )
        self.assertEqual(movie.description, "")


class SeatModelTest(TestCase):
    """
    Unit tests for the Seat model, including edge cases.
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
        Test that seat booking status can be updated to booked.
        """
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)

    def test_seat_double_booking(self):
        """
        Edge case: Test that a seat can be marked booked twice without error.
        """
        self.seat.is_booked = True
        self.seat.save()
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)

    def test_seat_unbook(self):
        """
        Edge case: Test that a booked seat can be unbooked.
        """
        self.seat.is_booked = True
        self.seat.save()
        self.seat.is_booked = False
        self.seat.save()
        self.assertFalse(self.seat.is_booked)

    def test_seat_number_max_length(self):
        """
        Edge case: Test seat with maximum length seat number.
        """
        seat = Seat.objects.create(
            seat_number="A" * 10,
            is_booked=False
        )
        self.assertEqual(len(seat.seat_number), 10)


class BookingModelTest(TestCase):
    """
    Unit tests for the Booking model, including edge cases.
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

    def test_booking_date_auto_set(self):
        """
        Test that booking date is automatically set on creation.
        """
        self.assertIsNotNone(self.booking.booking_date)

    def test_multiple_bookings_same_user(self):
        """
        Edge case: Test that a user can have multiple bookings.
        """
        seat2 = Seat.objects.create(seat_number="C3", is_booked=False)
        booking2 = Booking.objects.create(
            movie=self.movie,
            seat=seat2,
            user=self.user
        )
        self.assertEqual(Booking.objects.filter(user=self.user).count(), 2)

    def test_booking_different_users_same_seat(self):
        """
        Edge case: Test that two different users can book the same seat
        (model level - no constraint prevents this).
        """
        user2 = User.objects.create_user(username="testuser2", password="testpass2")
        booking2 = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=user2
        )
        self.assertEqual(Booking.objects.filter(seat=self.seat).count(), 2)


class MovieAPITest(APITestCase):
    """
    Integration tests for the Movie API endpoints.
    """

    def setUp(self):
        """
        Set up test data for Movie API tests.
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

    def test_create_movie_missing_title(self):
        """
        Edge case: Test that creating a movie without a title fails.
        """
        data = {
            'description': 'No title movie',
            'release_date': '2025-08-01',
            'duration': 110
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_movie_invalid_date(self):
        """
        Edge case: Test that creating a movie with an invalid date fails.
        """
        data = {
            'title': 'Bad Date Movie',
            'description': 'Invalid date',
            'release_date': 'not-a-date',
            'duration': 100
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_nonexistent_movie(self):
        """
        Edge case: Test that requesting a nonexistent movie returns 404.
        """
        response = self.client.get('/api/movies/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_movie(self):
        """
        Test that a movie can be deleted via the API.
        """
        response = self.client.delete(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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

    def test_get_nonexistent_seat(self):
        """
        Edge case: Test that requesting a nonexistent seat returns 404.
        """
        response = self.client.get('/api/seats/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_seat(self):
        """
        Test that a seat can be created via the API.
        """
        data = {'seat_number': 'E5', 'is_booked': False}
        response = self.client.post('/api/seats/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_seat_missing_seat_number(self):
        """
        Edge case: Test that creating a seat without a seat number fails.
        """
        data = {'is_booked': False}
        response = self.client.post('/api/seats/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


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
        Edge case: Test that unauthenticated users cannot access bookings.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_only_sees_own_bookings(self):
        """
        Edge case: Test that users can only see their own bookings.
        """
        other_user = User.objects.create_user(username="otheruser", password="testpass")
        other_seat = Seat.objects.create(seat_number="F6", is_booked=False)
        Booking.objects.create(movie=self.movie, seat=other_seat, user=other_user)

        response = self.client.get('/api/bookings/')
        self.assertEqual(len(response.data), 0)

    def test_create_booking(self):
        """
        Test that an authenticated user can create a booking.
        """
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_unauthenticated(self):
        """
        Edge case: Test that unauthenticated users cannot create bookings.
        """
        self.client.force_authenticate(user=None)
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
