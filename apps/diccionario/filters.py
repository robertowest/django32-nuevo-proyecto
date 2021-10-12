from crispy_forms import bootstrap, helper, layout
from django import forms
from django_filters import FilterSet, CharFilter

from .models import Diccionario


class DiccionarioFilter(FilterSet):
    texto = CharFilter(label='Texto', lookup_expr='icontains')

    class Meta:
        model = Diccionario
        fields = ['texto', 'tabla', 'active']


class DiccionarioFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter mr-1"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/diccionario/listado/"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Row(
                layout.Div('tabla', css_class='col-lg-5 col-md-4 col-sm-6 mb-0'),
                layout.Div('active', css_class='col-lg-2 col-md-4 col-sm-6 mb-0'),
            ),
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar),
                css_class="float-right",
            ),
        )
