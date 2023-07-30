from django.contrib import admin
from django.urls import path
from AppLogin.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('login', login, name='Login'),
    path('sobremi', sobre_mi, name='Sobremi'),

]
