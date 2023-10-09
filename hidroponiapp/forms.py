from django import forms
from .models import Consumo, Planta

class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = ['tipo', 'cantidad', 'costo_por_unidad']
        widgets = {
            'tipo': forms.Select(attrs={'required': True}),
            'cantidad': forms.NumberInput(attrs={'required': True}),
            'costo_por_unidad': forms.NumberInput(attrs={'required': True}),
        }

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['tipo']