from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.urls import reverse
from .forms import RegisterForm, ClientForm
from django.contrib.auth import login

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def home(request):
    return render(request, 'home.html')

def test_page(request):
    return render(request, 'test_page.html')

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})

def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user right after registration
            return redirect('home')  # Redirect to the home page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})