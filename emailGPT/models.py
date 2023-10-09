
import openai
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

openai.api_key = "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"

# Create your models here.
class Email(models.Model):
        titulo = models.CharField(max_length=300)
        sugerenciaGenerada = models.BooleanField(default=False,verbose_name="Sugerencia Generada?",editable=False)
        mensaje = models.TextField(max_length=1500)
        sugerencias = models.TextField(max_length=1500,blank=True)

        def __str__(self):
            return self.titulo

@receiver(post_save, sender=Email)
def my_callback(sender, instance, **kwargs):

    # Do something with the instance here
    if not (instance.sugerenciaGenerada):
        respuesta = respondeGPT(instance.mensaje)

        Email.objects.filter(id=instance.id).update(sugerencias=respuesta,sugerenciaGenerada=True)

        #instance.sugerencias = respuesta
        #instance.update()
    pass

def respondeGPT(pregunta):

    prompt = "Haz un analisis de sentimiento de cada parrafo de este email. " \
             "Por cada parrafo con un sentimiento negativo, " \
             "sugiere uno nuevo que tenga el mismo sentido," \
             "pero que utilice palabras y tonos mas positivos." \
             "Email: " + pregunta

    # Lo envia como consulta a ChatGPT
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        temperature=0
    )

    return response["choices"][0]["text"]