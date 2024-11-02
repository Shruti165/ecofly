from django.db import models
from django.contrib.auth.models import User


class Ride(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    capacity = models.IntegerField()  # Ensure 'capacity' is defined if it's needed
    preferences = models.CharField(max_length=255, blank=True, null=True)  # Ensure 'preferences' is defined if it's needed

    def __str__(self):
        return f"Ride from {self.origin} to {self.destination} on {self.date} at {self.time}"

class SiteInfo(models.Model):
    name = models.CharField(max_length=100)
    best_time = models.CharField(max_length=200)
    local_regulations = models.TextField()
    weather_conditions = models.TextField()
