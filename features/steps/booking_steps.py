from behave import given, when, then
from django.test import Client
from bookings.models import Movie, Seat, Booking
from django.contrib.auth.models import User
import datetime


@given('the database has movies')
def step_database_has_movies(context):
    """
    Create a test movie in the database.
    """
    context.movie = Movie.objects.create(
        title="Behave Test Movie",
        description="A movie for BDD testing.",
        release_date=datetime.date(2025, 1, 1),
        duration=120
    )


@given('the database has seats')
def step_database_has_seats(context):
    """
    Create a test seat in the database.
    """
    context.seat = Seat.objects.create(
        seat_number="A1",
        is_booked=False
    )


@given('I am a logged in user')
def step_logged_in_user(context):
    """
    Create and log in a test user.
    """
    context.user = User.objects.create_user(
        username="behaveuser",
        password="testpass"
    )
    context.client = Client()
    context.client.login(username="behaveuser", password="testpass")


@when('I visit the movies page')
def step_visit_movies_page(context):
    """
    Send a GET request to the movies page.
    """
    context.client = Client()
    context.response = context.client.get('/movies/')


@when('I visit the seat booking page for a movie')
def step_visit_seat_booking_page(context):
    """
    Send a GET request to the seat booking page.
    """
    context.client = Client()
    context.response = context.client.get(f'/movies/{context.movie.id}/seats/')


@when('I visit the booking history page')
def step_visit_booking_history(context):
    """
    Send a GET request to the booking history page.
    """
    context.response = context.client.get('/bookings/')


@when('I request the movies API')
def step_request_movies_api(context):
    """
    Send a GET request to the movies API endpoint.
    """
    context.client = Client()
    context.response = context.client.get('/api/movies/')


@when('I request the seats API')
def step_request_seats_api(context):
    """
    Send a GET request to the seats API endpoint.
    """
    context.client = Client()
    context.response = context.client.get('/api/seats/')


@when('I request the bookings API without authentication')
def step_request_bookings_api_unauthenticated(context):
    """
    Send a GET request to the bookings API without authentication.
    """
    context.client = Client()
    context.response = context.client.get('/api/bookings/')


@then('I should see a list of movies')
def step_see_list_of_movies(context):
    """
    Verify the movies page loads successfully.
    """
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"


@then('I should see available seats')
def step_see_available_seats(context):
    """
    Verify the seat booking page loads successfully.
    """
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"


@then('I should see an empty booking history')
def step_see_empty_booking_history(context):
    """
    Verify the booking history page loads successfully.
    """
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"


@then('the response status should be 200')
def step_response_status_200(context):
    """
    Verify the API response status is 200.
    """
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"


@then('the response status should be 403')
def step_response_status_403(context):
    """
    Verify the API response status is 403 for unauthenticated requests.
    """
    assert context.response.status_code == 403, \
        f"Expected 403 but got {context.response.status_code}"
