from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView

urlpatterns = [
    # Hero Views
    path('', HeroListView.as_view(), name='hero_list'),          # Hero list
    path('<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),  # Hero detail
    path('add/', HeroCreateView.as_view(), name='hero_add'),         # Add hero
    path('<int:pk>/edit/', HeroUpdateView.as_view(), name='hero_edit'),  # Edit hero
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),  # Delete hero

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),

    # Admin views for users
    path('admin/', admin.site.urls),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)