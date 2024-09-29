from django.views.generic import RedirectView
from django.urls import path
from photos.views import PhotoListView, PhotoView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='photo/')),

    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoView.as_view()),
]
