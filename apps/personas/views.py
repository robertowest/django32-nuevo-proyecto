from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView

from core.audit.models import AuditableMixin
from core.comunes.utils import PagedFilteredTableView, where_are_we_going

from .models import Persona
from .tables import PersonaTable
from .filters import PersonaFilter, PersonaFilterForm
from .forms import PersonaForm


class PersonaTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return PersonaListView.as_view()(request)


class PersonaListView(PermissionRequiredMixin, PagedFilteredTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = '{domain}.view_{app}'.format(domain='personas', app='personas')
    model = Persona
    table_class = PersonaTable              # SingleTableView
    filter_class = PersonaFilter            # PagedFilteredTableView
    formhelper_class = PersonaFilterForm    # PagedFilteredTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        model = self.model
        context = super(PersonaListView, self).get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class PersonaCreateView(AuditableMixin, PermissionRequiredMixin, generic.CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}.add_{app}'.format(domain='personas', app='personas')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class PersonaDetailView(PermissionRequiredMixin, generic.DetailView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = '{domain}.view_{app}'.format(domain='personas', app='personas')
    model = Persona
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle_modal.html'


class PersonaUpdateView(AuditableMixin, PermissionRequiredMixin, generic.UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}.change_{app}'.format(domain='personas', app='personas')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    # def has_permission(self, request):
    #     return request.user.is_active and request.user.is_staff
    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class PersonaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}.del_{app}'.format(domain='personas', app='personas')
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        #reverse_lazy('persona:detail', args=(self.object.pk,))
        return reverse_lazy('persona:list')
