from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

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
    username= 'newuser'
    email= 'user@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Sign Up')
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertNotContains(self.response,'I am not n the page')

    def test_user_craete(self):
        newuser = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEquals(get_user_model().objects.all()[0].email,self.email)