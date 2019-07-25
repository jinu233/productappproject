from django.contrib import admin

#register your models here
from newproject.models import login,registration
admin.site.register(registration)
admin.site.register(login)
