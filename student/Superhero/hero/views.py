from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Business Card',
            'id': 'Anson Cordeiro',
            'image': '/static/businesscard.jpeg'
        }


class StoreView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My Store',
            'id': 'Interlock Go',
            'image': '/static/interlockgo.jpeg'
        }