import json

from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APIRequestFactory
from .views import provider_list

from app.models import Provider


class ProviderTestCase(TestCase):
    def setUp(self):
        Provider.objects.create(name="Test Provider")

    def test_defaults(self):
        """Providers defaults"""
        test_provider = Provider.objects.get(name="Test Provider")
        self.assertEqual(test_provider.fees, 0.0000)
        self.assertEqual(test_provider.minimum_balance, 0.0000)
        self.assertEqual(test_provider.automated, False)
        self.assertEqual(test_provider.advisor, False)
        self.assertEqual(test_provider.ease_of_use, 3)

class ProvidersEndpointGET(TestCase):
    def setUp(self):
        self.base_url = '/api/providers'
        self.factory = APIRequestFactory()
        self.keys = ('id', 'name', 'fees', 'minimum_balance', 'automated', 'advisor', 'ease_of_use')
        Provider.objects.create(name="Test Provider1")
        Provider.objects.create(name="Test Provider2")
        Provider.objects.create(name="Test Provider3")
        Provider.objects.create(name="Test Provider4")
    
    def test_endpoint(self):
        request = self.factory.get(self.base_url)
        response = provider_list(request)
        self.assertEqual(response.status_code, 200)
    
    def test_response(self):
        request = self.factory.get(self.base_url)
        response = provider_list(request)
        json_data = json.loads(response.content)
        self.assertEqual(len(json_data), 4)
        for item in json_data:
            if not all(key in item for key in self.keys):
                self.fail(f"Missing key from {self.keys}\n{item}")
    
    def test_limit_inbounds(self):
        request = self.factory.get(self.base_url + '?limit=3')
        response = provider_list(request)
        json_data = json.loads(response.content)
        self.assertEqual(len(json_data), 3)

    def test_limit_outbounds(self):
        request = self.factory.get(self.base_url + '?limit=6')
        response = provider_list(request)
        json_data = json.loads(response.content)
        self.assertEqual(len(json_data), 4)

class ProvidersPriorities(TestCase):
    def setUp(self):
        self.base_url = '/api/providers'
        self.factory = APIRequestFactory()
        Provider.objects.create(name='1', fees=100, minimum_balance=400)
        Provider.objects.create(name='2', fees=200, minimum_balance=300)
        Provider.objects.create(name='3', fees=300, minimum_balance=200)
        Provider.objects.create(name='4', fees=400, minimum_balance=100)
 
    def test_default_priority(self):
        request = self.factory.get(self.base_url)
        response = provider_list(request)
        json_data = json.loads(response.content)
        self.assertEqual(json_data[0]['name'], '1')
        self.assertEqual(json_data[1]['name'], '2')
        self.assertEqual(json_data[2]['name'], '3')
        self.assertEqual(json_data[3]['name'], '4')
    
    def test_given_priority(self):
        request = self.factory.get(self.base_url + '?priority=minimum_balance')
        response = provider_list(request)
        json_data = json.loads(response.content)
        self.assertEqual(json_data[0]['name'], '4')
        self.assertEqual(json_data[1]['name'], '3')
        self.assertEqual(json_data[2]['name'], '2')
        self.assertEqual(json_data[3]['name'], '1')
