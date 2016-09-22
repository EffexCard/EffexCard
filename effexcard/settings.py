# -*- encoding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lw#+liz$4)dt$+6bq7#0#a7h4v0gzg0vxp^brjz5+284kh+sp#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

# # DEFINICION DE DEPENDENCIAS 
THIRD_PARTY_APPS = (
    'suit',
    'bootstrapform',
    'mathfilters',
    'custom_user',
)
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)


LOCAL_APPS = (
    'webapp',
)

INSTALLED_APPS =  THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.csrf",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'effexcard.urls'

WSGI_APPLICATION = 'effexcard.wsgi.application'

AUTH_USER_MODEL = 'custom_user.EmailUser'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'effexcard',
        'USER': 'root',
        'PASSWORD': 'bolivar',
        'HOST': 'localhost',
        'PORT': '',
    },
}

# # # Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_ID = 3


# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# )

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MAIN_APP = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(MAIN_APP, ".."))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'../media')

TEMPLATE_DIRS = (
os.path.join(os.path.dirname(__file__),'../templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',  
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#configuracion para el captcha
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FONT_SIZE = 70
CAPTCHA_LETTER_ROTATION = (-20,20)
CAPTCHA_OUTPUT_FORMAT = '<p align="center">%(image)s</p> %(hidden_field)s %(text_field)s'

#configuracion de servidor de correo
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'donotreply@effexcard.com'
EMAIL_HOST_PASSWORD = 'fXcd0n0tr3ply'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'EffexCard <donotreply@effexcard.com>'
SERVER_EMAIL = EMAIL_HOST_USER

LOGIN_REDIRECT_URL = "/"

# # Redirect when login is not correct.
LOGIN_URL = '/login'

# #CONFIGURACION DEL DJANGO SUIT
# # Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'EffexCard',
    'HEADER_DATE_FORMAT': 'l, j F Y',
    'HEADER_TIME_FORMAT': 'H:i a',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
       'feedme': ' icon-shopping-cart',
    },
}
