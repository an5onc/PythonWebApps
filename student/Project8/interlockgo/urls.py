from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),  # Client detail URL
    path('clients/add/', views.client_add, name='client_add'),
    path('clients/<int:client_id>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('test/', views.test_page, name='test_page'),
    path('register/', views.register, name='register'),
    
]