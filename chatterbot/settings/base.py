"""

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path

from environ import Env

env = Env()

BASE_DIR = Path(__file__).parents[1]
PROJECT_DIR = BASE_DIR.parent

if (dot_env := PROJECT_DIR.joinpath('.env')).exists():
    env.read_env(f'{dot_env}')

BUILD_VERSION = env('BUILD_VERSION')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='2e6f9b0d5885b6010f9167787445617f553a735f')
API_SECRET_KEY = env('API_SECRET_KEY', default='7cc89434-9d6b-404a-b026-1caf422ff316')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='*')

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'chatterbot.api',
    'rest_framework',
    'storages',
    'drf_yasg',
    'corsheaders',
    'chatterbot.ext.django_chatterbot',
]

PAGE_SIZE = 100
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'chatterbot.base.api_pagination.LimitOffsetPaginationMixin',
    'PAGE_SIZE': PAGE_SIZE,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'chatterbot.base.authentication.TokenAPIAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'chatterbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chatterbot.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_TEST = env('DATABASE_TEST', default='chatterbot_test')
DATABASE_USER = env('DATABASE_USER', default='chatterbot_user')
DATABASE_PASSWORD = env('DATABASE_PASSWORD', default='password')
DATABASE_HOST = env('DATABASE_HOST', default='localhost')
DATABASE_PORT = env.int('DATABASE_PORT', default=5433)
DATABASE_NAME = env('DATABASE_NAME', default='chatterbot')
DATABASE_SCHEMA = env('DATABASE_SCHEMA', default='chatterbot')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': f'-c search_path={DATABASE_SCHEMA}'},
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'TEST': {
            'NAME': DATABASE_TEST,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = env('TIME_ZONE', default='America/Sao_Paulo')
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/api/v1/media/'
MEDIA_ROOT = PROJECT_DIR.joinpath('media').absolute()  # Absolute filesystem path to the directory that will hold
# user-uploaded files. # Example:
# "/home/media/media.lawrence.com/media/"

STATIC_ROOT = PROJECT_DIR.joinpath('static-collected').absolute()
# Absolute path to the directory where static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS. # Example:
# "/home/media/media.lawrence.com/static/"

# CELERY CONFIG
REDIS_HOST = env('REDIS_HOST', default='localhost')
REDIS_PORT = env.int('REDIS_PORT', default=6379)
REDIS_HOST_CELERY_BACKEND_DB = env.int('REDIS_HOST_CELERY_BACKEND_DB', default=0)
REDIS_HOST_CACHE_BACKEND_DB = env.int('REDIS_HOST_CACHE_BACKEND_DB', default=2)

# RABBIT_USER = env('RABBIT_USER', default='guest')
# RABBIT_PASS = env('RABBIT_PASS', default='guest')
# RABBIT_HOST = env('RABBIT_HOST', default='localhost')
# RABBIT_NODE_PORT = env.int('RABBIT_NODE_PORT', default=5673)
# RABBIT_VIRTUAL_HOST = env('RABBIT_VIRTUAL_HOST', default='')

ELASTICSEARCH_HOST = env('ELASTICSEARCH_HOST', default='localhost')
ELASTICSEARCH_PORT = env.int('ELASTICSEARCH_PORT', default=9200)
ELASTICSEARCH_ENVIRONMENT = env('ELASTICSEARCH_ENVIRONMENT', default='dev')
ELASTICSEARCH_USE_SSL = env.bool('ELASTICSEARCH_USE_SSL', default=False)
ELASTICSEARCH_USE_SSL = (
    bool(int(ELASTICSEARCH_USE_SSL))
    if (type(ELASTICSEARCH_USE_SSL) == str) and (len(str(ELASTICSEARCH_USE_SSL)) > 0)
    else ELASTICSEARCH_USE_SSL
)

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_HOST_CACHE_BACKEND_DB}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

# Logging settings.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '\n%(asctime)s [%(levelname)s] [%(name)s:%(module)s:%(funcName)s:%(lineno)s] \n%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {'format': '%(levelname)s %(message)s'},
    },
    'handlers': {
        'renda_fixa': {
            'level': 'INFO',
            'class': 'cmreslogging.handlers.CMRESHandler',
            'hosts': [{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}],
            'es_index_name': 'logs-chatterbot',
            'es_doc_type': None,
            'es_additional_fields': {'App': 'Chatterbot', 'Environment': ELASTICSEARCH_ENVIRONMENT},
            'use_ssl': ELASTICSEARCH_USE_SSL,
            'buffer_size': 3000,
            'flush_frequency_in_sec': 5,
        },
        'console': {'class': 'logging.StreamHandler', 'formatter': 'verbose'},
    },
    'loggers': {
        'django.request': {'handlers': ['renda_fixa', 'console'], 'level': 'ERROR', 'propagate': False},
        'renda_fixa': {
            'handlers': ['renda_fixa', 'console'],
            'formatter': 'verbose',
            'level': 'INFO',
            'propagate': False,
        },
    },
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,

    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'},
    },
    'DEFAULT_AUTO_SCHEMA_CLASS': 'chatterbot.base.CustomAutoSchema',
    'DEFAULT_GENERATOR_CLASS': 'chatterbot.base.CustomSchemaGenerator',
}

REDOC_SETTINGS = {'LAZY_RENDERING': True}

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOWED_ORIGIN_REGEXES = (r'^(https?:\/\/)?([\w-]+\.)?local.com.br$',)
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'authorization_system',
    'encryption_key',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-orama-platform',
    'x-api-key',
    'Authorization',
    'AuthorizationService',
    'access-control-allow-origin',
    'refreshtoken',
)
CORS_ORIGIN_ALLOW_ALL = True

USE_S3 = True
AWS_S3_SECURE_BUCKET = 'zurawskiarquivos'
AWS_S3_ENVIRONMENT = ''
AWS_S3_ACCESS_KEY_ID = 'AKIAWXVR3B6GXNXP3SX2'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_DEFAULT_ACL = None

CHATTERBOT = {
    'name': 'Tech Support Bot',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
}
