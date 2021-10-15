from crispy_forms import helper, layout
from django_filters import FilterSet, CharFilter

from .models import Diccionario


class DiccionarioFilter(FilterSet):
    texto = CharFilter(label='Texto', lookup_expr='icontains')

    class Meta:
        model = Diccionario
        fields = ['tabla', 'texto', 'active']


class DiccionarioFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter mr-1"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/{}/listado/"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'
        
        # app_name = __package__.split('.')[1]

        self.layout = layout.Layout(
            'tabla',
            'texto',
            'active',
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar.format("diccionarios")),
                css_class="d-flex justify-content-center",
            ),
        )
