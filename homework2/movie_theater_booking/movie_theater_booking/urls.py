from bookings.views import signup
from django.contrib import admin
from django.urls import path, include

"""
Main URL configuration for the movie_theater_booking project.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('bookings.urls')),
]
