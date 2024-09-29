# Import RedirectView from Django's generic views to handle URL redirection
from django.views.generic import RedirectView

# Import the path function to define URL patterns
from django.urls import path

# Import the views that will handle the URLs
from photos.views import PhotoDetailView, PhotoListView

# Define the list of URL patterns for the application
urlpatterns = [

    # Home URL pattern
    # When the user visits the root URL (''), redirect them to the 'photo/' URL
    path('', RedirectView.as_view(url='photo/'), name='home'),

    # Photos List URL pattern
    # Maps the 'photo/' URL to the PhotoListView, which displays the list of photos
    path('photo/', PhotoListView.as_view(), name='photo-list'),

    # Photo Detail URL pattern
    # Maps URLs like 'photo/1', 'photo/2', etc., to the PhotoDetailView
    # The <int:id> part captures an integer from the URL and passes it as the 'id' parameter to the view
    path('photo/<int:id>/', PhotoDetailView.as_view(), name='photo-detail'),

    # Gallery URL pattern
    # Maps the 'gallery/' URL to the same PhotoListView
    # This provides an alternative URL to access the photo list
    path('gallery/', PhotoListView.as_view(), name='gallery'),
]