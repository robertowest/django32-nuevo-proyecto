from django import forms
from django_select2 import forms as s2forms

from crispy_forms import helper, layout

from .models import Persona


class ComunicacionSelectWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'texto__istartswith'
    ]

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'genero', 'active']
        widgets = {
            # 'comunicacion': ComunicacionSelectWidget(
            #     attrs = {
            #         'data-minimum-input-length': 4,
            #         'data-placeholder': '-- seleccione una opción --',
            #     },
            #     max_results = 10
            # ),
            'fecha_nacimiento': forms.TextInput(
                attrs={'class':'form-control', 'placeholder': 'dd/mm/aaaa', 'type':'date'}
            ),
        }
        labels = {
            'documento': 'Nro. Documento',
            'fecha_nacimiento': 'Fecha Nacimiento',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('nombre', css_class='col-lg-6 col-md-6 mb-0'),
                layout.Column('apellido', css_class='col-lg-6 col-md-6 mb-0'),
            ),
            layout.Row(
                layout.Column('documento',        css_class='col-lg-4 mb-0'),
                layout.Column('fecha_nacimiento', css_class='col-lg-4 mb-0'),
                layout.Column('genero',           css_class='col-lg-4 mb-0'),
            ),
            'active',
        )

        # agregamos los botones de acción ( mr-2 )
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fa fa-save"></i></span><span class="text"> Grabar</span></button>'
        # bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        # self.helper.layout.append(layout.HTML(bCancel))
