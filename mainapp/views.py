from django.shortcuts import render
from geekshop.views import parse
from .models import *


def products(request):
    menu = parse('data.json')
    prod_menu = ProductCategory.objects.all()
    context = {
        'menu': menu,
        'prod_menu': prod_menu,
    }
    return render(request, 'mainapp/products.html', context)
