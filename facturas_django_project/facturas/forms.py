from django import forms
from .models import Factura, ProductoFactura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente']

class ProductoFacturaForm(forms.ModelForm):
    class Meta:
        model = ProductoFactura
        fields = ['producto', 'cantidad']