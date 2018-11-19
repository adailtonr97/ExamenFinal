from django.db import models
from django.contrib import admin
from django.utils import timezone

class Materia(models.Model):
        nombre_materia = models.CharField(max_length=200)
        creditos_materia = models.CharField(max_length=200)
        profesor_materia = models.CharField(max_length=200)
        fecha_creacion2 = models.DateTimeField(
                default=timezone.now)
        fecha_publicacion2 = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.fecha_publicacion2 = timezone.now()
            self.save()

        def __str__(self):
            return self.nombre_doctor

class Grado(models.Model):
        nombre_grado = models.CharField(max_length=200)
        seccion_grado = models.CharField(max_length=200)

        fecha_creacion = models.DateTimeField(
                default=timezone.now)
        fecha_publicacion = models.DateTimeField(
                blank=True, null=True)
        materias = models.ManyToManyField(Materia, through='Cita')

        def publish(self):
            self.fecha_publicacion = timezone.now()
            self.save()

        def __str__(self):
            return self.nombre_grado


class Asignacion(models.Model):
        fecha_asignacion = models.DateTimeField(default=timezone.now)
        materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
        grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

        def publish(self):
            self.fecha_asignacion = timezone.now()
            self.save()

class AsignacionInLine(admin.TabularInline):
        model = Cita
        extra = 1

class MateriaAdmin(admin.ModelAdmin):
        inlines = (AsignacionInLine,)

class GradoAdmin(admin.ModelAdmin):
        inlines = (AsignacionInLine,)
