
"""
Django settings for Family Wedding Centre project.
Local Development + Vercel Production Configuration.
"""

import os
from pathlib import Path
from decouple import config
from django.core.exceptions import ImproperlyConfigured


# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# SECURITY CONFIGURATION
# =====================================================

SECRET_KEY = config(
    'SECRET_KEY',
    default='django-insecure-local-development-only-key'
)

DEBUG = config(
    'DEBUG',
    default=False,
    cast=bool
)

# Prevent insecure default SECRET_KEY in production
if not DEBUG and SECRET_KEY == 'django-insecure-local-development-only-key':
    raise ImproperlyConfigured(
        'Set a secure SECRET_KEY in production environment variables.'
    )


# Allowed Hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'family-wedding-mall.vercel.app',
    '.vercel.app',
]


# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in config(
        'CSRF_TRUSTED_ORIGINS',
        default='https://family-wedding-mall.vercel.app'
    ).split(',')
    if origin.strip()
]


# =====================================================
# APPLICATION DEFINITION
# =====================================================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # Custom Apps
    'core',
]


# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================================================
# URL CONFIGURATION
# =====================================================

ROOT_URLCONF = 'family_wedding.urls'


# =====================================================
# TEMPLATES CONFIGURATION
# =====================================================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.debug',

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'core.context_processors.site_context',

            ],

        },

    },

]


# =====================================================
# WSGI / ASGI CONFIGURATION
# =====================================================

WSGI_APPLICATION = 'family_wedding.wsgi.application'

ASGI_APPLICATION = 'family_wedding.asgi.application'


# =====================================================
# DATABASE CONFIGURATION - POSTGRESQL
# =====================================================

DB_SSL_REQUIRE = config(
    'DB_SSL_REQUIRE',
    default=False,
    cast=bool
)

DATABASE_OPTIONS = {}

if DB_SSL_REQUIRE:
    DATABASE_OPTIONS['sslmode'] = 'require'


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': config(
            'DB_NAME',
            default='family_wedding_db'
        ),

        'USER': config(
            'DB_USER',
            default='postgres'
        ),

        'PASSWORD': config(
            'DB_PASSWORD',
            default=''
        ),

        'HOST': config(
            'DB_HOST',
            default='localhost'
        ),

        'PORT': config(
            'DB_PORT',
            default='5432'
        ),

        'OPTIONS': DATABASE_OPTIONS,

        # Suitable starting point for serverless deployments
        'CONN_MAX_AGE': 0,

    }

}


# =====================================================
# PASSWORD VALIDATION
# =====================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]


# =====================================================
# INTERNATIONALIZATION
# =====================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# =====================================================
# STATIC FILE CONFIGURATION
# =====================================================

STATIC_URL = config(
    'STATIC_URL',
    default='/static/'
)

STATICFILES_DIRS = [

    BASE_DIR / 'static',

]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# =====================================================
# MEDIA FILE CONFIGURATION
# =====================================================

MEDIA_URL = config(
    'MEDIA_URL',
    default='/media/'
)

MEDIA_ROOT = BASE_DIR / 'media'


# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =====================================================
# PRODUCTION SECURITY SETTINGS
# =====================================================

if not DEBUG:

    # HTTPS Configuration
    SECURE_SSL_REDIRECT = True

    SECURE_PROXY_SSL_HEADER = (
        'HTTP_X_FORWARDED_PROTO',
        'https'
    )

    # Browser Security
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SECURE_BROWSER_XSS_FILTER = True

    X_FRAME_OPTIONS = 'DENY'

    # Secure Cookies
    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

    # HSTS
    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # Prevent MIME type sniffing
    SECURE_CONTENT_TYPE_NOSNIFF = True


# =====================================================
# END OF SETTINGS
# =====================================================
