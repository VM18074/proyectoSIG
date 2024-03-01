from django.contrib import admin

# Register your models here.
from .models import Producto, Pedido, Proveedor

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Proveedor)