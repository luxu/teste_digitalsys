import os
from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = ["http://localhost:9000"]

ROOT_URLCONF = 'emprestimo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'emprestimo.wsgi.application'

# INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv(), default='127.0.0.1')

default_db_url = "sqlite:///" + str(BASE_DIR / "emprestimo.sqlite3")
DATABASES = {
    "default": config("DATABASE_URL", default=default_db_url, cast=db_url)
}

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

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://127.0.0.1:6379/0")

# REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    # )
# }

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

BASE_URL = config("BASE_URL", "0.0.0.0")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJOSER = {
    'PERMISSIONS': {
        'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.AllowAny'],
    },
    "SERIALIZERS": {
        "loan": "api.serializers.LoanListSerializer"
    }
}
