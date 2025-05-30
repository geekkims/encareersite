from pathlib import Path
import os
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6$!g=v&_m9b66&z+xx3k7frh8eo8ee4&6(_!suj07t1tg%l=9&'

# Set DEBUG based on environment - for production set to False
DEBUG = False  # Change to False for production

# ALLOWED_HOSTS for both development and production
ALLOWED_HOSTS = ['careerventures.co.ke', 'www.careerventures.co.ke', '127.0.0.1', 'localhost', '0.0.0.0']

# HTTPS settings - only apply in production (when DEBUG=False)
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'authentication',
    'website',
    'ckeditor',
    'taggit',
    'user_visit',
    'jobapp',
    'blogs',
    # 'debug_toolbar',  # Uncomment for development debugging
    'django.contrib.humanize',
    'contactus'
]

CKEDITOR_UPLOAD_PATH = "uploads/"   

ORDERABLE_MODELS = {
    'auth.User': ('home', 'users'),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_visit.middleware.UserVisitMiddleware', 
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',  # Uncomment for development debugging
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# CKEDITOR custom config
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'tabSpaces': 4,
    }
}

# For debug toolbar (only in development)
INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static files configuration - FIXED for production
# Always include STATICFILES_DIRS so Django can find your static/assets/ folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Production: Use STATIC_ROOT for collected static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Message tags for Bootstrap styling
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Email configuration
EMAIL_HOST = 'mail.techspace.co.ke'
EMAIL_HOST_USER = 'info@techspace.co.ke'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@techspace.co.ke'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'P@$$w0rd.2016'

# Logging configuration (optional but recommended for production)
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'django_errors.log'),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }
