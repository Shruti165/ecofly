from django.urls import path
from . import views

app_name = 'sustainability'

urlpatterns = [
    path('sustainability-innovation/', views.sustainability_innovation, name='sustainability_innovation'),
    path('incentives/', views.incentives, name='incentives'),
]
