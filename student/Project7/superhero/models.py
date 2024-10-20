from django.db import models
from django.urls import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default="None", blank=True, null=True)  # Allows for optional descriptions
    image = models.ImageField(upload_to='heroes/', default="default.jpg")  # Image upload path with a default image
    strengths = models.CharField(max_length=200, default="None", blank=True, null=True)  # Optional strengths
    weaknesses = models.CharField(max_length=200, default="None", blank=True, null=True)  # Optional weaknesses

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')  # Redirect to the hero list view