from django.contrib import admin
from .models import Consumo
from .models import Planta

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo', 'cantidad', 'costo_por_unidad', 'costo_total')

@admin.register(Planta)
class PlataAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'fecha_inicio', 'fecha_fin', 'estado')
