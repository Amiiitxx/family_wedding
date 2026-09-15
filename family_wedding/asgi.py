"""ASGI config for family_wedding project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'family_wedding.settings')
application = get_asgi_application()
