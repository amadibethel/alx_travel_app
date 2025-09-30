# ALX Travel App 0x00

This project is a duplicated version of **alx_travel_app**, enhanced with models, serializers, and database seeding.  
It demonstrates how to structure relational data in Django, expose it through Django REST Framework (DRF), and populate the database with sample data for development and testing.

---

## Features
- **Listings**: Properties that can be booked.
- **Bookings**: Records of user reservations for listings.
- **Reviews**: User reviews with ratings for listings.
- **Serializers**: DRF serializers to convert Django models into JSON responses.
- **Database Seeding**: A custom management command to populate the database with sample listings and bookings.

---

## Tech Stack
- **Python 3.x**
- **Django 5.x**
- **Django REST Framework**
- **SQLite/PostgreSQL**

---

## Project Structure

alx_travel_app_0x00/
│── alx_travel_app/
│ ├── listings/
│ │ ├── models.py # Listing, Booking, Review models
│ │ ├── serializers.py # DRF serializers for models
│ │ ├── management/
│ │ │ └── commands/
│ │ │ └── seed.py # Seeder to populate database with sample data
│ └── ...
│── README.md


---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd alx_travel_app_0x00

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

## Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

## Install Dependencies

pip install -r requirements.txt

## Run Migrations

python manage.py migrate

