from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class UsersTest(APITestCase):
    def test_user_list_returns_200(self):
        url = reverse('user-list')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_list_returns_400(self):
        url= reverse('user-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 400)

    def test_user_check_statuscode(self):
        url = reverse('user-list')
        response = self.client.get(url, data={})
        self.assertIsInstance(response.data, list)