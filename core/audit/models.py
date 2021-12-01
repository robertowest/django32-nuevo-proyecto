from datetime import datetime

from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _


class Auditable(models.Model):
    active = models.BooleanField(_('Activo'), default=True, null=False, blank=False)

    created_on = models.DateTimeField(_('Creado el'), auto_now_add=True, editable=False, 
                                      null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, editable=False,
                                   related_name='%(class)s_created_by', 
                                   verbose_name=_('Creado por'),
                                   on_delete=models.CASCADE)

    modified_on = models.DateTimeField(_('Modificado el'), auto_now=True, editable=False, 
                                       null=True, blank=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True, blank=True, editable=False,
                                    related_name='%(class)s_modified_by', 
                                    verbose_name=_('Modificado por'),
                                    on_delete=models.CASCADE)

    exclude_fields = ['created_on', 'created_by', 'modified_on', 'modified_by']

    success_create_message = _('Registro creado correctamente')
    success_update_message = _('Registro actualizado correctamente')
    success_delete_message = _('Registro eliminado correctamente')

    error_create_message = _('El registro no pudo ser creado')
    error_update_message = _('El registro no pudo ser modificado')
    error_delete_message = _('El registro no pudo ser eliminado')

    not_found_message = _('No se ha encontrado un registro con estos datos')

    class Meta:
        abstract = True

    # TODO: no logro obtener los campos desde el objeto
    # def get_fields(self):
    #     # exclude = self.exclude_fields.append('active')
    #     # include = [f.name for f in self._meta.get_fields() 
    #     #             if f.name not in self.exclude_fields]
    #     # return include.append('active')
    #     return self.model._meta.fields

    def get_data(self):
        '''Devuelve una lista con los nombres de todos los campos'''
        fields = []
        for f in self._meta.fields:
            # comprobamos que el campo sea del tipo que queremos visualizar
            # if f.editable and f.name not in self.exclude_fields:
            if f.editable and f.name:
                try:
                    value = getattr(self, f.name)
                    if value:
                        if f.choices:
                            fields.append({'name':f.verbose_name, 'value':dict(f.choices)[value],})
                        else:
                            fields.append({'name':f.verbose_name, 'value':value,})
                except:
                    value = None
        return fields

    def get_absolute_url(self):
        try:
            return reverse('%s:list' % self._meta.model_name)
        except:
            return reverse('%s:list' % self._meta.app_label)

    def get_list_url(self):
        return self.get_absolute_url()

    def get_detail_url(self):
        try:
            return reverse('%s:detail' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:detail' % self._meta.app_label, args=(self.pk,))

    def get_create_url(self):
        try:
            return reverse('%s:create' % self._meta.model_name)
        except:
            return reverse('%s:create' % self._meta.app_label)

    def get_read_url(self):
        try:
            return reverse('%s:read' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:read' % self._meta.app_label, args=(self.pk,))

    def get_update_url(self):
        try:
            return reverse('%s:update' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:update' % self._meta.app_label, args=(self.pk,))

    def get_delete_url(self):
        try:
            return reverse('%s:delete' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:delete' % self._meta.app_label, args=(self.pk,))

    def get_verbose_name(self):
        # if isinstance(self, QuerySet):
        #     return self._meta.verbose_name
        # else:
        #     return self.verbose_name
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(Auditable, self).delete(*args,**kwargs)


class AuditableMixin(object,):
    '''Se utilizará para grabar la información del usuario actual'''
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableMixin, self).form_valid(form)


class SQLView(models.Model):
    class Meta:
        abstract = True

    def get_fields(self):
        '''Devuelve una lista con los nombres de todos los campos'''
        fields = []
        for f in self._meta.fields:
            try:
                value = getattr(self, f.name)
                if value:
                    if f.choices:
                        fields.append({'name':f.verbose_name, 'value':dict(f.choices)[value],})
                    else:
                        fields.append({'name':f.verbose_name, 'value':value,})
            except:
                value = None
        return fields

    def get_create_url(self):
        db_table = self._meta.db_table
        if db_table == 'localidades_view':
            db_table = 'localidad'
        return reverse('%s:create' % db_table)

    def get_detail_url(self):
        db_table = self._meta.db_table
        if db_table == 'localidades_view':
            db_table = 'localidad'
        return reverse('%s:detail' % db_table, args=(self.pk,))

    def get_update_url(self):
        db_table = self._meta.db_table
        if db_table == 'localidades_view':
            db_table = 'localidad'
        return reverse('%s:update' % db_table, args=(self.pk,))

    def get_delete_url(self):
        db_table = self._meta.db_table
        if db_table == 'localidades_view':
            db_table = 'localidad'
        return reverse('%s:delete' % db_table, args=(self.pk,))

    