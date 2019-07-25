from django.db import models



class login(models.Model):
    uname = models.CharField(max_length=264,unique=True)
    pword = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.uname

class registration(models.Model):
    uname = models.CharField(max_length=264,unique=True)
    fname = models.CharField(max_length=264,unique=True)
    lname = models.CharField(max_length=264, unique=True)
    fname = models.CharField(max_length=264, unique=True)
    pword = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.uname
