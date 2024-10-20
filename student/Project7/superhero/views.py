from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero
from .forms import SuperheroForm  # Import your form here

# List all heroes
class HeroListView(ListView):
    model = Superhero
    template_name = 'list.html'
    context_object_name = 'heroes'

# Hero details
class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'detail.html'
    context_object_name = 'hero'

# Add a new hero
class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    form_class = SuperheroForm  # Use the form
    template_name = 'add.html'
    success_url = reverse_lazy('hero_list')

# Edit an existing hero
class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    form_class = SuperheroForm  # Use the form
    template_name = 'edit.html'
    success_url = reverse_lazy('hero_list')

# Delete an existing hero
class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'delete.html'
    success_url = reverse_lazy('hero_list')