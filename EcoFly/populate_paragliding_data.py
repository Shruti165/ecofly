import os

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EcoFly.settings")

# Import and setup Django after setting DJANGO_SETTINGS_MODULE
import django
django.setup()

from datetime import date, time
from django.contrib.auth.models import User
from paragliding.models import Ride, SiteInfo

# Create a user to link rides if necessary (if you want to assign a user as a seller)
if not User.objects.filter(username="pilot_user").exists():
    user = User.objects.create_user(username="pilot_user", password="password123")
else:
    user = User.objects.get(username="pilot_user")

# Populate Ride data
def populate_ride_data():
    rides = [
        {"origin": "Mumbai", "destination": "Panchgani", "date": date(2024, 11, 5), "time": time(8, 30), "capacity": 3, "preferences": "Eco-friendly"},
        {"origin": "Delhi", "destination": "Bir", "date": date(2024, 12, 1), "time": time(10, 0), "capacity": 4, "preferences": "Shared ride"},
        {"origin": "Bangalore", "destination": "Goa", "date": date(2024, 11, 20), "time": time(7, 15), "capacity": 2, "preferences": "Pet-friendly"},
    ]
    for ride_data in rides:
        Ride.objects.get_or_create(**ride_data)

# Populate SiteInfo data
def populate_site_info_data():
    sites = [
        {
            "name": "Bir",
            "best_time": "October to December, March to May",
            "local_regulations": "Respect local customs, avoid littering",
            "weather_conditions": "Clear skies, moderate winds, cool temperature",
        },
        {
            "name": "Panchgani",
            "best_time": "September to February",
            "local_regulations": "Use official launch sites only",
            "weather_conditions": "Mild winds, slightly warmer temperatures",
        },
        {
            "name": "Goa",
            "best_time": "October to March",
            "local_regulations": "Stay clear of tourist areas for safety",
            "weather_conditions": "Warm, sunny, moderate coastal winds",
        },
    ]
    for site_data in sites:
        SiteInfo.objects.get_or_create(**site_data)

# Execute the population functions
if __name__ == "__main__":
    populate_ride_data()
    populate_site_info_data()
    print("Data populated successfully!")
