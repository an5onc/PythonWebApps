from django.views.generic import TemplateView

# Dictionary of heroes
heroes = {
    'hulk': {
        'title': 'Hulk',
        'id': 'Bruce Banner',
        'strengths': 'Superhuman strength, invulnerability',
        'weaknesses': 'Uncontrollable rage',
        'image': '/static/hulk.jpeg'
    },
    'superman': {
        'title': 'Superman',
        'id': 'Clark Kent',
        'strengths': 'Super strength, flight, invulnerability, laser vision',
        'weaknesses': 'Kryptonite',
        'image': '/static/superman.jpeg'
    },
    'batman': {
        'title': 'Batman',
        'id': 'Bruce Wayne',
        'strengths': 'Martial arts, genius intellect, detective skills',
        'weaknesses': 'Human limits',
        'image': '/static/batman.jpeg'
    },
    'wonderwoman': {
        'title': 'Wonder Woman',
        'id': 'Diana Prince',
        'strengths': 'Super strength, combat skills, Lasso of Truth',
        'weaknesses': 'None known',
        'image': '/static/wonderwoman.jpeg'
    },
    'store': {
        'title': 'My Store',
        'id': 'Interlock Go',
        'strengths': 'Quick installation, reliability',
        'weaknesses': 'Limited staff',
        'image': '/static/interlockgo.jpeg'
    }
}

# View to display the list of heroes
class HeroListView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heroes'] = heroes
        return context

# View to display an individual hero's profile
class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        hero_name = self.kwargs.get('hero_name')
        hero = heroes.get(hero_name, None)

        if hero:
            return hero
        # Return a default context if hero is not found
        return {
            'title': 'Hero Not Found',
            'id': '',
            'strengths': '',
            'weaknesses': '',
            'image': '/static/default.jpeg'
        }
