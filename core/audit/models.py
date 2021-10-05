from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


class Auditable(models.Model):
    active = models.BooleanField('Activo', default=True, null=False, blank=False)

    created_on = models.DateTimeField('Creado', auto_now_add=True, editable=False, 
                                      null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
                                   null=True, blank=True, editable=False, \
                                   related_name='%(class)s_created_by', verbose_name='Creado por', \
                                   on_delete=models.CASCADE)

    modified_on = models.DateTimeField('Modificado', auto_now=True, editable=False, 
                                       null=True, blank=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
                                    null=True, blank=True, editable=False, \
                                    related_name='%(class)s_modified_by', verbose_name='Modificado por', \
                                    on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def get_fields(self):
        """Devuelve una lista con los nombres de todos los campos"""
        fields = []
        for f in self._meta.fields:
            # comprobamos que el campo sea del tipo que queremos visualizar
            if f.editable and f.name not in ('id2', 'active'):
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
        return reverse('%s:list' % self._meta.app_label)

    def get_list_url(self):
        return reverse('%s:list' % self._meta.app_label)

    def get_create_url(self):
        return reverse('%s:create' % self._meta.app_label)

    def get_detail_url(self):
        return reverse('%s:detail' % self._meta.app_label, args=(self.pk,))

    def get_update_url(self):
        if self.pk:
            return reverse('%s:update' % self._meta.app_label, args=(self.pk,))
        else:
            return None

    def get_delete_url(self):
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

    def hard_delete(self):
        super(Auditable, self).delete()



class AuditableMixin(object,):
    """Se utilizará para grabar la información del usuario actual"""
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableMixin, self).form_valid(form)


class SQLView(models.Model):
    class Meta:
        abstract = True

    def get_fields(self):
        """Devuelve una lista con los nombres de todos los campos"""
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

    