from django.shortcuts import render
from .models import Costumer, Products, Order
# Create your views here.


def home(request):
    orders = Order.objects.all()
    costumers = Costumer.objects.all()
    total_costumers = costumers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders, 'costumers': costumers,
        'total_costumers': total_costumers, 'total_orders': total_orders,
        'delivered': delivered, 'pending': pending
        }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def costumer(request):
    return render(request, 'accounts/costumer.html')
