from django import forms
from .models import Publicacion, Comentario

class PublicarForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria']

class ActualizarForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria', 'creador']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']