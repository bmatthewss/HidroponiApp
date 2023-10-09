from django.contrib import admin
from recetasApp.models import Unidade
from recetasApp.models import Ingrediente
from recetasApp.models import SaboresGeneral
from recetasApp.models import Hora
from recetasApp.models import Receta
from recetasApp.models import Accion
from recetasApp.models import InstruccionesEspecifica
from recetasApp.models import Utensilio
from recetasApp.models import Condimento
from recetasApp.models import Consistencia
from recetasApp.models import Paso
from recetasApp.models import PasoIngrediente

# Register your models here.

class RecetaAdmin (admin.ModelAdmin):
    list_display = ("nombre","publica","porciones","fechayhora")
    search_fields = ("nombre","porciones")
    list_filter = ("hora","saborGeneral")

class PasoAdmin (admin.ModelAdmin):
    list_display = ("id","receta","accion", "instruccionEspecifica", "utensiliosPrint", "tiempoMinutos", "temperatura", "condimentoEspecialPrint", "consistenciaPrint")
    search_fields = ("receta","tiempoMinutos", "temperatura")
    list_filter = ("accion","instruccionEspecifica", "utensilio", "condimentoEspecia", "consistenciaDeseada")

admin.site.register(Unidade)
admin.site.register(Ingrediente)
admin.site.register(SaboresGeneral)
admin.site.register(Hora)
admin.site.register(Receta,RecetaAdmin)
admin.site.register(Accion)
admin.site.register(InstruccionesEspecifica)
admin.site.register(Utensilio)
admin.site.register(Condimento)
admin.site.register(Consistencia)
admin.site.register(Paso,PasoAdmin)
admin.site.register(PasoIngrediente)