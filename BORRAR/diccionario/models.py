from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable


class Diccionario(Auditable):
    TABLA = (
        ('comunicacion', _('Comunicaciones')),
        ('tipo_domicilio', _('Tipo de Domicilio')),
        ('tipo_calle', _('Tipo de Calle')),
        ('tipo_documento', _('Tipo de Documento')),
    )

    texto = models.CharField(max_length=150)
    codigo = models.CharField(max_length=5, null=True, blank=True, unique=True)
    tabla = models.CharField(max_length=25, choices=TABLA, default='comunicacion')

    class Meta:
        db_table = 'diccionario'
        verbose_name = _('Diccionario')
        verbose_name_plural = _('Diccionarios')

    def __str__(self):
        return self.texto

    def get_texto(self):        
        return "{0} ({1})".format(self.texto, self.get_tabla_display())
