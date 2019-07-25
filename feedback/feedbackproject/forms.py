from django import forms
from django.core import validators


class FormName(forms.Form):
    course = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)

