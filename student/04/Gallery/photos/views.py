from pathlib import Path
from django.views.generic import TemplateView
from django.http import Http404


def photo_list():
    def photo_details(i, f):
        caption = f'Caption for Photo {i}' if i == 1 else None
        return dict(id=i, file=f, caption=caption)

    # Ensure the directory exists and is not empty
    image_dir = Path('static/images')
    if not image_dir.exists() or not any(image_dir.iterdir()):
        return []  # Return an empty list if no images are found

    photos = image_dir.iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()

        # Handle invalid id
        if i < 0 or i >= len(photos):
            raise Http404("Photo not found")

        p = photos[i]
        return dict(photo=p)