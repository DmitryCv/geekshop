from django.shortcuts import render
import json


def parse(menu_json):
    with open(menu_json,'r', encoding='utf-8') as f:
        menu = json.load(f)
    return menu['links']


def index(request):
    menu = parse('data.json')
    context = {'menu': menu}
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    menu = parse('data.json')
    context = {'menu': menu}
    return render(request, 'geekshop/contact.html', context)
