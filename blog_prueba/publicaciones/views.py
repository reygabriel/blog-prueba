from django.shortcuts import render
from .models import Publicacion

# Create your views here.

def publicaciones_views(request):

    ctx = {
        'publicaciones' : Publicacion.objects.all()
    }

    return render(request, 'publicaciones.html', ctx)