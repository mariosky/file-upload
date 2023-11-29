"""
Django settings for imageservice project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
#import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# env = environ.Env()
# APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")
# FILE_UPLOAD_STORAGE = env("FILE_UPLOAD_STORAGE", default="local")  # local | s3

# if FILE_UPLOAD_STORAGE == "local":
#     MEDIA_ROOT_NAME = "media"
#     MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
#     MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

# if FILE_UPLOAD_STORAGE == "s3":
#     # Using django-storages
#     # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#     AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
#     AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
#     AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
#     AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
#     AWS_S3_SIGNATURE_VERSION = env("AWS_S3_SIGNATURE_VERSION", default="s3v4")

#     # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
#     AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default="private")

#     AWS_PRESIGNED_EXPIRY = env.int("AWS_PRESIGNED_EXPIRY", default=10)  # seconds




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lmm#(dg9rxa8r6p@w)7qlo$krm(x&3kt$rila%46!h%_*!oz)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ittweb.ddns.net', '54.146.67.173']
CORS_ALLOWED_ORIGINS = ['http://ittweb.ddns.net:8080','http://54.146.67.173:8080']
CSRF_TRUSTED_ORIGINS = [
    "http://ittweb.ddns.net:8080",'http://54.146.67.173:8080'
]
# Application definition

INSTALLED_APPS = [
    'images.apps.ImagesConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imageservice.urls'

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

WSGI_APPLICATION = 'imageservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
