# paragliding/management/commands/populate_ecofly_data.py
from django.core.management.base import BaseCommand
from paragliding.models import Ride, SiteInfo
from marketplace.models import EquipmentListing, Event
from sustainability.models import SustainabilityPractice, Incentive
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populates the EcoFly database with sample data'

    def handle(self, *args, **kwargs):
        # Populate Ride data
        for i in range(10):
            Ride.objects.create(
                origin=f"City {i}",
                destination=f"Flying Site {i % 5}",
                departure_time=datetime.now() + timedelta(hours=random.randint(1, 48)),
                capacity=random.randint(2, 5),
                available_seats=random.randint(1, 4),
                preferences="Non-smoking, extra baggage space",
            )

        # Populate SiteInfo data
        site_names = ["Bir", "Panchgani", "Kerala", "Goa", "Assam"]
        for name in site_names:
            SiteInfo.objects.create(
                name=name,
                description=f"{name} is a popular paragliding site known for its unique landscapes and favorable weather conditions.",
                weather="Sunny" if name in ["Goa", "Bir"] else "Cloudy",
                best_flying_times="October to March",
                local_regulations="Basic paragliding license required",
                safety_tips="Carry extra water, follow weather updates",
            )

        # Populate EquipmentListing data
        equipment_names = ["Beginner Glider", "Advanced Harness", "Reserve Parachute", "Flight Helmet", "GPS Device"]
        for i in range(10):
            EquipmentListing.objects.create(
                name=f"{equipment_names[i % 5]} Model {i + 1}",
                description=f"This {equipment_names[i % 5]} is ideal for paragliding in varied weather conditions.",
                price=random.randint(10000, 50000),
                seller=f"Pilot {i + 1}",
                site="Bir" if i % 2 == 0 else "Panchgani",
                contact_info=f"contact{i}@example.com",
            )

        # Populate Event data
        event_types = ["Meetup", "Training", "Competition"]
        for i in range(10):
            Event.objects.create(
                name=f"{event_types[i % 3]} Event {i + 1}",
                location="Kerala" if i % 2 == 0 else "Goa",
                event_date=datetime.now() + timedelta(days=random.randint(1, 60)),
                description=f"A {event_types[i % 3]} for paragliding enthusiasts to connect and improve their skills.",
                capacity=random.randint(5, 20),
                attendees=random.randint(1, 15),
            )

        # Populate SustainabilityPractice data
        practices = [
            "Use reusable water bottles",
            "Share rides to flying sites",
            "Opt for environmentally friendly equipment",
            "Minimize waste at flying sites",
            "Promote responsible flying practices",
            "Encourage wind-powered flying",
            "Support local eco-friendly businesses",
            "Avoid single-use plastics",
            "Recycle old equipment",
            "Adopt low-emission transportation to sites",
        ]
        for practice in practices:
            SustainabilityPractice.objects.create(
                description=practice,
                user_submitted=True,
            )

        # Populate Incentive data
        for i in range(10):
            Incentive.objects.create(
                title=f"Incentive {i + 1}",
                description="Earn points by participating in eco-friendly practices.",
                points=random.randint(10, 50),
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated EcoFly database with sample data."))
