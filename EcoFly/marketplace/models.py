# marketplace/models.py
from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class EquipmentListing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller= models.ForeignKey(User, on_delete=models.CASCADE)  # Correct foreign key

    def __str__(self):
        return self.name
