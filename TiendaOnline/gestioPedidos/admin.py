from django.contrib import admin
from gestioPedidos.models import clientes, articulos, pedidos

# Register your models here.
admin.site.register(clientes)
admin.site.register(articulos)
admin.site.register(pedidos)
