from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

from .models import Producto, Categoria


@login_required
def inicio(request):
    return render(request, "inicio.html")


@staff_member_required
def panel_encargado(request):
    return render(
        request,
        "panel_encargado.html"
    )


@login_required
def catalogo(request):

    productos = Producto.objects.filter(
        disponible=True,
        categoria__activa=True
    )

    buscar = request.GET.get("buscar")

    if buscar:
        productos = productos.filter(
            nombre__icontains=buscar
        )

    categoria_id = request.GET.get("categoria")

    if categoria_id:
        productos = productos.filter(
            categoria_id=categoria_id
        )

    categorias = Categoria.objects.filter(
        activa=True
    )

    return render(
        request,
        "catalogo.html",
        {
            "productos": productos,
            "categorias": categorias
        }
    )


@staff_member_required
def lista_categorias(request):

    categorias = Categoria.objects.all()

    return render(
        request,
        "categorias/lista.html",
        {
            "categorias": categorias
        }
    )
@staff_member_required
def lista_productos(request):

    productos = Producto.objects.all()

    buscar = request.GET.get("buscar")

    if buscar:
        productos = productos.filter(
            nombre__icontains=buscar
        ) | Producto.objects.filter(
            codigo__icontains=buscar
        )

    disponible = request.GET.get("disponible")

    if disponible == "1":
        productos = productos.filter(
            disponible=True
        )

    elif disponible == "0":
        productos = productos.filter(
            disponible=False
        )

    return render(
        request,
        "productos/lista.html",
        {
            "productos": productos
        }
    )