from django.urls import path
from .views import api_home

urlpatterns = [
    path('',api_home), # Localhost:8000/api/
]