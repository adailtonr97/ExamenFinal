from django.contrib import admin
from .models import Grado, Materia, GradoAdmin, MateriaAdmin
admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
