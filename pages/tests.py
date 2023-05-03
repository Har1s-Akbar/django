from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomeTest(SimpleTestCase):
    def Setup(self):
        url = reverse('home')
        self.response = self.client.get(url)
    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
