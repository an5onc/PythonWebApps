from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView
from django.contrib import admin

urlpatterns = [
    # Hero Views
    path('',           HeroListView.as_view(),    name='hero_list'),          # Hero list
    path('<int:pk>/',       HeroDetailView.as_view(),  name='hero_detail'),        # Hero detail
    path('add/',            HeroCreateView.as_view(),  name='hero_add'),           # Add hero
    path('<int:pk>/edit/',  HeroUpdateView.as_view(),  name='hero_edit'),          # Edit hero
    path('<int:pk>/delete/',HeroDeleteView.as_view(),  name='hero_delete'),        # Delete hero

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),

    # Admin views for users
    path('admin/', admin.site.urls),
]
