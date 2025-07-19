from .base import *
from dotenv import load_dotenv
import dj_database_url

load_dotenv()
DEBUG = os.getenv('DJANGO_DEBUG')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER_LOCAL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD_LOCAL')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


print('now in dev env settings')

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    # 'default': dj_database_url.config(default=os.getenv('DATABASE_LOCAL')) #this default to "DATABASE_URL" even when u explicitly choose otherwise, only works if url doesn't exist
    'default_render': dj_database_url.parse(os.getenv('DATABASE_EXTERNAL_RENDER')),
    'default': dj_database_url.parse(os.getenv('DATABASE_LOCAL')),
}