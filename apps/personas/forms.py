from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'tipo_documento', 'documento', 'fecha_nacimiento', 'genero']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['apellido'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['tipo_documento'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['documento'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['fecha_nacimiento'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['genero'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        # self.fields['price'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
