# config/urls.py

from django.contrib import admin
from django.urls import path, include
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
    path('heroes/', HeroListView.as_view(), name='list'),            # Hero list
    path('heroes/<int:pk>/', HeroDetailView.as_view(), name='detail'),  # Hero detail
    path('heroes/add/', HeroCreateView.as_view(), name='add'),          # Add hero
    path('heroes/<int:pk>/edit/', HeroUpdateView.as_view(), name='edit'),  # Edit hero
    path('heroes/<int:pk>/delete/', HeroDeleteView.as_view(), name='delete'),  # Delete hero

    # User Authentication
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password change, password reset

    # Admin Views
    path('admin/', admin.site.urls),  # Django admin
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)