from django.contrib import admin
from django.urls import path, include

"""
Main URL configuration for the movie_theater_booking project.
Routes requests to the admin panel, the bookings API, and template views.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
]
