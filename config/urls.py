"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('cambiar_lenguaje/', 
            TemplateView.as_view(template_name='config/cambiar_lenguaje.html'), 
            name='cambiar_lenguaje'),
]


# -------------------------------------------------------------------
# incluimos las urls de cada aplicación
# -------------------------------------------------------------------
from django.views.generic import TemplateView

urlpatterns += [
    path('', TemplateView.as_view(template_name="base.html"), name='home'),

    path('usuarios/', include('core.usuarios.urls')),
]


# -----------------------------------------------------------------------------
# DEBUG
# -----------------------------------------------------------------------------
from django.conf import settings

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
