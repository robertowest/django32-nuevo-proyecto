from django import forms
from django_select2 import forms as s2forms

from crispy_forms import helper, layout

from apps.personas.models import Persona
from apps.domicilios.models import Domicilio
from apps.telefonos.models import Telefono
from .models import Contacto, ContactosTelefonos


class CustomMMCF(forms.ModelMultipleChoiceField):
    '''ManyToMany Custom Field'''
    def label_from_instance(self, member):
        return "%s" % member.telefono


class ContactoForm_OLD(forms.ModelForm):
    telefonos = CustomMMCF(
        queryset=ContactosTelefonos.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Contacto
        fields = ['persona', 'domicilio', 'telefonos', 'active']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Div(
                layout.Div(
                    layout.Row(
                        layout.Column('persona',   css_class='col-12 mb-0'),
                        layout.Column('domicilio', css_class='col-12 mb-0'),
                    ),
                    css_class='col-6'
                ),
                layout.Div(
                    layout.Row(
                        layout.Column('telefonos',   css_class='col-12 mb-0'),
                    ),
                    css_class='col-6'
                ),  
                css_class='row'
            ),
            'active',
        )

        # agregamos los botones de acción ( mr-2 )
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fa fa-save"></i></span><span class="text"> Grabar</span></button>'
        # bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        # self.helper.layout.append(layout.HTML(bCancel))


class ContactoForm(forms.ModelForm):
    # no utilizaré el campo ManyToMany, lo usaré desde un segundo formulario
    persona = forms.ModelChoiceField(
        queryset = Persona.objects.filter(active=True),
        required = False,
        widget = s2forms.ModelSelect2Widget(
            model = Persona,
            search_fields = ['apellido__icontains'],
            attrs = {'data-minimum-input-length': 3, 'style': 'width: 100%;'},
        )
    )
    domicilio = forms.ModelChoiceField(
        queryset = Domicilio.objects.filter(active=True),
        required = False,
        widget = s2forms.ModelSelect2Widget(
            model = Domicilio,
            search_fields = ['nombre__icontains'],
            attrs = {'data-minimum-input-length': 3, 'style': 'width: 100%;'},
        )
    )
    # ManyToMany con Checkbox
    # telefonos = CustomMMCF(
    #     queryset=ContactosTelefonos.objects.all(),
    #     required = False,
    #     widget=forms.CheckboxSelectMultiple
    # )

    class Meta:
        model = Contacto
        fields = ['persona', 'domicilio', 'active']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()

        # agregamos todos los campos
        for fld in self.Meta.fields:
            self.helper.layout.append(fld)

        # agregamos los botones de acción ( mr-2 )
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fa fa-save"></i></span><span class="text"> Grabar</span></button>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))


class ContactoTelefonoUnBoundForm(forms.Form):
    telefono = forms.ModelChoiceField(
        label="",
        queryset=Telefono.objects.filter(active=True),
        required=False,
        widget=s2forms.ModelSelect2Widget(
            model=Telefono,
            search_fields=['texto__icontains'],
            attrs={'data-minimum-input-length': 3, 'style': 'width: 100%;'},
        )
    )

    class Meta:
        model = Telefono
        fields = ['telefono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()

        # agregamos todos los campos
        for fld in self.Meta.fields:
            self.helper.layout.append(fld)
