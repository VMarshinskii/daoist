"""
Django settings for pipoo project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__$mb-5bgvs0k$b2s=l^z4!$nnm*0ne&0g)_c+%9v8^^9pxu&a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'blog',
    'pages',
    'consultations'
    #'redactor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# USER_AGENTS_CACHE = 'default'

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.core.context_processors.auth",
#     'django.contrib.auth.context_processors.auth',
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     'django.core.context_processors.request',
# )

ROOT_URLCONF = 'daoist.urls'

WSGI_APPLICATION = 'daoist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd E Y'

REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'static'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ('static', )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'blog/templates'),
    os.path.join(BASE_DIR,  'pages/templates'),
    os.path.join(BASE_DIR,  'consultations/templates'),
)