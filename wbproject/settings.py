# Base settings for the WhereBee Django project.
# For development or production settings:
#   from wbproject.settings import *
#   # ... customize settings ...

USE_I18N = True
USE_L10N = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'wbproject.auth.ActiveUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'wbproject.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'wbinventory',
    'wbproject',
)
