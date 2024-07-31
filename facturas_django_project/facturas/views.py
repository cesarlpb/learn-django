
# Create your views here.

from django.shortcuts import render, redirect
from .models import Factura, ProductoFactura
from .forms import FacturaForm, ProductoFacturaForm

def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        if factura_form.is_valid():
            factura = factura_form.save()
            return redirect('agregar_productos', factura_id=factura.id)
    else:
        factura_form = FacturaForm()
    return render(request, 'facturas/crear_factura.html', {'factura_form': factura_form})

def agregar_productos(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    if request.method == 'POST':
        producto_form = ProductoFacturaForm(request.POST)
        if producto_form.is_valid():
            producto_factura = producto_form.save(commit=False)
            producto_factura.factura = factura
            producto_factura.save()
            return redirect('detalle_factura', factura_id=factura.id)
    else:
        producto_form = ProductoFacturaForm()
    return render(request, 'facturas/agregar_productos.html', {'producto_form': producto_form, 'factura': factura})

def detalle_factura(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    productos_factura = ProductoFactura.objects.filter(factura=factura)
    total = sum(pf.producto.precio * pf.cantidad for pf in productos_factura)
    return render(request, 'facturas/detalle_factura.html', {'factura': factura, 'productos_factura': productos_factura, 'total': total})