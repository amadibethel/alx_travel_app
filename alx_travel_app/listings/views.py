from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage Listings.
    Supports CRUD operations: list, retrieve, create, update, delete.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage Bookings.
    Supports CRUD operations: list, retrieve, create, update, delete.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
