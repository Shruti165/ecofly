from django.shortcuts import render
from .models import Ride, SiteInfo

def ride_match(request):
    rides = Ride.objects.all()
    return render(request, 'paragliding/ride_match.html', {'rides': rides})

def site_info(request):
    sites = SiteInfo.objects.all()
    return render(request, 'paragliding/site_info.html', {'sites': sites})
