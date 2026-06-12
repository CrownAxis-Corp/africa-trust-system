from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.

class DisputeTests(APITestCase):
    def test_dispute_returns_200(self):
        url = reverse('dispute-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_dispute_returns_400(self):
        url = reverse('dispute-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 400)

    def test_dispute_checks_statuscode(self):
        url = reverse('dispute-list')
        response = self.client.get(url)
        self.assertIsInstance(response.data,list)