from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book

class BookView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'book.html'
    login_url='account_login'

class BookDetail(LoginRequiredMixin, PermissionRequiredMixin ,DetailView):
    model = Book
    template_name = 'book_detail.html'
    login_url = 'account_login'
    permission_required = 'book.special_status'