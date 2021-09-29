from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CONTENT_DIR = settings.BASE_DIR / 'content'
DEBUG = True
ALLOWED_HOSTS = ['*']


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
EMAIL_FILE_PATH = CONTENT_DIR, 'tmp/emails'
EMAIL_HOST_USER = 'test@example.com'
DEFAULT_FROM_EMAIL = 'test@example.com'


# -------------------------------------------------------------------
# configuración para el uso de app 'usuarios'
# -------------------------------------------------------------------
ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'usuarios:log_in'
USE_REMEMBER_ME = True
RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True
SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']


# -------------------------------------------------------------------
# configuración para debug
# -------------------------------------------------------------------
if DEBUG:
    settings.INSTALLED_APPS += ['debug_toolbar',]
    settings.MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}


# -------------------------------------------------------------------
# aplicaciones del proyecto
# -------------------------------------------------------------------
settings.INSTALLED_APPS += [
    'core.comunes',
    'core.usuarios',

    # 'apps.personas',
]