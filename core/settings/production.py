from .base import *
import dj_database_url


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'xxx3.onrender.com', '*']
DEBUG = os.getenv('DJANGO_DEBUG')


try:
    from .local import *
except ImportError:
    pass

print('now in prod env settings')
# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.privateemail.com'  # or 'smtp.privateemail.com' or yahoo 'smtp.mail.yahoo.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER_NAMECHEAP')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD_NAMECHEAP')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DATABASES = {
    'default-style': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtail_tenant',
        'USER': 'aboy',
        'PASSWORD': os.getenv('DATABASE_PSWD_RENDER_INTERNAL'),
        'HOST': os.getenv('DATABASE_HOST_RENDER_PUBLIC'),  # Internal hostname
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'  # Optional for internal DBs
        }
    },

    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL'),
    )
}
