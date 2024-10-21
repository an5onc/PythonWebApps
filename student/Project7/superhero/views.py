# superhero/views.py

from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Superhero
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'list.html'
    context_object_name = 'superheroes'

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'detail.html'
    context_object_name = 'superhero'

class SuperheroCreateView(CreateView):
    model = Superhero
    template_name = 'add.html'
    fields = '__all__'

class SuperheroUpdateView(UpdateView):
    model = Superhero
    template_name = 'edit.html'
    fields = '__all__'

class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'delete.html'
    success_url = reverse_lazy('list')