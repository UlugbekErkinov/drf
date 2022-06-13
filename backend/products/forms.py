from django import forms
from .models import Product

class ProductForm(forms.ModelsForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price' 
        ]