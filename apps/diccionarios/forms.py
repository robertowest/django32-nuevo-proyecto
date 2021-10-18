from crispy_forms import helper, layout
from django import forms

from .models import Diccionario


class DiccionarioForm(forms.ModelForm):
    class Meta:
        model = Diccionario
        fields = ['tabla', 'texto', 'texto_corto', 'active']

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
        # bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        # self.helper.layout.append(layout.HTML(bCancel))
