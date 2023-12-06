from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView

# Create your views here.

#View basa en función, para listar publicaciones.
"""def publicaciones_views(request):

    ctx = {
        'publicaciones' : Publicacion.objects.all()
    }

    return render(request, 'publicaciones.html', ctx)"""

# View basa en clase, para listar las publicaciones.
class PublicacionesView(ListView):
    template_name = 'publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'