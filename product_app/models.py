from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    currency = models.CharField(max_length=3)
    img = models.CharField(max_length=400)

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}{self.currency}, {self.img}"