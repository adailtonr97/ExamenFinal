from django import forms
from .models import Paciente

class PostForm1(forms.ModelForm):
        class Meta:
            model = Paciente
            fields = ('nombre_paciente', 'direccion_paciente', 'telefono_paciente', 'correo_paciente','sintomas_paciente')
