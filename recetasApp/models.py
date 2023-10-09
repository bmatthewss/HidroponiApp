import datetime

from django.db import models


# Create your models here.

class Unidade(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


# One to Many Rel
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=30)
    unidad = models.ForeignKey(Unidade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre


class SaboresGeneral(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Hora(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


# Many to Many and Many to Many plus additional fields
class Receta(models.Model):
    fechayhora = models.DateTimeField(auto_now_add=True)
    publica = models.BooleanField(default=False)
    nombre = models.CharField(max_length=30)
    porciones = models.PositiveIntegerField()
    hora = models.ManyToManyField(Hora)
    saborGeneral = models.ManyToManyField(SaboresGeneral)

    def __str__(self):
        return self.nombre


class Accion(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class InstruccionesEspecifica(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Utensilio(models.Model):
    articulo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Condimento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Consistencia(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Paso(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.DO_NOTHING, verbose_name="Nombre Receta")
    accion = models.ForeignKey(Accion, on_delete=models.DO_NOTHING, verbose_name="Accion")
    instruccionEspecifica = models.ForeignKey(InstruccionesEspecifica, on_delete=models.DO_NOTHING,
                                              verbose_name="Instruccion Especifica")
    ingredientes = models.ManyToManyField(Ingrediente, through='PasoIngrediente')
    tiempoMinutos = models.PositiveIntegerField(verbose_name="Duracion (min.)")
    utensilio = models.ManyToManyField(Utensilio, verbose_name="Utensilios")
    temperatura = models.PositiveIntegerField(blank=True)
    condimentoEspecia = models.ManyToManyField(Condimento, blank=True, verbose_name="Condimentos")
    consistenciaDeseada = models.ManyToManyField(Consistencia, blank=True, verbose_name="Consistencia")

    def utensiliosPrint(self):
        return self.utensilio.all().values_list('nombre', flat=True)

    def condimentoEspecialPrint(self):
        return self.condimentoEspecia.all().values_list('nombre', flat=True)

    def consistenciaPrint(self):
        return self.consistenciaDeseada.all().values_list('nombre', flat=True)

    def __str__(self):
        return self.receta.nombre + ' - Paso ' + str(self.id)


class PasoIngrediente(models.Model):
    paso = models.ForeignKey(Paso, on_delete=models.DO_NOTHING)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        a = self.receta.nombre + ': ' + str(self.cantidad) + self.ingrediente.unidadd.nombre \
            + ' de ' + self.ingrediente.nombre
        return a
