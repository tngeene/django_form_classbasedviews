"""
Django settings for custom_user_django_en project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants
from decouple import config
from django.conf.urls.static import static

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
# ---------------------------------------------------------- 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# ----------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a-^cwq-nzm(b-oi%25(2mzwu6k=m8vl*fnkjz(!lv!$5b$_qnh'

# ----------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# ----------------------------------------------------------
# SSL and Cookies
# ----- Production ----- #
if not DEBUG:
	SECURE_SSL_REDIRECT = True
	ADMINS = [(('ADMIN'), ('leticialimacgi@gmail.com'))]
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True


# ----------------------------------------------------------
# Application definition

INSTALLED_APPS = [
	# --- Django Apps --- #
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles', 
	# --- My Apps ---#
	'base',  
	'manuais',
]


# ----------------------------------------------------------
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	# 'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ----------------------------------------------------------
ROOT_URLCONF = 'custom_user_django_en.urls'

# ----------------------------------------------------------
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

# ----------------------------------------------------------
WSGI_APPLICATION = 'custom_user_django_en.wsgi.application'


# ----------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# --- Development SQLite3 --- #
# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.sqlite3',
# 		'NAME': BASE_DIR / 'db.sqlite3',
# 	}
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sistema',
        'PORT': '3306',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',

    }
}


# ----------------------------------------------------------
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# ----------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ----------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[STATIC_DIR,]
MEDIA_ROOT=os.path.join(BASE_DIR,'static')
MEDIA_URL = '/media/' 