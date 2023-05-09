from django.contrib import admin
from .models import Book, Review

class ReviewList(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):

    inlines=[
        ReviewList
    ]


    list_display= ["title", "author" ,"price"]

admin.site.register(Book, BookAdmin)
