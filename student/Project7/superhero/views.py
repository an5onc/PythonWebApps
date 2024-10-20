from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero


class HeroListView(ListView):
    template_name = 'list.html'  # Removed 'templates/' from the path
    model = Superhero
    context_object_name = 'heroes'


class HeroDetailView(DetailView):
    template_name = 'detail.html'  # Removed 'templates/' from the path
    model = Superhero
    context_object_name = 'hero'


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "add.html"  # Removed 'templates/' from the path
    model = Superhero
    fields = '__all__'


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"  # Removed 'templates/' from the path
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'delete.html'  # Removed 'templates/' from the path
    success_url = reverse_lazy('hero_list')