from django.urls import path, include
from rest_framework import routers
from .views import ListingViewSet, BookingViewSet

# DRF Router automatically generates RESTful URLs
router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoints under /api/
]
