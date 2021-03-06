from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CONTENT_DIR = settings.BASE_DIR / 'content'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 10 DEBUG   - Mensajes relacionados con el desarrollo que serán ignorados (o eliminados)en un despliegue de producción
# 20 INFO    - Mensajes informativos para el usuario
# 25 SUCCESS - Una acción fue exitosa, por ejemplo, "Su perfil se actualizó correctamente"
# 30 WARNING - No se produjo un fallo pero puede ser inminente
# 40 ERROR   - Una acción no tuvo éxito o se produjo alguna otra falla
MESSAGE_LEVEL = 10  # DEBUG


# -------------------------------------------------------------------
# internalización
# -------------------------------------------------------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Inglés')),
]


# -------------------------------------------------------------------
# reglas de validación para la clave de autenticación
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = []


# -------------------------------------------------------------------
# archivos estáticos, multimedia y traducciones
# -------------------------------------------------------------------
STATIC_ROOT = CONTENT_DIR / 'static' / 'assets'
STATIC_URL = '/static/'

MEDIA_ROOT = CONTENT_DIR / 'media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [CONTENT_DIR / 'static']
LOCALE_PATHS = [CONTENT_DIR / 'locale']


# -------------------------------------------------------------------
# ubicación de los templates públicos
# -------------------------------------------------------------------
settings.TEMPLATES[0]['DIRS'] = [CONTENT_DIR / 'templates']


# -------------------------------------------------------------------
# configuración del correo electrónico
# -------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/emails'
EMAIL_HOST_USER = 'test@example.com'
DEFAULT_FROM_EMAIL = 'test@example.com'


# -------------------------------------------------------------------
# configuración para el uso de app 'accounts'
# -------------------------------------------------------------------
ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = False
RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True
SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']


# -------------------------------------------------------------------
# tiempo de sesión
# -------------------------------------------------------------------
SESSION_COOKIE_AGE = 36000  # tiempo de vida de la sesión (10 minutos)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # cerrar sesión al cerrar navegador


# -------------------------------------------------------------------
# configuración para debug
# -------------------------------------------------------------------
if DEBUG:
    settings.INSTALLED_APPS += ['debug_toolbar',]
    settings.MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}


# -------------------------------------------------------------------
# aplicaciones de terceros
# -------------------------------------------------------------------
settings.INSTALLED_APPS += [
    'crispy_forms',
    'django_tables2',
    'django_filters',
    'django_select2',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# posibles variables para select2
# SELECT2_JS = 'assets/js/select2.min.js'
# SELECT2_CSS = 'assets/css/select2.css'
# SELECT2_I18N_PATH = 'assets/js/i18n'


# -------------------------------------------------------------------
# aplicaciones del proyecto
# -------------------------------------------------------------------
settings.INSTALLED_APPS += [
    'core.accounts',
    'core.comunes',

    'apps.diccionarios',
    'apps.personas',
    'apps.domicilios',
    'apps.telefonos',
]
