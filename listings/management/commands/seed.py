#!/usr/bin/env python3
from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Ocean View", "description": "Beautiful beach house", "location": "Mombasa", "price_per_night": 100.00},
            {"title": "City Apartment", "description": "In the heart of Nairobi", "location": "Nairobi", "price_per_night": 75.50},
            {"title": "Mountain Cabin", "description": "Quiet and peaceful", "location": "Mt. Kenya", "price_per_night": 85.00},
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
