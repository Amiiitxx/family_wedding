"""Django admin configuration for Family Wedding Centre."""

from django.contrib import admin
from django.utils.html import format_html
from .models import Store, Brand, Collection, GalleryImage, Enquiry


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'address', 'phone', 'email']
    ordering = ['name']
    list_editable = ['is_active']

    fieldsets = (
        ('Store Information', {
            'fields': (
                'name',
                'address',
                'phone',
                'email',
            )
        }),
        ('Online & Media', {
            'fields': (
                'google_maps_url',
                'instagram_url',
                'image',
            )
        }),
        ('Status', {
            'fields': (
                'is_active',
            )
        }),
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'logo_preview',
        'website_url',
        'display_order',
        'is_active'
    ]
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['display_order', 'name']
    list_editable = ['display_order', 'is_active']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="60" height="40" '
                'style="object-fit:contain;" />',
                obj.logo.url
            )
        return '—'

    logo_preview.short_description = 'Logo'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'display_order',
        'is_active'
    ]
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    ordering = ['display_order', 'name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['display_order', 'is_active']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image_preview',
        'category',
        'display_order',
        'is_active'
    ]
    list_filter = ['is_active', 'category']
    search_fields = ['title']
    ordering = ['display_order', '-id']
    list_editable = ['display_order', 'is_active']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" '
                'style="object-fit:cover;border-radius:4px;" />',
                obj.image.url
            )
        return '—'

    image_preview.short_description = 'Preview'


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'email',
        'created_at',
        'is_contacted'
    ]
    list_filter = ['is_contacted', 'created_at']
    search_fields = [
        'name',
        'phone',
        'email',
        'message'
    ]
    ordering = ['-created_at']
    list_editable = ['is_contacted']
    readonly_fields = [
        'name',
        'phone',
        'email',
        'message',
        'created_at'
    ]

    def has_add_permission(self, request):
        return False  # Enquiries come from the form only


# Customize admin site header
admin.site.site_header = 'Family Wedding Centre Admin'
admin.site.site_title = 'FWC Admin'
admin.site.index_title = 'Site Administration'