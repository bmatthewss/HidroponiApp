import logging
import shutil
from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import openai
openai.api_key = "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"

class SrtHandler(FileSystemEventHandler):
    def on_modified(self, event):

        # Si el archivo es SRT
        if event.src_path.endswith(".srt"):

            # Lo abre y obtiene su info
            with open(event.src_path, "r") as f:
                fileContent = f.read()
                f.close()

            prompt = "Traduce este archivo de subtitulos srt al idioma ingles, manten el formato con tiempos: " + fileContent

            # Lo envia como consulta a ChatGPT
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                temperature=0
            )

            responseText = response["choices"][0]["text"]

            # Genera la respuesta como un nuevo archivo .srt en la carpeta translated
            print(responseText)
            path = 'subtitulosGPT/files/translated/'
            filename = os.path.basename(event.src_path)
            name, ext = os.path.splitext(filename)

            # Usa el módulo `os` para unir la ruta y el nombre del archivo
            file = os.path.join(path, name + ext)

            # Abre el archivo en modo escritura (w)
            with open(file, "w") as f:
                # Escribe el string en el archivo
                f.write(responseText)

         #   print("SrtHandler")
         #   filename = os.path.basename(event.src_path)
         #   # Mover archivo a processed
         #   shutil.move(event.src_path, 'subtitulosGPT/files/processed/' + filename)
#
         #   # Crear un archivo de registro
         #   logging.basicConfig(filename='subtitulosGPT/files/logs/logfile.log', level=logging.INFO)
#
         #   # Escribir mensaje de registro
         #   logging.info(f'Archivo {event.src_path} modificado y movido a subtitulosGPT/files/processed/')
#

#class GptHandler(FileSystemEventHandler):
#    def on_modified(self, event):
#
#        # Lee el contenido archivo
#        with open(event.src_path, "r") as f:
#            fileContent = f.read()
#            f.close()
#
#        print("GptHandler")
#
#        # Lo envia como consulta a ChatGPT
#        response = openai.Completion.create(
#            model="text-davinci-003",
#            prompt="Traduce este archivo de subtitulos al idioma ingles: "+fileContent,
#            max_tokens=2048,
#            temperature=0
#        )
#
#        # Genera la respuesta como un nuevo archivo .srt en la carpeta translated
#        print(response)
#        path = 'subtitulosGPT/files/translated/'
#        filename = os.path.basename(event.src_path)
#        name, ext = os.path.splitext(filename)
#
#        # Usa el módulo `os` para unir la ruta y el nombre del archivo
#        file = os.path.join(path, name+ext)
#
#        # Abre el archivo en modo escritura (w)
#        with open(file, "w") as f:
#            # Escribe el string en el archivo
#            f.write(response)
#
#        # Crear un archivo de registro
#        logging.basicConfig(filename='subtitulosGPT/files/logs/logfile.log', level=logging.INFO)
#
#        # Escribir mensaje de registro
#        logging.info(f'Archivo {event.src_path} modificado y movido a translated')

class Command(BaseCommand):
        help = "import booms"

        def add_arguments(self, parser):
            pass

        def handle(self, *args, **options):
            observer = Observer()
            observer.schedule(SrtHandler(), path='subtitulosGPT/files/received/', recursive=True)
            observer.start()
            print("El PID del proceso observer es: ", os.getpid())
            observer.join()

          #  observerGPT = Observer()
          #  observerGPT.schedule(SrtHandler(), path='subtitulosGPT/files/processed/', recursive=True)
          #  observerGPT.start()
          #  print("El PID del proceso observerGPT es: ", os.getpid())
          #  observerGPT.join()


