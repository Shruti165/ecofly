from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paragliding/', include('paragliding.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('sustainability/', include('sustainability.urls')),
]
