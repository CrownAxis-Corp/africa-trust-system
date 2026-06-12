from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.
class ContractTests(APITestCase):
    def test_list_contracts_returns_200(self):
        response = self.client.get(reverse('contract-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_contracts_return_400(self):
        response = self.client.post(reverse('contract-list'),data={})
        self.assertEqual(response.status_code, 400)

    def test_list_contracts_returns_list(self):
        response = self.client.get(reverse('contract-list'), data={})
        self.assertIsInstance(response.data, list)