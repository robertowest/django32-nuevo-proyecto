from django import forms

from .models import Diccionario


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Diccionario
        exclude = ('model_state',)
    
    def clean_texto(self):
        data = self.cleaned_data['texto']
        if data != '' or data is not None:
            print("Hola desde form personalizado")
        return data
