from django import forms

class PubliFormulario(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=30000)
    autor = forms.CharField(max_length=30)
    fecha = forms.DateField()
    imagen = forms.ImageField(required=True)