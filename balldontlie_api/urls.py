# URLS.py

from django.urls import path
from .views import get_teams

urlpatterns = [
    path('teams/', get_teams, name='get-teams'),
]