from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Costumer, Products, Order
from .forms import OrderForm
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


def costumer(request, pk_test):
    costumer = Costumer.objects.get(id=pk_test)
    orders = costumer.order_set.all()
    order_count = orders.count
    context = {
        'costumer': costumer, 'orders': orders,
        'order_count': order_count
        }
    return render(request, 'accounts/costumer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Costumer, Order, fields=('product', 'status'), extra=4)
    costumer = Costumer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=costumer)
    if request.method == 'POST':
        formset = OrderForm(request.POST, instance=costumer)
        if formset.is_valid():
            formset.save()
            return redirect('/home')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/home')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
