from django.db import models

# Create your models here.
from django.db import models  # Import Django's built-in model module

class Note(models.Model):  # Create a Note model that inherits from Django's base Model class
    title = models.CharField(max_length=200)   # A title field with a maximum length of 200 characters
    author = models.CharField(max_length=200)  # An author field with a maximum length of 200 characters
    body = models.TextField()                  # A body field for the main content, allows unlimited text

def __str__(self):  # Define a string representation for each instance of the Note model
    return f'{self.pk}. {self.title} - {self.author}'  # Return the title of the note