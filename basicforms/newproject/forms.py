from django import forms
from django.core import validators


class FormName(forms.Form):
    firstname = forms.CharField()
    lastname=forms.CharField()
    username=forms.CharField()
    pword=forms.CharField()
    cpword = forms.CharField()


    def clean(self):
        all_clean_data = super().clean()
        pword = all_clean_data['pword']
        cpword= all_clean_data['cpword']

        if pword != cpword:
            raise forms.ValidationError("MAKE SURE PASSWORDS MATCH!")

class login(forms.Form):

    username=forms.CharField()
    pword=forms.CharField()


