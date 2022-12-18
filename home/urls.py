from django.urls import path

from . import views
from .models import Diseases

app_name = 'home'
urlpatterns = [
    path('', views.home_site, name='home'),
    path('disease/<int:disease_id>', views.disease, name='disease'),
    path('disease/<int:disease_id>/results', views.results, name='results'),
]

