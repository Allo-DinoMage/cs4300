import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')
django.setup()

from bookings.models import Seat

for i in range(1, 6):
    for letter in ['A', 'B', 'C', 'D']:
        Seat.objects.get_or_create(seat_number=f'{letter}{i}', defaults={'is_booked': False})

print("Done! Seats created.")
