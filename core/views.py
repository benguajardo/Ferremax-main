from django.shortcuts import render, redirect
from .models import *
from .forms import *



def index(request):
    return render(request, 'core/index.html')
    
def shop(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/shop.html', data)

def base(request):
    return render(request, 'core/base.html')

def detail(request,id):
    producto = Producto.objects.get(id=id) # BUSCA PRODUCTO POR ID
    data={
        'producto' : producto
    }
    return render(request, 'core/detail.html', data)

def contact(request):
    return render(request, 'core/contact.html')
def checkout(request):
    return render(request, 'core/checkout.html')

def cart(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/cart.html', data)

def a(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/a.html', data)

# CRUD PRODUCTO
def addProduct(request):
    data={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # RECIBE TODA INFO DEL FORM
        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Producto agregado correctamente!"
    return render(request, 'core/addProduct.html', data)

def updateProduct(request,id):
    producto = Producto.objects.get(id=id) # BUSCA PRODUCTO POR ID
    data={
        'producto' : producto,
        'form': ProductoForm(instance=producto) # CARGA INFO EN EL FORM
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
            data['msj'] = "Producto modificado correctamente!"
    return render(request, 'core/updateProduct.html',data)

def deleteProduct(request,id):
    producto= Producto.objects.get(id=id)# BUSCA PRODUCTO POR ID
    producto.delete()
    return redirect(to="shop")
