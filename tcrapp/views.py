from itertools import product

from django.shortcuts import render
from .models import Product  # Import your Product model
from django.http import HttpResponse


def home(request):
    products = Product.objects.all()  # Retrieve all products
    print(products)
    params = {'product': products}
    return render(request, 'home.html', params)


def aboutus(request):
    return render(request, 'aboutus.html')


def cart(request):
    return render(request, 'cart.html')
