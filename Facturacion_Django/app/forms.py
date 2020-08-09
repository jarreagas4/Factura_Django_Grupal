from django import forms
from .models import Producto, Cliente,Factura,DetalleFactura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion','precio','stock','iva')
        label = {'descripcion': 'Producto', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion','producto')
        label = {'ruc': 'ruc', 'nombre': 'nombre', 'direccion': 'direccion','producto':'producto'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', 'total')
        label = {'cliente': 'cliente', 'fecha': 'fecha', 'total': 'total'}

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ('factura', 'producto', 'cantidad','precio','subtotal')
        label = {'factura': 'factura', 'producto': 'producto', 'cantidad': 'cantidad', 'precio': 'precio', 'subtotal': 'subtotal'}