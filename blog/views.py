from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Paciente, Doctor
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
    pac = Paciente.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'pac': pac})

def lista2(request):
    doc = Doctor.objects.filter(fecha_publicacion2__lte=timezone.now()).order_by('fecha_publicacion2')
    return render(request, 'blog/listar2.html', {'doc': doc})


def detalle(request, pk):
    det = get_object_or_404(Paciente, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})

def detalle2(request, pk):
    det = get_object_or_404(Doctor, pk=pk)
    return render(request, 'blog/detalle2.html', {'det': det})


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
def editar2(request, pk):
        post = get_object_or_404(Doctor, pk=pk)
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
def borrador(request):
    draft = Paciente.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/borrador.html', {'draft': draft})

@login_required
def borrador2(request):
    draft = Doctor.objects.filter(fecha_publicacion2__isnull=True).order_by('fecha_creacion2')
    return render(request, 'blog/borrador2.html', {'draft': draft})


@login_required
def paciente(request, pk):
    pu = get_object_or_404(Paciente, pk=pk)
    pu.publish()
    return redirect('detalle', pk=pk)

@login_required
def doctor(request, pk):
    do = get_object_or_404(Doctor, pk=pk)
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
    rv = get_object_or_404(Paciente, pk=pk)
    rv.delete()
    return redirect('/')

@login_required
def eliminar2(request, pk):
    rv = get_object_or_404(Doctor, pk=pk)
    rv.delete()
    return redirect('/')
