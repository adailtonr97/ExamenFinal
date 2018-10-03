from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .forms import NuevoForm


def post_list(request):
    articulos = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos': articulos})

def detalle(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle.html', {'pub': pub})

def nuevo(request):
    if request.method == "POST":
        formulario = NuevoForm(request.POST)
        if formulario.is_valid():
            p = formulario.save(commit=False)
            p.autor = request.user
            p.fecha_publicacion = timezone.now()
            p.save()
            return redirect('detalle', pk=p.pk)
    else:
        formulario = NuevoForm()
    return render(request, 'blog/editar.html', {'formulario': formulario})

def editar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = NuevoForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle', pk=post.pk)
    else:
        formulario = NuevoForm(instance=post)
    return render(request, 'blog/editar.html', {'formulario': formulario})
