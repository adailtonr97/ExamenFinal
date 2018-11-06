from django import forms
from .models import Paciente, Doctor

class PostForm1(forms.ModelForm):

        class Meta:
            model = Paciente
            fields = ('nombre_paciente', 'direccion_paciente', 'telefono_paciente', 'correo_paciente','sintomas_paciente', 'doctores')

            def __init__ (self, *args, **kwargs):
                super(PostForm3, self).__init__(*args, **kwargs)
                self.fields["doctores"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["doctores"].help_text = "Seleccione al doctor"
                self.fields["doctores"].queryset = Doctor.objects.all()

class PostForm2(forms.ModelForm):

        class Meta:
            model = Doctor
            fields = ('nombre_doctor', 'direccion_doctor', 'telefono_doctor', 'correo_doctor','colegiado_doctor','especialidad_doctor')
