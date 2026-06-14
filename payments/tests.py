from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

class PaymentTests(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
    def test_list_payment_returns_200(self):
        response = self.client.get(reverse('payment-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_payment_returns_400(self):
        response = self.client.post(reverse('payment-list'), data={})
        self.assertEqual(response.status_code, 400)

    def test_list_payment_returns_list(self):
        response = self.client.get(reverse('payment-list'))
        self.assertIsInstance(response.data, list)
    
