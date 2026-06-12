from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class PaymentTests(APITestCase):
    def test_list_payment_returns_200(self):
        response = self.client.get(reverse('payment-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_payment_returns_400(self):
        response = self.client.post(reverse('payment-list'), data={})
        self.assertEqual(response.status_code, 400)

    def test_list_payment_returns_list(self):
        response = self.client.get(reverse('payment-list'))
        self.assertIsInstance(response.data, list)
    
