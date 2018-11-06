from django.contrib import admin
from .models import Paciente, Doctor, PacienteAdmin, DoctorAdmin
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
