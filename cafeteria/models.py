from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    codigo = models.CharField(max_length=7, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Pedido(models.Model):
    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("En preparación", "En preparación"),
        ("Listo", "Listo"),
        ("Entregado", "Entregado"),
    ]

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField(auto_now_add=True)
    hora_retiro = models.TimeField()
    observacion = models.TextField(blank=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Pendiente"
    )

    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Pedido #{self.id}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"