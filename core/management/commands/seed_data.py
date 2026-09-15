"""
Management command: seed_data

Populates the database with initial stores, brands, and collections.
Run with: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from core.models import Store, Brand, Collection


STORES = [
    {
        'name': 'Kunnamangalam',
        'address': 'National Highway 766, Wayanad Rd, Kunnamangalam, Calicut, Kerala',
        'phone': '0495 2966263',
        'email': '',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Kunnamangalam+Calicut',
    },
    {
        'name': 'Vadakara',
        'address': 'NH BYPASS Near Malabar Gold, Edodi, Vadakara, Kerala',
        'phone': '0496 2973333',
        'email': 'familyvadakara@gmail.com',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Vadakara',
    },
    {
        'name': 'Manjeri',
        'address': 'Calicut Road, City Point Shopping Mall, Manjeri, Kerala',
        'phone': '0483 2971004',
        'email': 'familymanjeri@gmail.com',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Manjeri',
    },
    {
        'name': 'Meppadi',
        'address': 'Wayanad, Kerala',
        'phone': '0493 6282828',
        'email': 'familymeppady@gmail.com',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Meppadi+Wayanad',
    },
    {
        'name': 'Tirur',
        'address': 'SH 71, Pan Bazaar, Tirur, Kerala',
        'phone': '0494 2956363',
        'email': 'familytirur@gmail.com',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Tirur',
    },
    {
        'name': 'Perinthalmanna',
        'address': 'Calicut Road, Perinthalmanna, Kerala 679322',
        'phone': '04933 223363',
        'email': '',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Perinthalmanna',
    },
    {
        'name': 'Kannur',
        'address': 'Thayatheru Road, Kannur, Kerala 670002',
        'phone': '0497-2976363',
        'email': '',
        'google_maps_url': 'https://maps.google.com/?q=Family+Wedding+Centre+Kannur',
    },
]

BRANDS = [
    {'name': 'U.S. Polo Assn.', 'display_order': 1},
    {'name': 'Indian Terrain', 'display_order': 2},
    {'name': 'Flying Machine', 'display_order': 3},
    {'name': 'Blackberrys', 'display_order': 4},
    {'name': 'Benetton', 'display_order': 5},
    {'name': 'Basics', 'display_order': 6},
    {'name': 'Allen Solly', 'display_order': 7},
    {'name': 'North Republic', 'display_order': 8},
    {'name': 'Louis Philippe', 'display_order': 9},
    {'name': 'fête', 'display_order': 10},
]

COLLECTIONS = [
    {
        'name': 'Bridal Wear',
        'slug': 'bridal-wear',
        'description': 'Exquisite bridal collections for your most special day. From traditional Kerala sarees to contemporary bridal lehengas.',
        'display_order': 1,
    },
    {
        'name': 'Groom Wear',
        'slug': 'groom-wear',
        'description': 'Premium groom attire from classic sherwanis to modern suits, curated for the discerning groom.',
        'display_order': 2,
    },
    {
        'name': 'Family Wear',
        'slug': 'family-wear',
        'description': 'Coordinate your entire family\'s wedding look with our exclusive family wear collections.',
        'display_order': 3,
    },
    {
        'name': 'Jewellery',
        'slug': 'jewellery',
        'description': 'Complete your wedding look with our stunning jewellery collections from leading designers.',
        'display_order': 4,
    },
    {
        'name': 'Premium Wear',
        'slug': 'premium-wear',
        'description': 'Luxury fashion labels and designer collections for those who demand only the finest.',
        'display_order': 5,
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with initial stores, brands and collections data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding.',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Store.objects.all().delete()
            Brand.objects.all().delete()
            Collection.objects.all().delete()

        # Seed stores
        created_stores = 0
        for data in STORES:
            obj, created = Store.objects.get_or_create(name=data['name'], defaults=data)
            if created:
                created_stores += 1
        self.stdout.write(self.style.SUCCESS(f'✓ Stores: {created_stores} created'))

        # Seed brands
        created_brands = 0
        for data in BRANDS:
            obj, created = Brand.objects.get_or_create(name=data['name'], defaults=data)
            if created:
                created_brands += 1
        self.stdout.write(self.style.SUCCESS(f'✓ Brands: {created_brands} created'))

        # Seed collections
        created_collections = 0
        for data in COLLECTIONS:
            obj, created = Collection.objects.get_or_create(slug=data['slug'], defaults=data)
            if created:
                created_collections += 1
        self.stdout.write(self.style.SUCCESS(f'✓ Collections: {created_collections} created'))

        self.stdout.write(self.style.SUCCESS('\n✅ Seed data loaded successfully!'))
        self.stdout.write('   Visit /admin/ to add images to stores, brands and collections.')
