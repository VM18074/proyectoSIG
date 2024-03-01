from django.db import models


# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre_producto

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=255, null=False)
    correo_electronico = models.EmailField(null=False)
    direccion_envio = models.TextField(null=False)
    fecha_pedido = models.DateField(null=False)
    estado_pedido = models.CharField(max_length=50, null=False)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return str(self.id_pedido) + " - " + self.nombre_cliente

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=255, null=False)
    nombre_contacto = models.CharField(max_length=255, null=False)
    correo_electronico = models.EmailField(null=False)
    numero_telefonico = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre_proveedor

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255, null=False)
    correo_electronico = models.EmailField(null=False)
    usuario = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)  # Renamed for security

    def __str__(self):
        return self.nombre_usuario