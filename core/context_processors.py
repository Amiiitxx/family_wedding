"""Context processors — inject global site context into every template."""

from .models import Collection


def site_context(request):
    """Make navigation collections and site info available globally."""
    return {
        'site_phone': '+91 8943 63 63 63',
        'site_phone_raw': '+918943636363',
        'site_email': 'info@familyweddingcentre.com',
        'site_address': 'Family Wedding Centre, Corporate Office, Kunnamangalam, Calicut, Kerala 673571',
        'nav_collections': Collection.objects.filter(is_active=True).order_by('display_order')[:6],
    }
