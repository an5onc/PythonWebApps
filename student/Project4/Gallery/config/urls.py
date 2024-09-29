from django.urls import path    # Import the path function
from photos.views import PhotolistView, PhotoView # Import the views

urlpatterns = [
    path('', PhotolistView.as_view(), name='photo_list'),  # Display the list of photos
    path('photo/<str:name>/', PhotoView.as_view(), name='photo_detail'),  # Display a specific photo by name
]