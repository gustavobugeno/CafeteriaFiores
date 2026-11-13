from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from cafeteria.views import inicio, panel_encargado, catalogo
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
        '',
        inicio,
        name='inicio'
    ),
    path(
    'catalogo/',
    catalogo,
    name='catalogo'
),
]