from django.contrib import admin

# Register your models here.
from .models import Costumer, Products, Order

admin.site.register(Costumer)
admin.site.register(Products)
admin.site.register(Order)
