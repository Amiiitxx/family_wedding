"""WSGI config for family_wedding project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'family_wedding.settings')
application = get_wsgi_application()
