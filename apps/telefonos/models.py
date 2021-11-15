from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable
from apps.diccionarios.models import Diccionario


class Telefono(Auditable):
    tipo = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                             null=True, blank=True, default=1,
                             limit_choices_to={'tabla': 'comunicacion', 'active': True})
    texto = models.CharField(max_length=150)

    class Meta:
        db_table = 'comunicaciones'
        verbose_name = 'Comunicación'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return "%s: %s" % (self.tipo, self.texto)
