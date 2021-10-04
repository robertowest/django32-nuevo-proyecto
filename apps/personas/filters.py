from crispy_forms import bootstrap, helper, layout
from django import forms
from django_filters import FilterSet, CharFilter
from django.utils.translation import gettext_lazy as _

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
        bURL = "{% url 'personas:list' %}"
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="{{bURL}}"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Row(
                layout.Div('nombre', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Div('apellido', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Div('documento', css_class='col-lg-2 col-md-2 col-sm-6 mb-0'),
                layout.Div('active', css_class='col-lg-2 col-md-2 col-sm-6 mb-0'),
            ),
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar),
                css_class="float-right",
            ),
        )


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class PersonaFilterModal(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento']

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            data.setdefault("documento", "*")
        super(PersonaFilterModal, self).__init__(data, *args, **kwargs)


class PersonaFilterFormModal(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'
        self.form_id = 'frmFilter'
        self.form_action = "#"  # {# url 'personas:domicilio-filtro-modal' #}

        self.layout = layout.Layout(
            layout.Div(
                layout.Fieldset(
                    None,
                    layout.Div(
                        bootstrap.InlineField("nombre", wrapper_class="col-4"),
                        bootstrap.InlineField("apellido", wrapper_class="col-4"),
                        bootstrap.InlineField("documento", wrapper_class="col-4"),
                        css_class="row",
                    ),
                    css_class="col-10",
                ),
                bootstrap.FormActions(
                    layout.Button('btnFilter', 'Buscar', 
                                  css_id="btnFilter", 
                                  css_class='btn btn-primary', 
                                  onclick="ajax_modal_submit(frmFilter);"),
                    css_class="col-2 text-right align-self-center",
                ),
                css_class="row",
            )
        )
