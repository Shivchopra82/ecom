from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact, Order, OrderUpdate
from math import ceil
import json

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
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({})
        except Exception as e:
            return HttpResponse({})

    return render(request, 'shop/tracker.html')

def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')

        order = Order(items_json=itemsJson, name=name, email=email, address=address, city=city, state=state, zip_code=zip, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc= "Your order has been placed")
        update.save()
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':'thanls', 'id':id})
    return render(request, 'shop/checkout.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        var = "received"
        return render(request, 'shop/Contact.html', {"var": var})
    return render(request, 'shop/Contact.html')

def search(request):
    return HttpResponse("This is search page of our webapp")

def productview(request, id):
    prod = product.objects.get(id=id)
    return render(request, 'shop/productview.html', {'product': prod})
