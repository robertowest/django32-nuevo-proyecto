from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView as ReadView, 
                                  UpdateView, 
                                  DeleteView)

class TemplateView(TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return ListView.as_view()(request)


class ListView(ListView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    pass


class CreateView(CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    pass


class ReadView(ReadView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    pass


class UpdateView(UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    pass


class DeleteView(DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    pass

