"""Views for Family Wedding Centre core app."""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .models import Store, Brand, Collection, GalleryImage
from .forms import EnquiryForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['collections'] = (
            Collection.objects
            .filter(is_active=True)
            .order_by('display_order')[:6]
        )

        context['stores'] = Store.objects.filter(is_active=True)

        context['brands'] = (
            Brand.objects
            .filter(is_active=True)
            .order_by('display_order')[:10]
        )

        context['gallery_images'] = (
            GalleryImage.objects
            .filter(is_active=True)[:8]
        )

        context['enquiry_form'] = EnquiryForm()

        context['page_title'] = (
            'Family Wedding Centre | Kerala\'s Premier Wedding Fashion Destination'
        )

        context['meta_description'] = (
            'Family Wedding Centre — Kerala\'s ultimate wedding destination. '
            'Bridal wear, groom wear, family collections and premium fashion brands '
            'across 7 stores in Calicut, Vadakara, Manjeri, Meppadi, Tirur, '
            'Perinthalmanna and Kannur.'
        )

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stores_count'] = (
            Store.objects
            .filter(is_active=True)
            .count()
        )

        context['brands'] = (
            Brand.objects
            .filter(is_active=True)
            .order_by('display_order')
        )

        context['page_title'] = (
            'About Us | Family Wedding Centre Kerala'
        )

        context['meta_description'] = (
            'Learn about Family Wedding Centre — Kerala\'s premier wedding '
            'fashion retail brand. Over 10 retail outlets, 2 million happy '
            'customers, and the finest collections from India and abroad.'
        )

        return context


# ============================================================
# OUR STORY
# ============================================================

class OurStoryView(TemplateView):
    template_name = 'our-story.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_title'] = (
            'Our Story | Family Wedding Centre'
        )

        context['meta_description'] = (
            'Discover the story behind Family Wedding Centre — '
            'where every celebration becomes a family story.'
        )

        return context


class CollectionsView(TemplateView):
    template_name = 'collections.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['collections'] = (
            Collection.objects
            .filter(is_active=True)
            .order_by('display_order')
        )

        context['page_title'] = (
            'Wedding Collections | Family Wedding Centre'
        )

        context['meta_description'] = (
            'Explore our stunning wedding collections — Bridal Wear, Groom Wear, '
            'Family Wear, Jewellery and Premium fashion at Family Wedding Centre Kerala.'
        )

        return context


class BrandsView(TemplateView):
    template_name = 'brands.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['brands'] = (
            Brand.objects
            .filter(is_active=True)
            .order_by('display_order')
        )

        context['page_title'] = (
            'Our Brands | Family Wedding Centre'
        )

        context['meta_description'] = (
            'Discover top fashion brands at Family Wedding Centre — '
            'US Polo Assn., Allen Solly, Louis Philippe, Blackberrys, '
            'Indian Terrain and many more.'
        )

        return context


class StoresView(TemplateView):
    template_name = 'stores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stores'] = (
            Store.objects
            .filter(is_active=True)
        )

        context['page_title'] = (
            'Our Stores | Family Wedding Centre'
        )

        context['meta_description'] = (
            'Visit Family Wedding Centre showrooms across Kerala — '
            'Kunnamangalam, Vadakara, Manjeri, Meppadi, Tirur, '
            'Perinthalmanna and Kannur.'
        )

        return context


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.request.GET.get('category', '')

        qs = GalleryImage.objects.filter(is_active=True)

        if category:
            qs = qs.filter(category=category)

        context['images'] = (
            qs.order_by('display_order')
        )

        context['active_category'] = category

        context['categories'] = (
            GalleryImage.CATEGORY_CHOICES
        )

        context['page_title'] = (
            'Gallery | Family Wedding Centre'
        )

        context['meta_description'] = (
            'Browse our wedding fashion gallery — bridal wear, groom attire, '
            'couple outfits, family wear and jewellery at Family Wedding Centre.'
        )

        return context


@require_http_methods(['GET', 'POST'])
def contact_view(request):
    """Contact / enquiry page with form handling."""

    form = EnquiryForm()
    success = False

    if request.method == 'POST':

        form = EnquiryForm(request.POST)

        if form.is_valid():

            form.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! We will contact you shortly.'
                })

            success = True
            form = EnquiryForm()

        else:

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':

                errors = {
                    field: list(errs)
                    for field, errs in form.errors.items()
                }

                return JsonResponse(
                    {
                        'success': False,
                        'errors': errors
                    },
                    status=400
                )

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'success': success,
            'page_title': 'Contact Us | Family Wedding Centre',
            'meta_description': (
                'Get in touch with Family Wedding Centre. Enquire about our '
                'wedding fashion collections, store locations and more.'
            ),
        }
    )


def robots_txt(request):
    """Serve robots.txt."""

    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n\n"
        "Sitemap: https://familyweddingcentre.com/sitemap.xml\n"
    )

    return HttpResponse(
        content,
        content_type='text/plain'
    )