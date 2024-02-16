"""
Django settings for camerahub project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('CAMERAHUB_SECRET_KEY', 'OverrideMe!')

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('CAMERAHUB_PROD') == 'true':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_registration',
    'django.contrib.sites',
    'django_prometheus',
    'iommi',
    'schema',
    'api',
    'ui',
    'djmoney',
    'fullurl',
    'django_filters',
    'watson',
    'taggit',
    'django_social_share',
    'django_countries',
    'bootstrap_datepicker_plus',
    'geoposition',
    'leaflet',
    'rest_framework',
    'drf_generators',
    'dbbackup',
    'health_check',
    'health_check.db',
    'colorfield',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'iommi.live_edit.Middleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'camerahub.middleware.DynamicSiteDomainMiddleware',
    'iommi.sql_trace.Middleware',
    'iommi.profiling.Middleware',
    'iommi.middleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'camerahub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
            #'loaders': [
            #    'django.template.loaders.filesystem.Loader',
            #    'django.template.loaders.app_directories.Loader',
            #],
        },
    },
]

WSGI_APPLICATION = 'camerahub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('CAMERAHUB_DB_ENGINE', 'django_prometheus.db.backends.sqlite3'),
        'NAME': os.getenv('CAMERAHUB_DB_NAME', BASE_DIR / 'db/db.sqlite3'),
        'USER': os.getenv('CAMERAHUB_DB_USER'),
        'PASSWORD': os.getenv('CAMERAHUB_DB_PASS'),
        'HOST': os.getenv('CAMERAHUB_DB_HOST'),
        'PORT': os.getenv('CAMERAHUB_DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

DATE_INPUT_FORMATS = ['%Y-%m-%d', ]
DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M']
TIME_INPUT_FORMATS = ['%H:%M:%S', '%H:%M', ]

DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'Y-m-d H:i'
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Where to put static files when they are collected
STATIC_ROOT = BASE_DIR / 'static'

# Where to serve static files from
STATIC_URL = 'static/'

# Where to store uploaded assets
MEDIA_ROOT = BASE_DIR / 'media'

# Where to serve uploaded assets from
MEDIA_URL = '/media/'

# Add media to the list of static dirs
STATICFILES_DIRS = [
    BASE_DIR / 'media'
]

LOGIN_REDIRECT_URL = 'schema:index'
LOGOUT_REDIRECT_URL = 'schema:index'

# Email support
DEFAULT_FROM_EMAIL = os.getenv('CAMERAHUB_FROM_EMAIL', "noreply@camerahub.info")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_BACKEND = os.getenv('CAMERAHUB_EMAIL_BACKEND', 'django.core.mail.backends.filebased.EmailBackend')

if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    EMAIL_USE_TLS = os.getenv('CAMERAHUB_EMAIL_USE_TLS')
    EMAIL_USE_SSL = os.getenv('CAMERAHUB_EMAIL_USE_SSL')
    EMAIL_HOST = os.getenv('CAMERAHUB_EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('CAMERAHUB_EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('CAMERAHUB_EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('CAMERAHUB_EMAIL_PORT')
elif EMAIL_BACKEND == 'django.core.mail.backends.filebased.EmailBackend':
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
REGISTRATION_OPEN = True  # allow sign-ups

# Required for django.contrib.sites
DEFAULT_SITE_ID = 1
SITE_ID = 1

#AUTH_USER_MODEL = 'schema.User'

# Emit logs of WARNING and above to stderr
# for both production and debug mode
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console2': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console2'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
        },
    },
}

TAGGIT_CASE_INSENSITIVE = True

# Use OpenStreetMap instead of Google for form widget
GEOPOSITION_BACKEND = 'leaflet'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, "backup")}
DBBACKUP_CONNECTORS = {
    'default': {
        'USER': os.getenv('CAMERAHUB_DB_USER'),
        'PASSWORD': os.getenv('CAMERAHUB_DB_PASS'),
        'HOST': os.getenv('CAMERAHUB_DB_HOST'),
        'CONNECTOR': 'dbbackup.db.postgresql.PgDumpBinaryConnector',
    }
}

# drf-generators
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25
}

# status URL
STATUS_URL = os.getenv('CAMERAHUB_STATUS_URL')

# django-settings-export
# These settings are exposed to template context
SETTINGS_EXPORT = [
    'STATUS_URL',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


GEOPOSITION_GOOGLE_MAPS_API_KEY = ''

# These imports need to be at the bottom of the file!
from iommi import Style, Asset
from iommi.style_bootstrap import bootstrap

IOMMI_DEFAULT_STYLE = Style(
    bootstrap,
    base_template='iommi_base.html',
#    root__assets=dict(
#        my_project_custom_css=Asset.css(attrs__href='/static/custom.css'),
#        my_project_custom_js=Asset.js(attrs__src='/static/custom.js'),
#    ),
)
