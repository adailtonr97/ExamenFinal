from django import forms
from .models import Grado, Materia

class PostForm1(forms.ModelForm):

        class Meta:
            model = Grado
            fields = ('nombre_grado', 'seccion_grado', 'materias')

            def __init__ (self, *args, **kwargs):
                super(PostForm3, self).__init__(*args, **kwargs)
                self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["materias"].help_text = "Seleccione las material"
                self.fields["materias"].queryset = Materia.objects.all()

class PostForm2(forms.ModelForm):

        class Meta:
            model = Materia
            fields = ('nombre_materia', 'creditos_materia', 'profesor_materia')
