from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=128)
    course= models.CharField(max_length=128)
    topic = models.EmailField(max_length=254,unique=True)
    topic = models.EmailField(max_length=254, unique=True)
