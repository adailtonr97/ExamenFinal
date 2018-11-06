from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Paciente
from .forms import PostForm1
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def lista(request):
    pac = Paciente.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'pac': pac})

def principal(request):
    return render(request, 'blog/principal.html')

def menu(request):
    return render(request, 'blog/menu.html')

def base(request):
    return render(request, 'blog/base.html')

def detalle(request, pk):
    det = get_object_or_404(Paciente, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})

@login_required
def nuevo(request):
        if request.method == "POST":
            form = PostForm1(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.save()
                return redirect('detalle', pk=p.pk)
        else:
            form = PostForm1()
        return render(request, 'blog/editar.html', {'form': form})

@login_required
def editar(request, pk):
        post = get_object_or_404(Paciente, pk=pk)
        if request.method == "POST":
            form = PostForm1(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detalle', pk=post.pk)
        else:
            form = PostForm1(instance=post)
        return render(request, 'blog/editar.html', {'form': form})

@login_required
def borrador(request):
    draft = Paciente.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/borrador.html', {'draft': draft})

@login_required
def paciente(request, pk):
    pu = get_object_or_404(Paciente, pk=pk)
    pu.publish()
    return redirect('detalle', pk=pk)

def publish(self):
    self.fecha_publicacion = timezone.now()
    self.save()

@login_required
def eliminar(request, pk):
    rv = get_object_or_404(Paciente, pk=pk)
    rv.delete()
    return redirect('/')
