from django import forms
from .models import Paciente, Doctor, Cita

class PostForm1(forms.ModelForm):
        class Meta:
            model = Paciente
            fields = ('nombre_paciente', 'direccion_paciente', 'telefono_paciente', 'correo_paciente','sintomas_paciente')

class PostForm2(forms.ModelForm):
        class Meta:
            model = Doctor
            fields = ('nombre_doctor', 'direccion_doctor', 'telefono_doctor', 'correo_doctor','colegiado_doctor','especialidad_doctor')

class PeliculaForm(forms.ModelForm):
        class Meta:
            model = Pelicula
            fields = ('nombre', 'anio', 'actores')

            def __init__ (self, *args, **kwargs):
                super(PeliculaForm, self).__init__(*args, **kwargs)
                self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["actores"].help_text = "Ingrese los Actores que participaron en la película"
                self.fields["actores"].queryset = Actor.objects.all()
