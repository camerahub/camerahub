"""
Django settings for photodb project.

Generated by 'django-admin startproject' using Django 2.1.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j257bf@$mm807k1l#$y=9ru9jyk2e_2aply-g6uiw=7bbc2o_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'schema.apps.SchemaConfig',
    'djmoney',
    'favicon',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photodb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'photodb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_DIRS = ('static',)
STATIC_URL = '/static/'

# django-fluent-dashboard
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

FLUENT_DASHBOARD_DEFAULT_ICON = 'icons/unknown.png'
FLUENT_DASHBOARD_DEFAULT_MODULE = 'admin_tools.dashboard.modules.AppList'

FLUENT_DASHBOARD_APP_ICONS = {
  'schema/manufacturer': 'icons/manufacturer.png',
  'schema/accessorytype': 'icons/accessorytype.png',
  'schema/accessory': 'icons/accessory.png',
  'schema/archive': 'icons/archive.png',
  'schema/battery': 'icons/battery.png',
  'schema/condition': 'icons/condition.png',
  'schema/exposureprogram': 'icons/exposureprogram.png',
  'schema/flashprotocol': 'icons/flashprotocol.png',
  'schema/filter': 'icons/filter.png',
  'schema/negativesize': 'icons/negativesize.png',
  'schema/format': 'icons/format.png',
  'schema/series': 'icons/series.png',
  'schema/flash': 'icons/flash.png',
  'schema/enlarger': 'icons/enlarger.png',
  'schema/meteringmode': 'icons/meteringmode.png',
  'schema/meteringtype': 'icons/meteringtype.png',
  'schema/mount': 'icons/mount.png',
  'schema/lightmeter': 'icons/lightmeter.png',
  'schema/paperstock': 'icons/paperstock.png',
  'schema/person': 'icons/person.png',
  'schema/process': 'icons/process.png',
  'schema/teleconverter': 'icons/teleconverter.png',
  'schema/toner': 'icons/toner.png',
  'schema/filmstock': 'icons/filmstock.png',
  'schema/projector': 'icons/projector.png',
  'schema/bulkfilm': 'icons/bulkfilm.png',
  'schema/filteradapter': 'icons/filteradapter.png',
  'schema/shutterspeed': 'icons/shutterspeed.png',
  'schema/developer': 'icons/developer.png',
  'schema/lensmodel': 'icons/lensmodel.png',
  'schema/cameramodel': 'icons/cameramodel.png',
  'schema/lens': 'icons/lens.png',
  'schema/camera': 'icons/camera.png',
  'schema/film': 'icons/film.png',
  'schema/negative': 'icons/negative.png',
  'schema/print': 'icons/print.png',
  'schema/movie': 'icons/movie.png',
  'schema/repair': 'icons/repair.png',
  'schema/scan': 'icons/scan.png',
  'schema/order': 'icons/order.png',
}

from django.utils.translation import ugettext_lazy as _
FLUENT_DASHBOARD_APP_GROUPS = (
    (_('Administration'), {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            'google_analytics.*',
            'registration.*',
        ),
    }),
    (_('Quick links'), {
        'models': (
            'schema.models.Camera',
            'schema.models.Lens',
            'schema.models.Film',
            'schema.models.Negative',
            'schema.models.Print',
        ),
        'module': 'AppIconList',
        'collapsible': True,
    }),
    (_('Applications'), {
        'models': (
            'schema.*',
        ),
        'module': 'ModelList',
        'collapsible': True,
    }),
)

FAVICON_PATH = STATIC_URL + 'favicon.ico'