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
mkdir -p media static/css static/js static/img/favicons static/vendors templates
```

Para poder utilizar diferentes configuraciones de entornos, conservaremos el archivo `settings.py` original pero con otro nombre, así podremos crear diferentes archivos de configuración con el nombre **settings.py** 

```bash
mv config/settings.py config/base.py
echo "from config.base import *" > config/settings.py
```

Creamos un nuevo 'settings.py' con nuestra configuración:

```python
from config.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'
```

En este momento, nuestro árbol de directorios/archivos será similar a este:

```
miproyecto
├── config
│   ├── asgi.py
│   ├── base.py
│   ├── __init__.py
│   ├── settings.py
│   ├── settings.txt
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
├── README.txt
├── requirements.txt
├── static
│   ├── css
│   ├── img
│   ├── js
│   └── vendors
└── templates
```

agregamos la app `comunes` dentro de nuestro proyecto (el árbol quedaría así)
agregamos 'comunes' y lo agregamos a INSTALLED_APPS

creación de los archivos po
./manage.py makemessages  --locale=es --locale=en


https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free