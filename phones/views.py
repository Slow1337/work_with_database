from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    order = request.GET.get('sort')
    template = 'catalog.html'
    if order == 'name':
        phones = Phone.objects.all().order_by('name')
    elif order == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif order == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
