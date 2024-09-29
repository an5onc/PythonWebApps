from pathlib import Path
from django.views.generic import TemplateView
from django.conf import settings

class PhotoView(TemplateView):  # create a class called PhotoView
    template_name = 'photo.html'  # get the template name

    def get_context_data(self, **kwargs):  # get the name of the photo
        context = super().get_context_data(**kwargs)
        name = kwargs['name']  # get the name of the photo
        image = f'/static/images/{name}'  # construct the URL to the image
        context['photo'] = name  # return the image in the context
        return context


class PhotolistView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use the absolute path to the static directory in the file system
        static_images_path = Path(settings.BASE_DIR) / 'static/images'

        # Check if the directory exists before trying to list files
        if static_images_path.exists():
            photos = [f.name for f in static_images_path.iterdir() if f.is_file()]
        else:
            photos = []

        # Return the list of photo names in the context
        context['photos'] = photos
        return context



