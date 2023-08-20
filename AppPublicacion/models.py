from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=30000)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    imagen = models.ImageField(null=True, blank=True, upload_to='imagenes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)



