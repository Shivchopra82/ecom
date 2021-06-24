from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    with open('static/ecom/ecom.txt', 'r') as rf:
        string = rf.read()
        dice = {'purpose':'Read', 'file': string}
    return render(request, 'ecom/index.html', dice)
