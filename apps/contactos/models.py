from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable
from apps.domicilios.models import Domicilio
from apps.personas.models import Persona
from apps.telefonos.models import Telefono


class Contacto(Auditable):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE,
                                null=True, blank=True, 
                                limit_choices_to={'active': True}, default=1)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE,
                                  null=True, blank=True, 
                                  limit_choices_to={'active': True}, default=1)
    telefonos = models.ManyToManyField(Telefono, through='ContactosTelefonos')

    class Meta:
        db_table = 'contactos'
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')

    def __str__(self):
        return self.persona.apellido_nombre


class ContactosTelefonos(models.Model):
    contacto = models.ForeignKey(Contacto, models.DO_NOTHING, related_name='contacto_telefonos')
    telefono = models.ForeignKey(Telefono, models.DO_NOTHING, related_name='telefono_contactos')

    class Meta:
        # managed = False
        db_table = 'contactos_telefonos'
        verbose_name = 'Contacto y Teléfono'
        verbose_name_plural = 'Contactos y Teléfonos'
        unique_together = (('contacto', 'telefono'),)
