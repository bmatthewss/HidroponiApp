from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import re
from django.core.exceptions import ValidationError

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255,blank=True)
    rut = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100,blank=True)
    direccion = models.CharField(max_length=255,blank=True)
    ciudad = models.CharField(max_length=100,blank=True)
    estado = models.CharField(max_length=100,blank=True)
    infoRecibida =  models.BooleanField(default=False)

    def clean(self):
        pattern = r"^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$"
        match = re.match(pattern, self.rut)
        if not match:
            raise ValidationError("El rut no tiene un formato válido")
        else:
            rut_sin_dv = self.rut[:-1]
            rut_sin_dv = rut_sin_dv.replace(".", "")
            dv = self.rut[-1]
            if dv.upper() != self.calcular_dv(rut_sin_dv):
                raise ValidationError("El digito verificador es incorrecto")

    def __str__(self):
        return self.nombre

    def calcular_dv(self, rut):
        multiplo = 2
        acumulado = 0
        for i in range(len(rut) - 1, -1, -1):
            if rut[i].isnumeric():
                acumulado += int(rut[i]) * multiplo
                if multiplo == 7:
                    multiplo = 2
                else:
                    multiplo += 1
            else:
                continue
        dv = 11 - (acumulado % 11)
        if dv == 11:
            return "0"
        elif dv == 10:
            return "k"
        else:
            return str(dv)

    def __str__(self):
        return self.nombre

@receiver(post_save, sender=Persona)
def my_callback(sender, instance, **kwargs):

    # Do something with the instance here
    if not (instance.infoRecibida):
        respuesta = getRUT(instance.rut)

        if not (respuesta=="Error"):

            Persona.objects.filter(id=instance.id).update(nombre=respuesta["Nombre"],sexo=respuesta["Sexo"],direccion=respuesta["Direccion"],ciudad=respuesta["Ciudad"],estado=respuesta["Estado"],infoRecibida=True)
    pass

def getRUT(rut):
    url = f"https://rutificador.porsilapongo.cl/api/v1/persona/rut/{rut}"
    response = requests.get(url)
    if response.status_code == 200:
        respuesta = response.json()
        print("Persona Encontrada")
        return respuesta
    else:
        print("Error al recibir respuesta del servidor")
        return "Error"