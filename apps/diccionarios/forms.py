from django import forms

from .models import Diccionario


class DiccionarioForm(forms.ModelForm):
    class Meta:
        model = Diccionario
        exclude = Diccionario.exclude_fields
