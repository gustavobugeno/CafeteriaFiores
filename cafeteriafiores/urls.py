from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from cafeteria.views import (
    inicio,
    panel_encargado,
    catalogo,
    lista_categorias,
    lista_productos
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'encargado/',
        panel_encargado,
        name='panel_encargado'
    ),

    path(
        'encargado/categorias/',
        lista_categorias,
        name='lista_categorias'
    ),

    path(
        'catalogo/',
        catalogo,
        name='catalogo'
    ),

    path(
        '',
        inicio,
        name='inicio'
    ),
    path(
    'encargado/productos/',
    lista_productos,
    name='lista_productos'
    ),
]