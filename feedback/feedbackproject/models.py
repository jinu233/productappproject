from django.db import models
from django.urls import reverse
# Create your models here.
class feedback(models.Model):
    course= models.CharField(max_length=200)
    feedback = models.CharField(max_length=256)

    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})