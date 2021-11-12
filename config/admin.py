# # ---------------------------------------------------------------------
# # registra todos los modelos
# # se debe ejecutar al final de todo, por si ya existe alguna definición
# # ---------------------------------------------------------------------
# from django.apps import apps
# from django.contrib import admin, sites

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


def my_get_app_list(self, request):
    """
    Devuelve una lista ordenada de todas las aplicaciones 
    instaladas que se han registrado en este sitio. 
    """
    # recuperamos el listado original
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    # aplicamos ordenamiento personalizado
    for app in app_list:
        if app['app_label'] == 'auth':
            ordering = {
                'User': 1,
                'Group': 2
            }
            app['models'].sort(key=lambda x: ordering[x['object_name']])
        # elif app['app_label'] == 'domicilio':
        #     ordering = {
        #         'User': 1,
        #         'Group': 2
        #     }
        #     app['models'].sort(key=lambda x: ordering[x['object_name']])

    return app_list
