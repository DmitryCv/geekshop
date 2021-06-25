from django.shortcuts import render
from geekshop.views import parse


prod_menu = [
    {'href': '#', 'name': 'все'},
    {'href': '#', 'name': 'дом'},
    {'href': '#', 'name': 'офис'},
    {'href': '#', 'name': 'модерн'},
    {'href': '#', 'name': 'классика'},
]


def products(request):
    menu = parse('data.json')
    context = {
        'menu': menu,
        'prod_menu': prod_menu
    }
    return render(request, 'mainapp/products.html', context)
