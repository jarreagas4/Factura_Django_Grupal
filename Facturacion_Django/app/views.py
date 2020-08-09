from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm, ClienteForm,FacturaForm,DetalleFacturaForm
from .models import Producto, Cliente,Factura,DetalleFactura

def producto(request):
    opciones = {'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, './Producto/create.html', opciones)

def listarProducto(request):
    producto = Producto.objects.all()
    query = {'productos': producto}
    return render(request, './Producto/consultar.html', query)

def editarProducto(request, id):
    opciones = {'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto')
    return render(request, './Producto/create.html', opciones)
def Menu(request):
    return render(request, 'principal.html')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/listarproducto')
    return render(request, './Producto/delete.html', {'Producto':producto})

## Cliente
def cliente(request):
    opciones = {'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, './Cliente/cliente.html', opciones)

def editarCliente(request, id):
    opciones = {'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/listarcliente')

    return render(request, './Cliente/cliente.html', opciones)


def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'clientes': cliente}
    return render(request, './Cliente/listar_clientes.html', opciones)


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/listarcliente')
    return render(request, './Cliente/eliminar_cliente.html', {'Cliente': cliente})


## Factura
def factura(request):
    opciones = {'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarfactura')
    else:
        form = FacturaForm()
        opciones['form'] = form

    return render(request, './Factura/factura.html', opciones)

def editarFactura(request, id):
    opciones = {'accion': 'Actualizar'}
    factura = Factura.objects.get(id=id)
    if request.method == 'GET':
        form = FacturaForm(instance=factura)
        opciones['form'] = form
    else:
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('/listarfactura')

    return render(request,'./Factura/factura.html', opciones)


def listarFactura(request):
    factura = Factura.objects.all()
    opciones = {'facturas': factura}
    return render(request, './Factura/listar_facturas.html', opciones)


def eliminarFactura(request, id):
    factura = Factura.objects.get(id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('/listarfactura')
    return render(request, './Factura/eliminar_factura.html', {'Factura': factura})


## DetalleFactura
def detallefactura(request):
    opciones = {'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listardetallefactura')
    else:
        form = DetalleFacturaForm()
        opciones['form'] = form

    return render(request, './DetalleFactura/detallefactura.html', opciones)

def editarDetalleFactura(request, id):
    opciones = {'accion': 'Actualizar'}
    detallefactura = DetalleFactura.objects.get(id=id)
    if request.method == 'GET':
        form = DetalleFacturaForm(instance=detallefactura)
        opciones['form'] = form
    else:
        form = DetalleFacturaForm(request.POST, instance=detallefactura)
        if form.is_valid():
            form.save()
            return redirect('/listardetallefactura')

    return render(request,'./DetalleFactura/detallefactura.html', opciones)



def eliminarDetalleFactura(request, id):
    detallefactura = DetalleFactura.objects.get(id=id)
    if request.method == 'POST':
        detallefactura.delete()
        return redirect('/listardetallefactura')
    return render(request, './DetalleFactura/eliminar_detallefactura.html', {'DetalleFactura': detallefactura})


def listarDetalleFactura(request):
    detallefactura = DetalleFactura.objects.all()
    opciones = {'detallefacturas': detallefactura}
    return render(request, './DetalleFactura/listar_detallefacturas.html', opciones)

