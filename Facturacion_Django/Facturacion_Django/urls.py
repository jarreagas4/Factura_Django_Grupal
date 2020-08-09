"""Facturacion_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import producto, listarProducto,detallefactura,editarDetalleFactura,eliminarDetalleFactura,listarDetalleFactura, editarProducto,factura,editarFactura,listarFactura,eliminarFactura, Menu, eliminarProducto, cliente, listarCliente, eliminarCliente, editarCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', producto, name='producto-creacion'),
    path('listarproducto/', listarProducto, name='listarProducto'),
    path('editarproducto/<int:id>/', editarProducto, name='editarproducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarproducto'),
    ## Urls Cliente
    path('cliente/', cliente, name='cliente'),
    path('editarcliente/<int:id>/', editarCliente, name='editarcliente'),
    path('listarcliente/', listarCliente, name='listarcliente'),
    path('eliminarcliente/<int:id>', eliminarCliente, name='eliminarcliente'),
  
    ##Urls Factura
    path('factura/', factura, name='factura'),
    path('editarfactura/<int:id>/', editarFactura, name='editarfactura'),
    path('listarfactura/', listarFactura, name='listarfactura'),
    path('eliminarfactura/<int:id>', eliminarFactura, name='eliminarfactura'),
    ##Urls Detalle Factura
     path('detallefactura/', detallefactura, name='detallefactura'),
    path('editardetallefactura/<int:id>/', editarDetalleFactura, name='editardetallefactura'),
    path('listardetallefactura/', listarDetalleFactura, name='listardetallefactura'),
    path('eliminardetallefactura/<int:id>', eliminarDetalleFactura, name='eliminardetallefactura'),
    path('', Menu, name='index'),

]
