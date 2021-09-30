from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CONTENT_DIR = settings.BASE_DIR / 'content'
DEBUG = True
ALLOWED_HOSTS = []


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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


# # -------------------------------------------------------------------
# # configuración para el uso de app 'usuarios'
# # -------------------------------------------------------------------
# ENABLE_USER_ACTIVATION = True
# DISABLE_USERNAME = False
# LOGIN_VIA_EMAIL = False
# LOGIN_VIA_EMAIL_OR_USERNAME = True
# LOGIN_REDIRECT_URL = 'home'
# LOGIN_URL = 'usuarios:log_in'
# USE_REMEMBER_ME = False
# RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
# EMAIL_ACTIVATION_AFTER_CHANGING = True


# -------------------------------------------------------------------
# tiempo de sesión
# -------------------------------------------------------------------
SESSION_COOKIE_AGE = 3600  # tiempo de vida de la sesión (10 minutos)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # cerrar sesión al cerrar navegador


# -------------------------------------------------------------------
# aplicaciones del proyecto
# -------------------------------------------------------------------
settings.INSTALLED_APPS += [
    'core.comunes',
    'core.usuarios',
]
