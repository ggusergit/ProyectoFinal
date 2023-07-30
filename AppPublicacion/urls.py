from django.contrib import admin
from django.urls import path
from AppPublicacion.views import *

urlpatterns = [
    path('', inicio),
    
]
