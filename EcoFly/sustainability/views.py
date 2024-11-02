from django.shortcuts import render
from .models import SustainabilityPractice, Incentive

def sustainability_innovation(request):
    practices = SustainabilityPractice.objects.all()
    return render(request, 'sustainability/sustainability_innovation.html', {'practices': practices})

def incentives(request):
    incentives = Incentive.objects.all()
    return render(request, 'sustainability/incentives.html', {'incentives': incentives})
