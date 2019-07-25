from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return HttpResponse("<h1>welcome </h1>")
def myfirstpage(request):
    return HttpResponse('Hi')
def page(request):
    return render(request,'index.html')