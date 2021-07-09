from django.shortcuts import render, get_object_or_404
from .models import *
from basketapp.models import Basket


def products(request, pk=None):
    title = 'продукты'
    prod_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'prod_menu': prod_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'prod_menu': prod_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)
