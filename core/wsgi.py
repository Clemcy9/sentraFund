import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()
DEBUG = os.getenv('DJANGO_DEBUG')

if DEBUG:
    # where to switch between dev and prod settings
    print('using dev wsgi')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
else:
    print('using prod wsgi')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

application = get_wsgi_application()
