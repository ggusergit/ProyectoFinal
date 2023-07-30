from django.shortcuts import render
from AppLogin.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'AppLogin/inicio.html')

def login(request):
    return render(request, 'AppLogin/login.html')

def sobre_mi(request):
    return render(request, 'AppLogin/sobremi.html')