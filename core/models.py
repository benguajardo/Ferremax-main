from datetime import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect



class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.IntegerField
    fechaNac = models.DateField
    def  __str__(self):
        return self.nombre+self.apellido

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sueldo = models.IntegerField
    fechaNac = models.DateField
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    def  __str__(self):
        return self.nombre+self.apellido
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True,blank=True)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    stock = models.IntegerField()
    def  __str__(self):
        return self.nombre
    

    
class Boleta(models.Model):
    fecha = models.DateField
    total = models.IntegerField
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def  __str__(self):
        return self
    
class DetalleBol(models.Model):
    cantidad = models.PositiveIntegerField(default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    def  __str__(self):
        return self.producto.nombre+' x'+self.cantidad

class Envio(models.Model):
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField
    fecha = models.DateField
    destino = models.CharField(max_length=50)

    def  __str__(self):
        return self.descripcion
    
# class CarritoProducto(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def subtotal(self):
#         return self.producto.precio * self.cantidad

# class CarritoCliente(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(CarritoProducto)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def calcular_desc(self):
#         acumulador = 0
#         descuento = 0
#         for aux in self.items.all():
#             if aux.usuario.suscrito == True:
#                 acumulador += aux.subtotal()
#                 descuento = round(acumulador * 0.05)
#             else:
#                 acumulador += aux.subtotal()
#                 descuento = 0
#         return descuento
#     def calcular_total(self):
#         acumulador = 0
#         total = 0
#         for aux in self.items.all():
#             if aux.usuario.suscrito == True:
#                 acumulador += aux.subtotal()
#                 total = round(acumulador * 0.95)
#             else:
#                 acumulador += aux.subtotal()
#                 total = acumulador
#         return total
