from django.db import models

class Book(models.Model):
    title = models.TextField(max_length=50)
    author = models.TextField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title + " by "  + self.author