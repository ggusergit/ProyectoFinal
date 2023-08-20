from django.shortcuts import render
from AppPublicacion.forms import *
from AppPublicacion.models import *
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# Create your views here.

def inicio(request):
    return render(request, 'AppPublicacion/inicio.html')

def sobre_mi(request):
    return render(request, 'AppPublicacion/sobremi.html')

def publicaciones(request):
    
    publicacion = Publicacion.objects.filter(cuerpo__icontains='a')
    contexto = {"publicacion":publicacion}
    
    return render(request, 'AppPublicacion/publicaciones.html', contexto)

def pubFormulario(request):
    
    if request.method == 'POST':
        miFormulario = PubliFormulario(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            pub = Publicacion(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], autor=informacion['autor'], fecha=informacion['fecha'], imagen=informacion['imagen'])
            pub.save()

            return render(request, 'AppPublicacion/inicio.html')
    else:
        miFormulario = PubliFormulario()
    
    return render(request, 'AppPublicacion/publiFormulario.html', {"miFormulario": miFormulario})


class verPublicacion(DetailView):
    # if request.GET['titulo']:

    #     titulo = request.GET['titulo']
    #     publicacion = Publicacion.objects.filter(titulo__icontains=titulo)
    #     contexto = {'publicacion':publicacion}

    #     return render(request, 'AppPublicacion/verPublicacion.html', contexto)
    # else:
    #     respuesta = 'No enviaste datos'

    #return render(request, 'AppPublicacion/verPublicacion.html')#, {'respuesta':respuesta})

    
    model = Publicacion
    context_object_name = 'publicacion'
    template_name = 'AppPublicacion/verPublicacion.html'

    