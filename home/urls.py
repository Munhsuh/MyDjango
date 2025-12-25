# home/urls.py     it was created by the dev  in August 7, 2025

# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tour-packages/', views.tour_packages, name='tour_packages'),
    path('food/', views.food, name='food'),
    path('nomads/', views.nomads, name='nomads'),
    path('contact/', views.contact, name='contact'),  # Add this line
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),

    # ... other URLs ...
    path('guestbook/', views.guestbook, name='guestbook'),
]


from .views import load_data_view

urlpatterns += [
    path('load-data/', load_data_view),
]
