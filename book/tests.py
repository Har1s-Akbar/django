from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review

class BookTestscreate(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email = 'reviewuser@gmail.com',
            password = 'reveiewadmin',
        )
        self.special_permission = Permission.objects.get(codename='special_status')
        self.book = Book.objects.create(
            title = 'Harry Potter',
            author= 'idk',
            price= '25'
        )
        self.reviews = Review.objects.create(
            review='a good book',
            author = self.user,
            book = self.book
        )

    def test_book_create(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'idk')
        self.assertEqual(f'{self.book.price}', '25')
    def test_logged_in(self):
        self.client.login(email='reviewuser@gmail.com', password='reveiewadmin')
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'book.html')
    def test_logged_out(self):
        self.client.logout()
        response= self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/book/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/book/'%(reverse('account_login'))
        )
        self.assertContains(response, 'Log In')

    def test_with_permission(self):
        self.client.login(email='reviewuser@gmail.com', password='reveiewadmin')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/book/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'a good book')
        self.assertTemplateUsed(response, 'book_detail.html')
