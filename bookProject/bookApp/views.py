# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from bookApp.models import Book

class bookList(ListView):
    model = Book

class book_view(DetailView):
    model=Book
