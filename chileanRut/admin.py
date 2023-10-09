from django.contrib import admin

# Register your models here.
from chileanRut.models import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "sexo", "direccion","ciudad","estado","infoRecibida")
    search_fields = ("nombre", "rut", "direccion")
    list_filter = ("sexo","ciudad","estado",)

admin.site.register(Persona,PersonaAdmin)
