from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView
from .forms import PublicarForm

# Create your views here.

#View basa en función, para listar publicaciones.
"""def publicaciones_views(request):

    ctx = {
        'publicaciones' : Publicacion.objects.all()
    }

    return render(request, 'publicaciones.html', ctx)"""

# View basa en clase, para listar las publicaciones.
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

# View basada en función, para crear las publicaciones
def publicar_view(request):
    if request.method == "POST":
        # Guarda la data del formulario en la tabla
        form = PublicarForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save()
        return redirect('publicaciones')
    else:
        # Renderizar el html
        form = PublicarForm()
        ctx = {'form' : form}
        return render(request, 'publicaciones/publicar.html', ctx)