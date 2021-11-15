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

class TestEndpoint(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_endpoint(self):
        request = self.factory.get('/api/providers')
        response = provider_list(request)
        self.assertEqual(response.status_code, 200)
