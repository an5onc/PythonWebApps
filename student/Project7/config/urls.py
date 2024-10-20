# your_project/urls.py

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from superhero.views import (
    HomePageView,
    AboutPageView,
    HeroCreateView,
    HeroDeleteView,
    HeroDetailView,
    HeroListView,
    HeroUpdateView,
)

urlpatterns = [
    # Home and About Views
    path('', HomePageView.as_view(), name='home'),       # Home page
    path('about/', AboutPageView.as_view(), name='about'),  # About page

    # Hero Views
    path('heroes/', HeroListView.as_view(), name='hero_list'),            # Hero list
    path('heroes/<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),  # Hero detail
    path('heroes/add/', HeroCreateView.as_view(), name='hero_add'),          # Add hero
    path('heroes/<int:pk>/edit/', HeroUpdateView.as_view(), name='hero_edit'),  # Edit hero
    path('heroes/<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),  # Delete hero

    # User Authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Admin Views
    path('admin/', admin.site.urls),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)