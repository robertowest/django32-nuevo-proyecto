from django.contrib import admin

from .models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'apellido_nombre', 'documento', 'fecha_nacimiento', 'edad', 'active']
    list_display_links = ['apellido_nombre']
    list_filter = []
    search_fields = ['apellido', 'nombre', 'documento']
    ordering = ['apellido', 'nombre']

    def apellido_nombre(self, obj):
        # custom_field.short_description = u'Custom name'
        return '{0}, {1}'.format(obj.apellido, obj.nombre)
    
    apellido_nombre.short_description = 'Apellido y Nombre'
