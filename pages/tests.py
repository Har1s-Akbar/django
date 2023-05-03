from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomeView

class HomeTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        
    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    def testCorrectHtml(self):
        self.assertContains(self.response, 'home')
    def testWrongHtml(self):
        self.assertNotContains(self.response, 'Hi, I should not be on the page')

    def testView(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)