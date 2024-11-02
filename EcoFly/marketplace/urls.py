from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('equipment-listings/', views.equipment_listings, name='equipment_listings'),
    path('meetups/', views.meetups, name='meetups'),
]
