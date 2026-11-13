from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activa")
    search_fields = ("nombre",)
    list_filter = ("activa",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "categoria",
        "precio",
        "stock",
        "disponible"
    )

    search_fields = (
        "nombre",
        "codigo"
    )

    list_filter = (
        "categoria",
        "disponible"
    )


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente",
        "fecha",
        "estado",
        "total"
    )

    list_filter = ("estado",)
    search_fields = ("cliente__username",)

    inlines = [DetallePedidoInline]


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = (
        "pedido",
        "producto",
        "cantidad",
        "subtotal"
    )