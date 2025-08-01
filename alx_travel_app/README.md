# alx_travel_app

This is a Django backend application for a travel booking platform.

## Features

- **Listings**: Travel destinations or accommodation listings.
- **Bookings**: Users can book available listings.
- **Reviews**: Users can leave reviews on their bookings.

## Models

- **Listing**: Title, description, price, availability.
- **Booking**: Linked to a Listing, includes dates and number of guests.
- **Review**: Linked to a Booking, includes rating and comment.

## Serializers

- ListingSerializer
- BookingSerializer

## Seeder

Run the following command to seed the database with test data:

```bash
python manage.py seed
