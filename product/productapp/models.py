from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Product(models.Model):
    product = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('product_view', kwargs={'pk': self.pk})