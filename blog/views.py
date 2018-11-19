from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Grado, Materia, Asignacion
from .forms import PostForm1, PostForm2
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def principal(request):
    return render(request, 'blog/principal.html')


def base(request):
    return render(request, 'blog/base.html')

def base2(request):
    return render(request, 'blog/base2.html')


def lista(request):
    gra = Grado.objects.order_by('fecha_creacion')
    return render(request, 'blog/listar.html', {'gra': gra})

def lista2(request):
    mat = Materia.objects.filter(fecha_publicacion2__lte=timezone.now()).order_by('fecha_publicacion2')
    return render(request, 'blog/listar2.html', {'mat': mat})


def detalle(request, pk):
    det = get_object_or_404(Grado, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})

def detalle2(request, pk):
    det = get_object_or_404(Materia, pk=pk)
    return render(request, 'blog/detalle2.html', {'det': det})


@login_required
def nuevo(request):
        if request.method == "POST":
            form = PostForm1(request.POST)
            if form.is_valid():
                grado = Grado.objects.create(nombre_grado=form.cleaned_data['nombre_grado'], seccion_grado=form.cleaned_data['seccion_grado'] )
                for materia_id in request.POST.getlist('materias'):
                    asignaciones = Asignacion(materia_id=materia_id, grado_id = grado.id)
                    asignaciones.save()
                    messages.add_message(request, messages.SUCCESS, 'Asignacion efectuada correctamente')
        else:
            form = PostForm1()
        return render(request, 'blog/editar.html', {'form': form})

@login_required
def nuevo2(request):
        if request.method == "POST":
            form = PostForm2(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.save()
                return redirect('detalle2', pk=p.pk)
        else:
            form = PostForm2()
        return render(request, 'blog/editar2.html', {'form': form})

@login_required
def editar(request, pk):
        post = get_object_or_404(Grado, pk=pk)
        if request.method == "POST":
            form = PostForm1(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('lista')
        else:
            form = PostForm1(instance=post)
        return render(request, 'blog/editar.html', {'form': form})

@login_required
def editar2(request, pk):
        post = get_object_or_404(Materia, pk=pk)
        if request.method == "POST":
            form = PostForm2(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detalle2', pk=post.pk)
        else:
            form = PostForm2(instance=post)
        return render(request, 'blog/editar2.html', {'form': form})


@login_required
def grado(request, pk):
    pu = get_object_or_404(Grado, pk=pk)
    pu.publish()
    return redirect('detalle', pk=pk)

@login_required
def materia(request, pk):
    do = get_object_or_404(Materia, pk=pk)
    do.publish()
    return redirect('detalle2', pk=pk)



def publish(self):
    self.fecha_publicacion = timezone.now()
    self.save()

def publish2(self):
    self.fecha_publicacion2 = timezone.now()
    self.save()


@login_required
def eliminar(request, pk):
    rv = get_object_or_404(Grado, pk=pk)
    rv.delete()
    return redirect('/')

@login_required
def eliminar2(request, pk):
    rv = get_object_or_404(Materia, pk=pk)
    rv.delete()
    return redirect('/')
