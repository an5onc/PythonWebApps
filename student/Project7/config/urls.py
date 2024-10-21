# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from superhero.views import (
    HomeView,
    AboutView,
    SuperheroCreateView,
    SuperheroDeleteView,
    SuperheroDetailView,
    SuperheroListView,
    SuperheroUpdateView,
)

urlpatterns = [
    # Home and About Views
    path('', HomeView.as_view(), name='home'),    # Updated to HomeView from views.py
    path('about/', AboutView.as_view(), name='about'),  # Updated to AboutView from views.py

    # Hero Views
    path('heroes/', SuperheroListView.as_view(), name='list'),            # Hero list from views.py
    path('heroes/<int:pk>/', SuperheroDetailView.as_view(), name='detail'),  # Hero detail
    path('heroes/add/', SuperheroCreateView.as_view(), name='add'),          # Add hero
    path('heroes/<int:pk>/edit/', SuperheroUpdateView.as_view(), name='edit'),  # Edit hero
    path('heroes/<int:pk>/delete/', SuperheroDeleteView.as_view(), name='delete'),  # Delete hero

    # User Authentication
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password change, password reset

    # Admin Views
    path('admin/', admin.site.urls),  # Django admin
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)