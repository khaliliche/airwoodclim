from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'city', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 06XXXXXXXX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre ville'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complete'}),
        }