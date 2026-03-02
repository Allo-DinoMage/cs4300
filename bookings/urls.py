from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

"""
URL configuration for the bookings app.
Includes both API endpoints and template-based views.
"""

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', views.seat_booking, name='book_seat'),
    path('movies/<int:movie_id>/seats/<int:seat_id>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('bookings/', views.booking_history, name='booking_history'),
]
