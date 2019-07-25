from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)


# Create your views here.

from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data()
        context['injectme']="Basic Injection"
        return context
