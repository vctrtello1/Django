from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return render(request, 'accounts/products.html')


def costumer(request):
    return render(request, 'accounts/costumer.html')
