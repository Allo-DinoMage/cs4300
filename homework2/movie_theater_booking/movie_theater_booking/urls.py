from django.contrib import admin
from django.urls import path, include

"""
Main URL configuration for the movie_theater_booking project.
Routes requests to the admin panel and the bookings API.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),
]
