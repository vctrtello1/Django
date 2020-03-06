from django.contrib import admin
from gestioPedidos.models import clientes, articulos, pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion", )


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha", )
    date_hierarchy = ("fecha")


admin.site.register(clientes, ClientesAdmin)
admin.site.register(articulos, ArticulosAdmin)
admin.site.register(pedidos, PedidosAdmin)
