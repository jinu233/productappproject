# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=264,unique=True)
    email=models.EmailField(max_length=264,unique=True)
    salary=models.CharField(max_length=264,unique=True)
    def _str_(self):
        return self.id


