# Import the Path class from the pathlib module to handle filesystem paths
from pathlib import Path

# Import TemplateView from Django's generic views to create class-based views
from django.views.generic import TemplateView

# Import Http404 exception to handle cases where a requested resource is not found
from django.http import Http404


def photo_list():
    """
    This function retrieves a list of photos from the 'static/images' directory.
    Each photo is represented as a dictionary with an id, file path, and an optional caption.
    """
    
    def photo_details(i, f):
        """
        Helper function to create a dictionary containing photo details.
        
        Args:
            i (int): The index of the photo in the directory.
            f (Path): The Path object representing the photo file.
        
        Returns:
            dict: A dictionary with 'id', 'file', and 'caption' keys.
        """
        # Assign a caption only to the first photo (i == 1); others have no caption
        caption = f'Caption for Photo {i}' if i == 1 else None
        # Return a dictionary with photo details
        return dict(id=i, file=f, caption=caption)

    # Define the path to the images directory within the 'static' folder
    image_dir = Path('static/images')
    
    # Check if the images directory exists and is not empty
    if not image_dir.exists() or not any(image_dir.iterdir()):
        # If the directory doesn't exist or is empty, return an empty list
        return []  # No photos to display

    # Retrieve an iterator of all files in the images directory
    photos = image_dir.iterdir()
    
    # Enumerate over the photos, starting the index at 0
    # For each photo, create a dictionary of its details using photo_details()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    
    # Return the list of photo dictionaries
    return photos


class PhotoListView(TemplateView):
    """
    This view handles displaying a list of photos.
    It uses Django's TemplateView to render the 'photos.html' template.
    """
    
    # Specify the template that this view will render
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        """
        This method is used to pass context data to the template.
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            dict: A dictionary containing context data for the template.
        """
        # Call the base implementation to get a context dictionary
        context = super().get_context_data(**kwargs)
        
        # Add a 'photos' key to the context, containing the list of photos
        context['photos'] = photo_list()
        
        # Return the updated context
        return context


class PhotoDetailView(TemplateView):
    """
    This view handles displaying the details of a single photo.
    It uses Django's TemplateView to render the 'photo.html' template.
    """
    
    # Specify the template that this view will render
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        """
        This method is used to pass context data to the template.
        
        Args:
            **kwargs: Arbitrary keyword arguments, including URL parameters.
        
        Returns:
            dict: A dictionary containing context data for the template.
        
        Raises:
            Http404: If the requested photo ID is invalid.
        """
        # Extract the 'id' parameter from the URL keyword arguments
        i = kwargs['id']
        
        # Retrieve the list of photos
        photos = photo_list()

        # Check if the provided id is out of range
        if i < 0 or i >= len(photos):
            # If the id is invalid, raise a 404 error to indicate the photo was not found
            raise Http404("Photo not found")

        # Retrieve the photo dictionary corresponding to the provided id
        p = photos[i]
        
        # Call the base implementation to get a context dictionary
        context = super().get_context_data(**kwargs)
        
        # Add a 'photo' key to the context, containing the specific photo's details
        context['photo'] = p
        
        # Return the updated context
        return context