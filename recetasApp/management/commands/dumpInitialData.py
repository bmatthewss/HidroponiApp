from django.core.management.base import BaseCommand
import pandas as pd
from recetasApp.models import Unidade
from recetasApp.models import Hora
from recetasApp.models import SaboresGeneral
from recetasApp.models import Condimento
from recetasApp.models import Consistencia
from recetasApp.models import Utensilio
from recetasApp.models import Accion
from recetasApp.models import InstruccionesEspecifica
from recetasApp.models import Ingrediente

class Command(BaseCommand):
        help = "import booms"

        def add_arguments(self, parser):
            pass

        def handle(self, *args, **options):

            #Unidad
            df=pd.read_csv('recetasApp/fixtures/UnidadInitialDataBulkLoad.csv')
            for NOMBRE in df.Nombre:
                    models=Unidade(nombre=NOMBRE)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #Hora
            df=pd.read_csv('recetasApp/fixtures/HoraInitialDataBulkLoad.csv')
            for HORA in df.Hora:
                    models=Hora(nombre=HORA)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #SaboresGenerale
            df=pd.read_csv('recetasApp/fixtures/SaboresGeneralesInitialDataBulkLoad.csv')
            for SABORESGENERALES in df.SaboresGenerales:
                    models=SaboresGeneral(nombre=SABORESGENERALES)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #Condimento
            df=pd.read_csv('recetasApp/fixtures/CondimentoInitialDataBulkLoad.csv')
            for CONDIMENTOS in df.Condimentos:
                    models=Condimento(nombre=CONDIMENTOS)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #Consistencia
            df=pd.read_csv('recetasApp/fixtures/ConsistenciaInitialDataBulkLoad.csv')
            for CONSISTENCIAS in df.Consistencia:
                    models=Consistencia(nombre=CONSISTENCIAS)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #Utensilio
            df=pd.read_csv('recetasApp/fixtures/UtensiliosInitialDataBulkLoad.csv')
            for UTENSILIOS in df.Utensilios:
                    models=Utensilio(nombre=UTENSILIOS)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #Accion
            df=pd.read_csv('recetasApp/fixtures/AccionInitialDataBulkLoad.csv')
            for ACCIONES in df.Accion:
                    models=Accion(nombre=ACCIONES)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            #InstruccionEspecifica
            df=pd.read_csv('recetasApp/fixtures/InstruccionEspecificaInitialDataBulkLoad.csv')
            for INSTRUCCIONES in df.InstruccionEspecifica:
                    models=InstruccionesEspecifica(nombre=INSTRUCCIONES)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)



            #Ingrediente
            df=pd.read_csv('recetasApp/fixtures/IngredientesInitialDataBulkLoad.csv')
            for INGREDIENTES in df.Ingredientes:
                    models=Ingrediente(nombre=INGREDIENTES)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

