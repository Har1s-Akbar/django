from django.views.generic import ListView, DetailView
from .models import Book

class BookView(ListView):
    model = Book
    template_name = 'book.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'