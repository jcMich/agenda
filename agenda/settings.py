
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '000qqn+@2@-b+gvu0$96j4j6+$dgf9smoj80g#r)r!0n_%ezvq'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',
    'apps.registros',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "apps.context_processors.my_processors",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'agenda.urls'

WSGI_APPLICATION = 'agenda.wsgi.application'

AUTH_PROFILE_MODULE = 'home.userProfile'  #imagnees de perfil de usuarios

import pymysql
pymysql.install_as_MySQLdb()
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'agenda.db',
            'USER': '',
            'PASSWORD':'',
            'HOST': '',
            'PORT':''
        }
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

STATICFILES_DIRS =(
    os.path.join(BASE_DIR, 'static'),
)

#CONFIGURANDO SERVIDOR DE CORREO(GMAIL)
EMAIL_HOST =  'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'correo@gmail.com'
EMAIL_HOST_PASSWORD = '*******'
EMAIL_USE_TLS = True


