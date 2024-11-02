from django.shortcuts import render
from .models import EquipmentListing, Event

def equipment_listings(request):
    listings = EquipmentListing.objects.all()
    return render(request, 'marketplace/equipment_listings.html', {'listings': listings})

def meetups(request):
    meetups = Meetup.objects.all()
    return render(request, 'marketplace/meetups.html', {'meetups': meetups})
