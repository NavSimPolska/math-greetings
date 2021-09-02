# greetings/urls.py
from django.urls import path
from .views import ogolne, imie

urlpatterns = [
   path('', ogolne),
   path('<a>', imie)
]