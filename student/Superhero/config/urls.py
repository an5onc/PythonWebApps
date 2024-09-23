from django.urls import path
from hero.views import HeroListView, HeroDetailView

urlpatterns = [
    # URL for the home page that displays the list of heroes
    path('', HeroListView.as_view(), name='hero-list'),

    # URL for individual hero profile pages, e.g., /hero/hulk/
    path('hero/<str:hero_name>/', HeroDetailView.as_view(), name='hero-detail'),
]
