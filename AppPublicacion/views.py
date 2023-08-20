from django.shortcuts import render
from AppPublicacion.forms import *
from AppPublicacion.models import *
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
import re


# Create your views here.

def inicio(request):
    return render(request, 'AppPublicacion/inicio.html')

def sobre_mi(request):
    return render(request, 'AppPublicacion/sobremi.html')

@login_required
def publicaciones(request):
    
    publicacion = Publicacion.objects.all()
    contexto = {"publicacion":publicacion}
    
    return render(request, 'AppPublicacion/publicaciones.html', contexto)

def pubFormulario(request):
    
    if request.method == 'POST':
        miFormulario = PubliFormulario(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            u=User.objects.get(username=request.user)
            pub = Publicacion(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], autor=informacion['autor'], fecha=informacion['fecha'], imagen=informacion['imagen'], usuario=u)
            pub.save()

            return render(request, 'AppPublicacion/inicio.html')
    else:
        miFormulario = PubliFormulario()
    
    return render(request, 'AppPublicacion/publiFormulario.html', {"miFormulario": miFormulario})


class verPublicacion(DetailView):
    model = Publicacion
    context_object_name = 'publicacion'
    template_name = 'AppPublicacion/verPublicacion.html'

def eliminarPublicacion(request, pTitulo):
    publicacion = Publicacion.objects.get(titulo=pTitulo)
    publicacion.delete()

    publicacion= Publicacion.objects.all()
    contexto ={'publicacion':publicacion}

    return render(request, 'AppPublicacion/publicaciones.html', contexto)

def editarPublicacion(request, pTitulo):
    #profesor = Profesor.objects.get(nombre=profesor_nombre)
    publicacion = Publicacion.objects.get(titulo = pTitulo)

    if request.method == "POST":
        #miFormulario = ProfesorFormulario(request.POST)
        miFormulario = PubliFormulario(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            publicacion.titulo = informacion['titulo']
            publicacion.subtitulo = informacion['subtitulo']
            publicacion.cuerpo = informacion['cuerpo']
            publicacion.autor = informacion['autor']
            publicacion.fecha = informacion['fecha']
            publicacion.imagen = informacion['imagen']
            publicacion.save()
            
            # profesor.nombre = informacion['nombre']
            # profesor.apellido = informacion['apellido']
            # profesor.email = informacion['email']
            # profesor.profesion = informacion['profesion']

            # profesor.save()

            return render(request, 'AppPublicacion/inicio.html')
    else:
        # miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido,
        #                                            'email':profesor.email, 'profesion': profesor.profesion})
        miFormulario = PubliFormulario(initial={'titulo':publicacion.titulo, 'subtitulo':publicacion.subtitulo, 'cuerpo':publicacion.cuerpo, 'autor':publicacion.autor, 'fecha':publicacion.fecha, 'imagen':publicacion.imagen})
        
        
    #return render(request, 'editarProfesor.html', {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})
    return render(request, 'AppPublicacion/editarPublicacion.html', {'miFormulario':miFormulario, 'publicacion':pTitulo} )

    