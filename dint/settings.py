"""
Django settings for dint project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
import datetime
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', config('DINT'), config('WALLET_URL_DINT'), config('BE_URL_DINT')]

# Application definition
INSTALLED_APPS = [
    'chat',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'simple_history',
    'rest_framework_swagger',
    'corsheaders',
    'django_cron',
]

ASGI_APPLICATION = "dint.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'dint.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'api/templates')
        ],
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

WSGI_APPLICATION = 'dint.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int)
    }
}

AUTH_USER_MODEL = "api.User"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'api:login',
    'LOGOUT_URL': 'api:logout',
    'USE_SESSION_AUTH': False,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            "description": "JWT authorization"
        }
    },
}



REST_FRAMEWORK = {
    # inside the Rest framework settings dictionary, add the auth settings
    # Authentication settings
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],

    # Permission settings
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    #'EXCEPTION_HANDLER': 'api.utils.exceptions.custom_exception_handler',
    #'NON_FIELD_ERRORS_KEY': 'error',

    # Parser classes priority-wise for Swagger
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],

    "DATE_INPUT_FORMATS": ["%m/%d/%Y"],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

#USE_TZ = True

TIME12HRSFORMAT = "%I:%M %p"
DATEFORMAT = "%m/%d/%Y"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = "config('DEFAULT_FROM_EMAIL')"
EMAIL_HOST = "config('EMAIL_HOST')"
EMAIL_HOST_USER = "config('EMAIL_HOST_USER')"
EMAIL_HOST_PASSWORD = "config('EMAIL_HOST_PASSWORD')"
EMAIL_PORT = "config('EMAIL_PORT')"
EMAIL_USE_TLS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = False

#CORS Configuration
CORS_ORIGIN_WHITELIST = [
    'https://dint.com',
    'https://fedev.dint.com',
     'https://bepro.dint.com',
    'https://wallet.dint.com',
     'https://bedev.dint.com',
    'https://node.dint.com',
   'http://localhost:3000',
]


CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = config('AWS_SECRET_KEY')
AWS1_BUCKET_NAME = config('AWS1_BUCKET_NAME')
STRIPE_API_KEY = config('STRIPE_API_KEY')
ENCRYPTION_KEY = config('ENCRYPTION_KEY')

WISE_URL = config('WISE_URL')
WISE_TOKEN = config('WISE_TOKEN')
WISE_PROFILE_ID = config('WISE_PROFILE_ID')



OWNER_PRIVATE_KEY = config('OWNER_PRIVATE_KEY')
NODE_URL = config('NODE_URL')
DINT_TOKEN_DISTRIBUTOR_ADDRESS = config('DINT_TOKEN_DISTRIBUTOR_ADDRESS')
DINT_TOKEN_ADDRESS = config('DINT_TOKEN_ADDRESS')

NODE_API_KEY = config('NODE_API_KEY')
SEND_DINT_TOKEN_URL = config('SEND_DINT_TOKEN_URL')
WITHDRAW_DINT_TOKEN_URL = config('WITHDRAW_DINT_TOKEN_URL')
ID_ANALYZER_KEY = config('ID_ANALYZER_KEY')
SENDINBLUE_API = config('SENDINBLUE_API')

CRON_CLASSES = [
    "api.cron.MyCronJob",
]