from django.contrib import admin
from gestioPedidos.models import clientes, articulos, pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")


admin.site.register(clientes, ClientesAdmin)
admin.site.register(articulos)
admin.site.register(pedidos)
