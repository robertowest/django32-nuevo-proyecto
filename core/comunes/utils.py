import os

from django.contrib.contenttypes.models import ContentType

# How to use
# obj = [User].objects.create()
# get_app_name(obj)
# get_model_name(obj)

# __package__.split('.')[1]
# self._meta.verbose_name.lower()

def dictfetchall(cursor):
    "Devuelve todas las filas de un cursor como un diccionario"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_app_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.app_label


def get_template_path(appname, template):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = "{path}/{app}/templates/{app}/{html}".format(path=path, app=appname, html=template)
    if os.path.exists(file):
        template_name = "{app}/{html}".format(app=appname, html=template)
    else:
        template_name = "comunes/{html}".format(html=template)
    return template_name


def get_model_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.model

