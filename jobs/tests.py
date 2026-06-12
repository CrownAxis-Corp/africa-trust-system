from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.
class JobTests(APITestCase):
    def test_list_jobs_returns_200(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_job_returns_400(self):
        response = self.client.post(reverse('job-list'), data={})
        self.assertEqual(response.status_code, 400)

    def test_list_jobs_returns_list(self):
        response = self.client.get(reverse('job-list'), data={})
        self.assertIsInstance(response.data, list)