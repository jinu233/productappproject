from django.http import HttpResponse
from userdetails.models import Employee
from django.shortcuts import render
from userdetails.models import Employee

# Create your views here.

def homePage(request):
    return HttpResponse("WELCOME TO MY SECOND APPLICATION ")
def homeLocation(request):


    #return render(request,'Firstapp/Registration.html',context=mydict)
    return render(request, 'userdetails/registration.html')

def pageEmployee(request):
    webpages_list=Employee.objects.order_by('id')
    date_dict = {"employee_records": webpages_list}
    return render(request, 'userdetails/index.html', date_dict)