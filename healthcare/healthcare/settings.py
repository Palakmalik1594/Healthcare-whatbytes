from pathlib import Path
import environ
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent


# env
env = environ.Env(
DEBUG=(bool, False),
ACCESS_TOKEN_LIFETIME_MINUTES=(int, 60),
REFRESH_TOKEN_LIFETIME_DAYS=(int, 7),
)
# reading .env
environ.Env.read_env(BASE_DIR / '.env')


DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',') if env('ALLOWED_HOSTS') else []


INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',


# Third-party
'rest_framework',


# Local
'core',
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


ROOT_URLCONF = 'healthcare.urls'
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [],
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
WSGI_APPLICATION = 'healthcare.wsgi.application'


# Database
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': env('DB_NAME'),
'USER': env('DB_USER'),
'PASSWORD': env('DB_PASSWORD'),
'HOST': env('DB_HOST'),
'PORT': env('DB_PORT'),
}
}
AUTH_PASSWORD_VALIDATORS = [
{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DRF & JWT
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
),
'DEFAULT_PERMISSION_CLASSES': (
'rest_framework.permissions.AllowAny',
),
}
SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env('ACCESS_TOKEN_LIFETIME_MINUTES')),
'REFRESH_TOKEN_LIFETIME': timedelta(days=env('REFRESH_TOKEN_LIFETIME_DAYS')),
'AUTH_HEADER_TYPES': ('Bearer',),
}