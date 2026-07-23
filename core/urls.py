from django.urls import path
from . import views

urlpatterns = [
    path('', views.vessel_map, name='index'),
]
