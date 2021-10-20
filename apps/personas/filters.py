from crispy_forms import helper, layout
from django_filters import FilterSet, CharFilter

from .models import Persona


class PersonaFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']



class PersonaFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter mr-1"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/{}/listado/"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'
        
        self.layout = layout.Layout(
            'apellido',
            'nombre',
            'documento',
            'active',
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar.format( __package__.split('.')[1] )),
                css_class="d-flex justify-content-center",
            ),
        )
