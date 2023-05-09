import uuid
from django.urls import reverse

from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key= True,
        default= uuid.uuid4
    )
    title = models.TextField(max_length=50)
    author = models.TextField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='cover/', blank=True)


    def __str__(self):
        return self.title + " by "  + self.author
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete= models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=250)
    date = models.DateTimeField(auto_created=True, auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE
    )