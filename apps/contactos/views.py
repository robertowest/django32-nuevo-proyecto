from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  DetailView as ReadView, 
                                  UpdateView, 
                                  DeleteView)

from django_tables2 import SingleTableView

from core.audit.models import AuditableMixin
from core.comunes.utils import FilteredTableView, where_are_we_going

from .models import Contacto
from .tables import ContactoTable
from .filters import ContactoFilter, ContactoFilterForm
from .forms import ContactoForm, ContactoTelefonoUnBoundForm


PERMISSION = '{label}.view_{model}'.format(label='contactos', model='contacto')


class MyTemplateView(TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        url = '{}:list'.format(__package__.split('.')[1])
        return HttpResponseRedirect(reverse_lazy(url))


class MyListView(PermissionRequiredMixin, SingleTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Contacto
    table_class = ContactoTable              # SingleTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class MyFilterView(MyListView, FilteredTableView):
    """FilterView se utiliza para la presentación de una tabla con filtro"""
    filter_class = ContactoFilter            # FilteredTableView (filterset_class)
    formhelper_class = ContactoFilterForm    # FilteredTableView
    template_name = 'comunes/tabla.html'


class MyCreateView(AuditableMixin, PermissionRequiredMixin, CreateView):
    pass


class MyReadView(PermissionRequiredMixin, ReadView):
    pass


class MyUpdateView(AuditableMixin, PermissionRequiredMixin, UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    permission_required = PERMISSION.replace("view_", "change_")
    model = Contacto
    form_class = ContactoForm
    # template_name = 'comunes/formulario.html'
    template_name = 'contactos/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = "col-12"
        context['form_2'] = ContactoTelefonoUnBoundForm()   # (instance=self.model())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class MyDeleteView(PermissionRequiredMixin, DeleteView):
    pass