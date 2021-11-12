from django import forms

from crispy_forms import helper, layout
from django_select2 import forms as s2forms

from .models import Provincia, Departamento, Localidad, Domicilio


class DomicilioForm(forms.ModelForm):
    provincia = forms.ModelChoiceField(
        required=False,
        queryset=Provincia.objects.filter(active=True).filter(pais_id=1),
        widget=s2forms.ModelSelect2Widget(
            model=Provincia,
            search_fields=['nombre__icontains'],
            attrs = {'data-minimum-input-length': 0},
        )
    )
    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(active=True),
        label='Dpto.', required=False,
        widget=s2forms.ModelSelect2Widget(
            model=Departamento,
            search_fields=['nombre__icontains'],
            dependent_fields={'provincia': 'provincia'},
            attrs = {'data-minimum-input-length': 0},
            max_results=50,
            select2_options={ 'width': '100%' },
        ),
    )
    localidad = forms.ModelChoiceField(
        required=False,
        queryset=Localidad.objects.filter(active=True),
        widget=s2forms.ModelSelect2Widget(
            model=Localidad,
            search_fields=['nombre__icontains'],
            dependent_fields={'departamento': 'departamento'},
            attrs = {'data-minimum-input-length': 0},
            max_results=50,
        )
    )

    class Meta:
        model = Domicilio
        fields = ['tipo_domicilio', 'tipo_calle', 
                  'nombre', 'numero', 'piso', 'puerta', 'barrio', 
                  'provincia', 'departamento', 'localidad', 'observacion', 'active']
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('persona', css_class='col-lg-5 col-md-6 mb-0'),
            ),
            layout.Row(
                layout.Column('tipo_domicilio', css_class='col-lg-3 col-md-6 mb-0'),
                layout.Column('tipo_calle', css_class='col-lg-2 col-md-3 mb-0'),
                layout.Column('nombre', css_class='col-lg-5 col-md-7 mb-0'),
                layout.Column('numero', css_class='col-lg-2 col-md-2 mb-0'),
            ),
            layout.Row(
                layout.Column('piso', css_class='col-lg-2 col-md-2 mb-0'),
                layout.Column('puerta', css_class='col-lg-2 col-md-2 mb-0'),
                layout.Column('barrio', css_class='col-lg-8 col-md-8 mb-0'),
            ),
            layout.Row(
                layout.Column('provincia', css_class='col-lg-4 col-md-4 mb-0'),
                layout.Column('departamento', css_class='col-lg-4 col-md-4 mb-0'),
                layout.Column('localidad', css_class='col-lg-4 col-md-4 mb-0'),
            ),
            'observacion',
            'active',
        )

        # agregamos los botones de acción ( mr-2 )
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fa fa-save"></i></span><span class="text"> Grabar</span></button>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
