from photologue import PHOTOLOGUE_APP_DIR


"""
Django settings for aurora_alarm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u$m_8c8k3%&(bs33h@$%9dhk7@codm7wwt0*-ccqo5@tg9h_%)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'frontend',
    'rest_framework',
    'djcelery',
    'kombu.transport.django',
    'social.apps.django_app.default',
    'photologue', 
    'south',
    'tagging',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aurora_alarm.urls'

WSGI_APPLICATION = 'aurora_alarm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'frontend/static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend/static/photologue')

MEDIA_URL = '/static/photologue/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "aurora_alarm.context_processors.pass_global_variables",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    PHOTOLOGUE_APP_DIR,
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10
}

BROKER_URL = "django://"


API_URL = "http://127.0.0.1:8000/api/"

AUTHENTICATION_BACKENDS = (
      'social.backends.google.GoogleOAuth2',
      'social.backends.facebook.FacebookOAuth2',
      'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/complete/google-oauth2/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/'

SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 40
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 40

SOCIAL_AUTH_DEFAULT_USERNAME = 'new-username'
SOCIAL_AUTH_UUID_LENGTH = 16
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = False
SOCIAL_AUTH_CLEAN_USERNAMES = True

SOCIAL_AUTH_SANITIZE_REDIRECTS = False
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_URLOPEN_TIMEOUT = 30

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '782630118731-ctingp9rs9aqalmg78p2m4r3mtm1fs81.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ow9mOSbf03XIAP3MRPnKyK6s'

SOCIAL_AUTH_FACEBOOK_KEY = '427395604059121'
SOCIAL_AUTH_FACEBOOK_SECRET = '3796e1925d7188631dbef9bc88c32c42'

AUTH_PROFILE_MODULE = 'api.UserProfile'
