from django.shortcuts import render
from .models import Client
from django.urls import reverse

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def home(request):
    return render(request, 'home.html')

def test_page(request):
    return render(request, 'test_page.html')