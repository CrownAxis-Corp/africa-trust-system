from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Job

User = get_user_model()

# Create your tests here.
class JobTests(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='testuser', password = 'testpass123')
        self.interfere = User.objects.create_user(username='testedit', password = 'editpass123')
        self.job = Job.objects.create(
            title= 'Video Editing', 
            description = 'Edit a promotional video',
            location ='Kagarama',
            budget='50000', 
            client = self.owner
            )
        self.client.force_authenticate(user=self.owner)

    def test_non_owner_cannot_edit_job(self):
        url = reverse('job-detail', kwargs={'pk':self.job.id})
        self.client.force_authenticate(user = self.interfere)
        response = self.client.put(url, data={
            'title': 'Video Games Coach', 
            'description': 'We want some one who can teach kids how to play fifa 26',
            'location':'Morocco',
            'budget':'100000', 
        })
        self.assertEqual(response.status_code, 403)

    def test_owner_can_edit_job(self):
        url = reverse('job-detail', kwargs={'pk':self.job.id})
        self.client.force_authenticate(user = self.owner)
        response = self.client.put(url, data={
            'title': 'Fitness trainer', 
            'description': 'We want some one who has a background with gym equipments',
            'location':'Kigali-Remera',
            'budget':'15000', 
        })
        self.assertEqual(response.status_code, 200)
    


    def test_list_jobs_returns_200(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_job_returns_400(self):
        response = self.client.post(reverse('job-list'), data={})
        self.assertEqual(response.status_code, 400)

    def test_list_jobs_returns_list(self):
        response = self.client.get(reverse('job-list'), data={})
        self.assertIsInstance(response.data, list)