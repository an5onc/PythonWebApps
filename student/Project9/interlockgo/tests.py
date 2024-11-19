from django.test import TestCase, Client
from django.urls import reverse
from .models import Client as ClientModel  # Use alias if there's a name conflict

class ClientTests(TestCase):
    def setUp(self):
        # This setup runs before each test
        self.client = Client()  # Django test client
        self.client_data = {
            'first_name': 'Anson',
            'last_name': 'Cordeiro',
            'email': 'ansoncordeiro@yahoo.com',
            'phone_number': '9709094951'
        }
        self.client_instance = ClientModel.objects.create(**self.client_data)

    def test_home_page(self):
        # Test that the home page loads successfully
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Interlock Go")

    def test_client_list_page(self):
        # Test that the client list page loads successfully
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clients")

    def test_client_detail_page(self):
        # Test that the client detail page loads for a specific client
        response = self.client.get(reverse('client_detail', args=[self.client_instance.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.client_instance.first_name)

    def test_create_client(self):
        # Test the creation of a new client via a POST request
        response = self.client.post(reverse('client_add'), data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after creation
        self.assertEqual(ClientModel.objects.count(), 2)  # One new client is added

    def test_edit_client(self):
        # Test editing an existing client
        response = self.client.post(reverse('client_edit', args=[self.client_instance.id]), data={
            'first_name': 'UpdatedName',
            'last_name': self.client_instance.last_name,
            'email': self.client_instance.email,
            'phone_number': self.client_instance.phone_number
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after edit
        self.client_instance.refresh_from_db()
        self.assertEqual(self.client_instance.first_name, 'UpdatedName')

    def test_delete_client(self):
        # Test deleting a client
        response = self.client.post(reverse('client_delete', args=[self.client_instance.id]))
        self.assertEqual(response.status_code, 302)  # Check for redirect after deletion
        self.assertEqual(ClientModel.objects.count(), 0)  # Client count should be 0 after deletion