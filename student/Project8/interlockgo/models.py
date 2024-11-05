from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    favorite_color = models.CharField(max_length=7, blank=True, help_text="Enter a color hex code, e.g., #ff5733")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    uploaded_file = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
