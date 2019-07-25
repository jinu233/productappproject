# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from myfirstapp.models import *

# def homePage(request):
#     return HttpResponse("<h1>this is my first application</h1>")


def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={"access_records":webpages_list}
    print (date_dict)
    return render(request,'myfirstapp/myfirstapp.html',date_dict)
