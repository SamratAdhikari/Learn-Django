from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")

def tracker(request):
    return HttpResponse("Tacker")

def search(request):
    return HttpResponse("Search")

def product(request):
    return HttpResponse("Product")

def checkout(request):
    return HttpResponse("Checkout")
