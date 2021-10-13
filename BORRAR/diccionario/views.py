from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from core.audit.models import AuditableMixin
from core.comunes.utils import PagedFilteredTableView, where_are_we_going

from .models import Diccionario
from .tables import DiccionarioTable
from .filters import DiccionarioFilter, DiccionarioFilterForm
from .forms import DiccionarioForm

PERMISSION = '{domain}.view_{app}'.format(domain='diccionario', app='diccionario')


class DiccionarioTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return DiccionarioListView.as_view()(request)


class DiccionarioListView(PermissionRequiredMixin, PagedFilteredTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Diccionario
    table_class = DiccionarioTable              # SingleTableView
    filter_class = DiccionarioFilter            # PagedFilteredTableView
    formhelper_class = DiccionarioFilterForm    # PagedFilteredTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super(DiccionarioListView, self).get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class DiccionarioCreateView(AuditableMixin, PermissionRequiredMixin, generic.CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    model = Diccionario
    permission_required = PERMISSION.replace('view_', 'add_')
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class DiccionarioReadView(PermissionRequiredMixin, generic.DetailView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = PERMISSION
    model = Diccionario
    template_name = 'comunes/detalle.html'


class DiccionarioUpdateView(AuditableMixin, PermissionRequiredMixin, generic.UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    model = Diccionario
    permission_required = PERMISSION.replace('view_', 'change_')
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class DiccionarioDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    model = Diccionario
    permission_required = PERMISSION.replace('view_', 'del_')
    success_message = _('Registro eliminado correctamente')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('diccionario:list')
