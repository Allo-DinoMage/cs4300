# Movie Theater Booking Application
A RESTful Movie Theater Booking Application built with Python and Django.
This application allows users to view movie listings, book seats, and check
their booking history via both a REST API and a Bootstrap user interface.

## AI Usage Disclosure
This project was built with assistance from Claude (Anthropic) via claude.ai.
Claude was used to help generate boilerplate code, debug errors, write tests,
and provide guidance on Django conventions. All code was reviewed and understood
by the author before submission.

## Project Structure
```
movie_theater_booking/
├── bookings/
│   ├── models.py        # Movie, Seat, Booking models
│   ├── views.py         # API ViewSets and template views
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URL routing
│   ├── tests.py         # Unit and integration tests
│   └── templates/       # Bootstrap HTML templates
├── features/            # BDD tests with Behave
├── movie_theater_booking/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Setup Instructions

### Requirements
- Python 3.x
- Docker (for DevEdu environment)

### Installation
1. Clone the repository:
   git clone git@github.com:Allo-DinoMage/cs4300.git
   cd cs4300/homework2/movie_theater_booking

2. Create and activate virtual environment:
   python3 -m venv myenv --system-site-packages
   source myenv/bin/activate

3. Install dependencies:
   pip install django djangorestframework behave

4. Run migrations:
   python manage.py migrate

5. Start the server:
   python manage.py runserver 0.0.0.0:3000

6. Visit the app at http://localhost:3000/movies/

## API Endpoints

### Movies
- `GET  /api/movies/`           — List all movies
- `POST /api/movies/`           — Create a movie
- `GET  /api/movies/<id>/`      — Retrieve a movie
- `DELETE /api/movies/<id>/`    — Delete a movie

### Seats
- `GET  /api/seats/`            — List all seats
- `POST /api/seats/`            — Create a seat
- `GET  /api/seats/<id>/`       — Retrieve a seat

### Bookings (Authentication Required)
- `GET  /api/bookings/`         — List your bookings
- `POST /api/bookings/`         — Create a booking
- `DELETE /api/bookings/<id>/`  — Cancel a booking

### Authentication
- `POST /accounts/signup/`      — Register a new user
- `POST /api/register/`         — Register a new user (alternate endpoint)
- `POST /accounts/login/`       — Log in
- `POST /accounts/logout/`      — Log out

### Example: Creating a Booking
```
POST /api/bookings/
{
  "movie": 1,
  "seat": 3
}
```
Requires authentication. Returns 400 if seat is already booked or user has already booked that seat for that movie.

## Template Pages
- `/movies/`                    — Browse available movies
- `/movies/<id>/seats/`         — Book a seat for a movie
- `/bookings/`                  — View and cancel booking history
- `/accounts/signup/`           — Register a new account
- `/accounts/login/`            — Log in

## Running Tests

### Unit and Integration Tests
   python manage.py test

### BDD Tests
   behave

## Deployment
This application is deployed on Render.
Live URL: https://cs4300-pfwr.onrender.com

Auto-deploys from the `main` branch on GitHub. On each deploy, Render runs
`build.sh` which installs dependencies, collects static files, and runs migrations.
