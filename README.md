[Pantalla](pantalla.png)

Creamos un proyecto vacío

```bash
mkdir miproyecto
cd miproyecto
python3 -m venv .venv
pip install django
django-admin startproject config .
```

Creamos las carpetas que necesitaremos más adelante

```bash
mkdir -p apps content/locale content/static/css content/static/img/favicons content/static/js content/static/vendors content/templates media
```

Para poder utilizar diferentes configuraciones de entornos, conservaremos el archivo `settings.py` sin tocarlo demasiado. Para ello agregaremos al final del archivo las siguientes líneas:

```python
# configuramos nuestra entorno dependiendo de la configuración definida
import os
if os.environ.get('IS_PRODUCTION'):
    from config.environment.production.settings import *
else:
    from config.environment.development.settings import *
```

Ahora podremos crear tantos archivos de configuraciones como entornos tengamos:

```bash
mkdir -p config/environment/development config/environment/production
touch config/environment/development/settings.py
touch config/environment/production/settings.py
```

Y como ejemplo, agregamos las siguientes líneas a nuestro entorno de desarrollo

```python
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CONTENT_DIR = settings.BASE_DIR / 'content'
DEBUG = True
ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Inglés')),
]
```

En este momento, nuestro árbol de directorios/archivos será similar a este:

```
miproyecto
├── apps
├── config
│   ├── asgi.py
│   ├── environment
│   │   ├── development
│   │   │   ├── __init__.py
│   │   │   └── settings.py
│   │   └── production
│   │       ├── __init__.py
│   │       └── settings.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── content
│   ├── locale
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   │   └── favicons
│   │   ├── js
│   │   └── vendors
│   └── templates
├── media
└── manage.py
```

Agregamos la carpeta `core` a nuestro proyecto (el árbol quedaría así)
FALTA: definir lo que hay que hacer para que CORE quede operativo sin dar error

creación de los archivos po
./manage.py makemessages  --locale=es --locale=en


https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free