from django.shortcuts import render
from AppLogin.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# def inicio(request):
#     return render(request, 'AppPublicacion/inicio.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppLogin/login_ok.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppLogin/login_ok.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppLogin/login_ok.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {"form": form})

def login_ok(request):
    return render(request, 'AppLogin/login_ok.html')



def register(request):


    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppLogin/login_ok.html" ,  {"mensaje":"Usuario Creado :)"})

    else:  
        form = UserRegisterForm()     

    return render(request,"AppLogin/registro.html" ,  {"form":form})

