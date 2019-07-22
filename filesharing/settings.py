"""
Django settings for filesharing project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import getpass
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a7$(f%&hfc#4$=j4y5n#%mq!_snb4_5h3%*j@5r6c1$2o_6zua'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENVIRONMENT = 'Dev'

ALLOWED_HOSTS = ["*"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'filetransfer'
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

ROOT_URLCONF = 'filesharing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")], 
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

WSGI_APPLICATION = 'filesharing.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if ENVIRONMENT == "Dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dev_schoolmgt', 
            # 'USER': 'next',
            # 'PASSWORD': 'next',
            # 'HOST': '192.168.11.88',
            'USER': 'next',
            'PASSWORD': 'next',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
elif ENVIRONMENT == "Test":
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test_file_sharing', 
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            # 'PORT': '5432',
        }
    }
elif ENVIRONMENT == "Prod":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'prod_file_sharing', 
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            # 'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters' : {
        'standard' : {
            'format' : '%(asctime)s [%(levelname)s] : %(message)s'
        },
    },
    'handlers': {
        'logit': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'filename': '/var/log/Sharp/logit.log',
            'filename': os.path.join(BASE_DIR +'/logit.log'),
            #'filename': '/logit.log',
            'when': 'midnight',
            'backupCount': 10,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'logit': {
            'handlers': ['logit'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

FILEPATH = 'http://192.168.11:8003/media/file/'

### Media URL path and File Path
if ENVIRONMENT == "Dev":
    MEDIA_ROOT = '/home/users/'+getpass.getuser()+'/.filesharing/uploads/'
elif ENVIRONMENT == "Test":
    MEDIA_ROOT = '/home/'+getpass.getuser()+'/.filesharing/uploads/'
elif ENVIRONMENT == "Prod":
    MEDIA_ROOT = '/home/.filesharing/uploads/'
       
MEDIA_URL = '/media/'

### Status Code
STATUS_KEY = "status"
SUCCESS_STATUS = "Success"
FAILURE_STATUS = "Fail"
UPDATE_STATUS = "Update"
REMOVE_STATUS = "Remove"
ERROR = "Error"
