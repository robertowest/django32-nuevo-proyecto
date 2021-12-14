from django.contrib import admin

from apps.telefonos.models import Telefono
from .models import Contacto, ContactosTelefonos


# class TelefonosInLine(admin.TabularInline):
#     model = Telefono
#     fields = ['tipo', 'texto', 'active']
#     ordering = ['tipo', 'texto']
#     extra = 0
#     can_delete = False
#     # show_change_link = True    
#     view_on_site = False
class TelefonosInLine(admin.TabularInline):
    model = ContactosTelefonos
    fields = ['contacto', 'telefono']
    extra = 0
    can_delete = False
    # show_change_link = True    
    view_on_site = False


@admin.register(Contacto)
class ContactosAdmin(admin.ModelAdmin):
    raw_id_fields = ['persona', 'domicilio']
    autocomplete_fields = ['persona', 'domicilio']
    list_display = ['id', 'persona', 'domicilio']
    list_display_links = ['persona']
    ordering = ['persona']
    inlines = [TelefonosInLine]
