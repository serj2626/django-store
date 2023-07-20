from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {'title': 'Test Title',
               'username': 'Sergey'
               }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
