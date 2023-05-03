from django.test import TestCase
from django.contrib.auth import get_user_model

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