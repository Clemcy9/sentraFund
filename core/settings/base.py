
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# load env variable
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth',

    # allauth required apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',

    # django docs with spectacular
    'drf_spectacular',

    # drf
    'rest_framework',
    'rest_framework.authtoken',

    # normal apps
    'phonenumber_field',
    'user_management',
    'investment',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DEBUG = bool(os.getenv('DJANGO_DEBUG'))
print(f'debug = {DEBUG} type: {type(DEBUG)}')
print('now in base.py')
   

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = "/static/"

# Folder where collectstatic will collect files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage"
    },
    
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# default auth setup
AUTH_USER_MODEL = 'user_management.User'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# allauth setup
SITE_ID =1

AUTHENTICATION_BACKENDS =(
    'django.contrib.auth.backends.ModelBackend',
    'user_management.authentications.PhoneNumberBackend', #for custom login with phone_number
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'username_email' #username, email, username_email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USER_MODEL_USERNAME_FIELD =None
ACCOUNT_EMAIL_VERIFICATION = 'none' #optional, none or mandatory
ACCOUNT_UNIQUE_EMAIL = True

BASE_URL = os.getenv("BASE_URL")
EMAIL_CONFIRM_REDIRECT_URL = f"{BASE_URL}/email/confirm/"
PASSWORD_RESET_CONFIRM_REDIRECT_URL = F"{BASE_URL}/password-reset/confirm/"
PASSWORD_RESET_CONFIRM_URL = "password/reset/confirm/{uid}/{token}/"

ACCOUNT_FORMS = {
    'login': 'user_management.forms.CustomLoginForm',
    # 'signup':'user_management.forms.CustomSignupForm',
}
# SOCIALACCOUNT_ADAPTER = 'myapp.adapters.CustomSocialAccountAdapter'
ACCOUNT_ADAPTER = 'user_management.adapter.CustomAccountAdapter'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        # 'APP': {
        #     'client_id': os.getenv('GOOGLE_CLIENT_ID'),
        #     'secret': os.getenv('GOOGLE_SECRET'),
        #     'key': ''
        # },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    
    }
}

LOGIN_REDIRECT_URL = '/dashboard/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# drf spectatual config
SPECTACULAR_SETTINGS = {
    'TITLE': 'Auth API',
    'DESCRIPTION': 'API for user registration and authentication using dj-rest-auth and django-allauth',
    'VERSION': '1.0.0',
    # 'SERVE_INCLUDE_SCHEMA': False,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# contains settings for rest_auth
REST_AUTH = {
    'REGISTER_SERIALIZER': 'user_management.serializers.CustomRegistrationSerializer',
    
}


# CORS CONFIG

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True