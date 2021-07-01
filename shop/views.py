from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact
from math import ceil

def index(request):
    products = product.objects.all()
    all_prods = []
    categories_all_prods  = product.objects.values('prod_category', 'id')
    cats = {item['prod_category'] for item in categories_all_prods}
    for cat in cats:
        prod = product.objects.filter(prod_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all_prods.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': all_prods}
    return render(request, 'shop/index.html', params)







    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    # params = {'allProds':allProds }
    # return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    return render(request, 'shop/Tracker.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
    return render(request, 'shop/Contact.html')

def search(request):
    return HttpResponse("This is search page of our webapp")

def productview(request, id):
    prod = product.objects.get(id=id)
    return render(request, 'shop/productview.html', {'product': prod})
