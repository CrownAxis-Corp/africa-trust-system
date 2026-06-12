
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
class TrustEventTests(APITestCase):
    def test_trustevent_list_returns_200(self):
        response = self.client.get(reverse('trustevent-list'))
        self.assertEqual(response.status_code, 200)

    def test_trustevent_create_returns_400(self):
        response = self.client.post(reverse('trustevent-list'), data ={})
        self.assertEqual(response.status_code, 400)

    def test_trustevent_test_statuscode(self):
        response = self.client.get(reverse('trustevent-list'))
        self.assertIsInstance(response.data, list)