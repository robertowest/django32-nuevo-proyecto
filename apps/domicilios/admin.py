# departamentos / localidades
# https://www.colesctuc.com/index.php/es/publicaciones-de-interes/8-informativo/85-departamentos-y-municipios-de-tucuman

from django.contrib import admin

from .models import Pais, Provincia, Departamento, Localidad, Domicilio


# ordenamos la lista de aplicaciones según el orden definido de los modelos
from config.admin import my_get_app_list
admin.AdminSite.get_app_list = my_get_app_list


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    # list_display = [f.name for f in Diccionario._meta.get_fields()]
    list_display = ['id', 'nombre', 'cod_area_tel', 'active']
    list_display_links = ['nombre']
    # list_filter = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    raw_id_fields = ['pais']
    list_display = ['id', 'nombre', 'active']
    list_display_links = ['nombre']
    list_filter = ['pais__nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    fields = ['pais', 'nombre', 'active']


class LocalidadInLine(admin.TabularInline):
    # list_display = ['id', 'departamento', 'nombre', 'cod_postal', 'cod_area_tel', 'active']
    # list_display_links = ['nombre']
    # list_filter = ['departamento__nombre']
    # search_fields = ['nombre']
    # ordering = ['nombre']
    model = Localidad
    fields = ['nombre', 'cod_postal', 'cod_area_tel', 'active']
    # readonly_fields = fields
    ordering = ['nombre']
    extra = 0
    can_delete = False
    # show_change_link = True    
    view_on_site = False


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'active']
    list_display_links = ['nombre']
    list_filter = ['provincia__nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    fields = ['provincia', 'nombre', 'active']
    inlines = [LocalidadInLine]


@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    raw_id_fields = ['provincia', 'departamento', 'localidad']
    # list_display = [f.name for f in Domicilio._meta.get_fields() if f.name not in Domicilio.exclude_fields]
    list_display = ['id', 'domicilio_corto', 'active']
    list_display_links = ['domicilio_corto']
    # list_filter = ['localidad']
    search_fields = ['nombre']
    ordering = ['nombre']
