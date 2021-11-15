from django.test import TestCase
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

