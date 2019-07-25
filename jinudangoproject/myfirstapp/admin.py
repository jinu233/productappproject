from django.contrib import admin

#register your models here
from myfirstapp.models import Topic,Webpage,AccessRecord
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)


