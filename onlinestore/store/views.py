from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product
from django.http import HttpResponse


class Userlogin(LoginView):
    template_name = 'store/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('navigations')

def Navigations(request):
    return render(request, 'store/navigation.html')




class Categorieslist(ListView):
    model = Category
    template_name = 'store/category.html'
    context_object_name = 'categories'

class Categorydetail(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'

class Categoryedit(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')

class Categoryupdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')


class Categorydelete(DeleteView):
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('categories')

class Productlist(ListView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'products'

class Productdetail(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'

class Productedit(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')

class Productupdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class Productdelete(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')

