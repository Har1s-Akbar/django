from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .usersforms import UserCreationForm
from .views import SignUpView

class UserTest(TestCase):
    def tesUser(self):
        User = get_user_model()
        user = User.objects.create_user(
            username= 'test1',
            email= 'test@gmail.com',
            password= 'test12',
        )
        self.assertEqual(user.username, 'test1')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        
    def testSuperUser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username= 'super1',
            email= 'super@gmail.com',
            password= 'tests12',
        )
        self.assertEqual(superuser.username, 'super1')
        self.assertEqual(superuser.email, 'super@gmail.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class SignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signUp(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Sign Up')
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertNotContains(self.response, 'I am not included')

    def test_signupForm(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_ViewSignUp(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__, SignUpView.as_view().__name__ 
        )