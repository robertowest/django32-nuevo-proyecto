import datetime

from django import template
from django.db.models.query import QuerySet

register = template.Library()


# @register.filter
# def appname(obj):
#     # 'app_label': model._meta.app_label,
#     # 'model_name': model._meta.object_name.lower()
#     try:
#         # if isinstance(obj, Model):
#         #     return obj.get_app_label
#         return model._meta.app_label
#     except:
#         return 'unknow_app'


@register.filter
def verbose_name(obj):
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name
    else:
        # return obj._meta.verbose_name
        return obj._meta.model._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    # return obj._meta.verbose_name_plural
    # return obj.__class__.__name__         obj.query.base_table
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name_plural
    else:
        # return obj._meta.verbose_name_plural
        return obj._meta.model._meta.verbose_name_plural


@register.filter
def local_include_exists(value, appname):
    switcher = {
        'pais':'domicilio',
        'provincia':'domicilio',
        'departamento':'domicilio',
        'localidad':'domicilio',
    }
    appname = switcher.get(appname, appname)
    # comprobamos si existe el 'include' en el directorio de la app
    # sino, devolvemos el 'include' global
    file = str(appname) + '/includes/' + str(value) + '.html'
    if template_exists(file):
        return file
    return 'includes/' + str(value) + '.html'


@register.filter
def template_exists(value):
    try:
        template.loader.get_template(value)
        return True
    except template.TemplateDoesNotExist:
        return False


@register.filter
def filtro_active(modelo, valor):
    return modelo.filter(active=valor)


@register.filter
def query(qs, **kwargs):
    ''' template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    '''
    return qs.filter(**kwargs)


@register.filter
def url_action(obj, action):
    if isinstance(obj, QuerySet):
        model_name = obj.model._meta.verbose_name
    else:
        model_name = obj._meta.verbose_name
    return '{obj}:{act}'.format(obj=model_name.lower(), act=action.lower())


@register.filter
def url_action_pk(url, pk):
    return '{url} {id}'.format(url=url, id=pk)


# @register.simple_tag()
@register.filter
def var_dump(var):
    # forma de uso en html: {{ objeto|var_dump }}
    return vars(var)


@register.filter
def analizar(obj):
    return obj.resolver_match.app_name


@register.filter
def formato_dni(valor):
    decimal_points=3
    seperator=u'.'
    value = str(valor)
    if len(value) <= decimal_points:
        return value
    # say here we have value = '12345' and the default params above
    parts = []
    while value:
        parts.append(value[-decimal_points:])
        value = value[:-decimal_points]
    # now we should have parts = ['345', '12']
    parts.reverse()
    # and the return value should be u'12.345'
    return seperator.join(parts)


@register.filter
def formato_fecha(valor):
    return valor.strftime('%d/%m/%Y')


@register.simple_tag
def define(val=None):
    '''
    define una variable dentro de la plantilla
    uso: 
        {% if item %}
            {% define "modificando" as action %}
        {% else %}
            {% define "creando" as action %}
        {% endif %}
        Usted está {{action}} un item !
    '''
    return val


@register.filter(name='url_next')
def url_next(url, next):
    """retornar la clausula next de la url (si la tiene)"""
    if "next=" in url:
        pos = url.find("next=", 1, 100) + len("next=")
        return url[pos:]
    else:
        return next


@register.filter(name='cut_url_next')
def cut_url_next(url):
    """retornar la clausula next de la url"""
    if "next=" in url:
        pos = url.find("next=", 1, 100) + len("next=")
        return url[pos:]
    else:
        return url_next(url, "/home")
