from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )






from crispy_forms import helper, layout
from django import forms
from django_select2 import forms as s2forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'active']

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

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-2"><span class="icon text-white-50"><i class="fa fa-save"></i></span><span class="text"> Grabar</span></button>'
        # bCancel = '<a class="btn btn-sm btn-warning btn-icon-split" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        # bCancel (href): object.get_detail_url / request.META.HTTP_REFERER
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        # self.helper.layout.append(layout.HTML(bCancel))
