import uuid
from django.db import models
from django.urls import reverse

class Book(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key= True,
        default= uuid.uuid4
    )
    title = models.TextField(max_length=50)
    author = models.TextField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title + " by "  + self.author
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    