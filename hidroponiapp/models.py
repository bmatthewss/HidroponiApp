from django.db import models
from django.utils import timezone


class Consumo(models.Model):
    TIPOS_CONSUMO = (
        ('Agua', 'Agua'),
        ('Energía', 'Energía'),
        ('Nutrientes', 'Nutrientes'),
    )

    fecha = models.DateTimeField(auto_now_add=True, blank=False)
    tipo = models.CharField(max_length=10, choices=TIPOS_CONSUMO, blank=False)
    cantidad = models.FloatField(blank=False)
    costo_por_unidad = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def get_color_tipo(self):
        colors = {
            'Agua': 'primary',
            'Energía': 'warning',
            'Nutrientes': 'success',
            # Agrega más colores para los tipos de plantas aquí
        }
        return colors.get(self.tipo,
                          'secondary')  # El color 'secondary' será el color por defecto si no se encuentra el tipo de planta en el diccionario 'colors'
    def get_icon_tipo(self):
        colors = {
            'Agua': 'droplet',
            'Energía': 'lightning',
            'Nutrientes': 'tree',
            # Agrega más colores para los tipos de plantas aquí
        }
        return colors.get(self.tipo,
                          'secondary')  # El color 'secondary' será el color por defecto si no se encuentra el tipo de planta en el diccionario 'colors'



    def costo_total(self):
        return self.cantidad * float(self.costo_por_unidad)


class Planta(models.Model):
    VIVA = 'Viva'
    MUERTA = 'Muerta'
    COSECHADA = 'Cosechada'

    TIPOS_DE_PLANTAS = (
        ('Lechuga', 'Lechuga'),
        ('Espinaca', 'Espinaca'),
        ('Tomate', 'Tomate'),
        # Agrega más tipos de plantas aquí
    )

    ESTADOS_DE_PLANTAS = (
        ('Viva', 'Viva'),
        ('Muerta', 'Muerta'),
        ('Cosechada', 'Cosechada'),
    )

    tipo = models.CharField(max_length=20, choices=TIPOS_DE_PLANTAS)
    fecha_inicio = models.DateField(default=timezone.now)  # Establecer la fecha de inicio predeterminada como "ahora"
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_DE_PLANTAS, default='Viva')

    def __str__(self):
        return self.tipo

    def get_color(self):
        colors = {
            'Lechuga': 'primary',
            'Espinaca': 'success',
            'Tomate': 'danger',
            # Agrega más colores para los tipos de plantas aquí
        }
        return colors.get(self.tipo,
                          'secondary')  # El color 'secondary' será el color por defecto si no se encuentra el tipo de planta en el diccionario 'colors'

    def get_color_status(self):
        colors = {
            'Muerta': 'secondary',
            'Viva': 'success',
            'Cosechada': 'warning',
            # Agrega más colores para los tipos de plantas aquí
        }
        return colors.get(self.estado,
                          'secondary')  # El color 'secondary' será el color por defecto si no se encuentra el tipo de planta en el diccionario 'colors'
