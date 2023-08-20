from django.contrib import admin
from django.urls import path
from AppLogin.views import *

urlpatterns = [
    path('login', login_user, name='Login'),
    path('login_ok', login_ok, name='LoginOk'),
    path('registro', register, name="Registro"),
    
    


]
