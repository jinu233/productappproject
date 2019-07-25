from . import forms
from django.shortcuts import  render
# Create your views here.

def index(request):
    form = forms.login()

    if request.method == 'POST':
        form = forms.login(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE

            print("USERNAME:" + form.cleaned_data['username'])
            print("PASSWORD: " + form.cleaned_data['pword'])

    return render(request,'newproject/login.html',{'form':form})

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("FIRSTNAME: "+form.cleaned_data['firstname'])
            print("LASTNAME:"+form.cleaned_data['lastname'])
            print("USERNAME:" + form.cleaned_data['username'])
            print("PASSWORD: "+form.cleaned_data['pword'])
            print("CONFIRM PASSWORD: " + form.cleaned_data['cpword'])


    return render(request,'newproject/registration.html',{'form':form})
