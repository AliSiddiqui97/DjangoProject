from django.urls import path

from . import views

from rest_framework import routers
from .api import DestinationViewSet


urlpatterns = [
    path('',views.index,name='home'),

   
    
]

