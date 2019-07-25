from django.shortcuts import  render
from . import forms

def index(request):
    return render(request,'employee/index.html')
def form_name_view(request):
    form=forms.FormName()


    if

    return render(request,'employee/form_page.html',{'form':form})





