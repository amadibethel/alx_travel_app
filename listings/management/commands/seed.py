#!/usr/bin/env python3

from django.core.management.base import BaseCommand
from listings.models import Listing, Booking
from faker import Faker
import random
from datetime import timedelta, date


class Command(BaseCommand):
    help = "Seed the database with sample listings and bookings"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(50.0, 500.0), 2)
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

            # Create sample bookings for each listing
            for _ in range(random.randint(1, 5)):
                booking_date = fake.date_between(start_date='-30d', end_date='today')
                Booking.objects.create(
                    listing=listing,
                    user_name=fake.name(),
                    user_email=fake.email(),
                    booking_date=booking_date
                )
                self.stdout.write(self.style.SUCCESS(f'  Created booking for {listing.title} on {booking_date}'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed.'))