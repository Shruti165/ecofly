from django.urls import path
from . import views

app_name = 'paragliding'

urlpatterns = [
    path('ride-match/', views.ride_match, name='ride_match'),
    path('site-info/', views.site_info, name='site_info'),
]
