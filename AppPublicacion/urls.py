from django.contrib import admin
from django.urls import path
from AppPublicacion.views import *
from django import views
from . import views

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('sobremi', sobre_mi, name='Sobremi'),
    path('publicaciones', publicaciones, name='Publicaciones'),
    path('pubFormulario', pubFormulario, name='PubFormulario'),
    path('verPublicacion/<int:pk>', verPublicacion.as_view(), name='VerPublicacion'),

    
]
