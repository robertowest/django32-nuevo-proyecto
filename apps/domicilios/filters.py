from crispy_forms import helper, layout
from django_filters import FilterSet, CharFilter

from .models import Domicilio


class DomicilioFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    barrio = CharFilter(label='Barrio', lookup_expr='icontains')

    class Meta:
        model = Domicilio
        fields = ['nombre', 'barrio', 'provincia', 'tipo_domicilio', 'tipo_calle', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class DomicilioFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter mr-1"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/{}/listado/"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            'nombre',
            'barrior',
            'provincia',
            'tipo_domicilio',
            'tipo_calle',
            'active',
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar.format("domicilios")),
                css_class="d-flex justify-content-center",
            ),
        )
