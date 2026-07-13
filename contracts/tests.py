from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Contract
User = get_user_model()

# Create your tests here.
class ContractTests(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='testuser', password='testpass123')
        self.contractor_user = User.objects.create_user(username='testcontractor', password='testcontractor123')
        self.other_user = User.objects.create_user(username='testother', password='other123')
        self.contract = Contract.objects.create(
            client = self.client_user,
            contractor = self.contractor_user,
            title='Airbnb Host',
            description='someone who is familiar with airbnb business',
            amount = 100000
        )
       

    def test_client_can_access_contract(self):
        url= reverse('contract-detail', kwargs={'pk':self.contract.id})
        self.client.force_authenticate(user = self.client_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_contractor_can_access_contract(self):
        url= reverse('contract-detail', kwargs={'pk':self.contract.id})
        self.client.force_authenticate(user = self.contractor_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_non_client_or_contractor_returns_403(self):
        url=reverse('contract-detail', kwargs={'pk':self.contract.id})
        self.client.force_authenticate(user=self.other_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


    def test_list_contracts_returns_200(self):
        self.client.force_authenticate(user=self.client_user)
        response = self.client.get(reverse('contract-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_contracts_return_400(self):
        self.client.force_authenticate(user=self.client_user)
        response = self.client.post(reverse('contract-list'),data={})
        self.assertEqual(response.status_code, 400)

    def test_list_contracts_returns_list(self):
        self.client.force_authenticate(user=self.contractor_user)
        response = self.client.get(reverse('contract-list'), data={})
        self.assertIsInstance(response.data, list)