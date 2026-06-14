from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

User=get_user_model()


class UsersTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
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