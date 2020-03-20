from django.contrib import admin

# Register your models here.
from .models import Costumer, Products, Order, Tag

admin.site.register(Costumer)
admin.site.register(Products)
admin.site.register(Tag)
admin.site.register(Order)
