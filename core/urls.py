"""URL configuration for core app."""

from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    path('our-story/', views.OurStoryView.as_view(), name='our_story'),

    path('collections/', views.CollectionsView.as_view(), name='collections'),

    path('brands/', views.BrandsView.as_view(), name='brands'),

    path('stores/', views.StoresView.as_view(), name='stores'),

    path('gallery/', views.GalleryView.as_view(), name='gallery'),

    path('contact/', views.contact_view, name='contact'),

    path('robots.txt', views.robots_txt, name='robots_txt'),

]