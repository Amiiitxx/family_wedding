"""
Django models for Family Wedding Centre core app.
"""

from django.db import models
from django.utils.text import slugify


class Store(models.Model):
    """Physical retail store locations."""

    name = models.CharField(max_length=200)

    address = models.TextField()

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30
    )

    google_maps_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Google Maps URL"
    )

    instagram_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Instagram URL"
    )

    image = models.ImageField(
        upload_to="stores/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Fashion brands carried by the stores."""

    name = models.CharField(
        max_length=200
    )

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True
    )

    website_url = models.URLField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Product collections / categories."""

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="collections/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    """Gallery / lookbook images."""

    CATEGORY_CHOICES = [
        ("bridal", "Bridal"),
        ("groom", "Groom"),
        ("couple", "Couple"),
        ("family", "Family"),
        ("jewellery", "Jewellery"),
        ("fashion", "Wedding Fashion"),
    ]

    title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="fashion"
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "-id"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title


class Enquiry(models.Model):
    """Customer enquiry / contact form submissions."""

    name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_contacted = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return (
            f"{self.name} — "
            f"{self.phone} "
            f"({self.created_at.strftime('%d %b %Y')})"
        )