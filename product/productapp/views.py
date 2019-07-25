# Create your views here.
from productapp.models import Product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ProductList(ListView):
    model = Product


class ProductView(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = ['product', 'price']
    success_url = reverse_lazy('product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['product', 'price']
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')