from django.contrib import admin

# Register your models here.
from emailGPT.models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ("titulo", "sugerenciaGenerada", "mensaje", "sugerencias")
    search_fields = ("titulo", "mensaje", "sugerencias")
    list_filter = ("sugerenciaGenerada",)

admin.site.register(Email,EmailAdmin)
