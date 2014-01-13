# settings/local.py

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)


## Configuracion del debug_toolbar
INTERNAL_IPS = ("127.0.0.1", "172.16.0.3",)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

## Aqui las configuraciones del cache para el servidor interno y/o usando AWS
