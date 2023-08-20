from django.contrib import admin
from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_user, name='Login'),
    path('login_ok', login_ok, name='LoginOk'),
    path('registro', register, name="Registro"),
    path('logout', LogoutView.as_view(template_name='AppLogin/logout.html'),name='Logout'), 
    path('editarPerfil', editarPerfil, name='EditarPerfil'),


]
