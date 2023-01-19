from django.core.management.base import BaseCommand
import pandas as pd
from recetasApp.models import Unidade
from recetasApp.models import Hora
from recetasApp.models import SaboresGeneral
from recetasApp.models import Condimento

class Command(BaseCommand):
        help = "import booms"

        def add_arguments(self, parser):
            pass

        def handle(self, *args, **options):

            #Database Connections Here
            df=pd.read_csv('recetasApp/fixtures/UnidadInitialDataBulkLoad.csv')
            for NOMBRE in df.Nombre:
                    models=Unidade(nombre=NOMBRE)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)

            df=pd.read_csv('recetasApp/fixtures/HoraInitialDataBulkLoad.csv')
            for HORA in df.Hora:
                    models=Hora(nombre=HORA)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)


            df=pd.read_csv('recetasApp/fixtures/SaboresGeneralesInitialDataBulkLoad.csv')
            for SABORESGENERALES in df.SaboresGenerales:
                    models=SaboresGeneral(nombre=SABORESGENERALES)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)



            df=pd.read_csv('recetasApp/fixtures/CondimentoInitialDataBulkLoad.csv')
            for CONDIMENTOS in df.Condimentos:
                    models=Condimento(nombre=CONDIMENTOS)
                    try:
                        models.save()
                        print("Model saved successfully")
                    except Exception as e:
                        print("Error saving model:", e)