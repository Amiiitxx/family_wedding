"""Sitemap configuration for Family Wedding Centre."""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return [
            'core:home',
            'core:about',
            'core:collections',
            'core:brands',
            'core:stores',
            'core:gallery',
            'core:contact',
        ]

    def location(self, item):
        return reverse(item)
