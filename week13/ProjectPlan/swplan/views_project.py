from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Project


class ProjectView(RedirectView):
    url = reverse_lazy('project_list')


class ProjectListView(ListView):
    template_name = 'project_list.html'
    model = Project


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs.update(dict(dependent=Dependent.obects.filter(project=kwargs.get('object'))))
    #     return kwargs


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "project_add.html"
    model = Project
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "project_edit.html"
    model = Project
    fields = '__all__'


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project_list')