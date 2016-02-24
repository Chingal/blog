from django.db import models

class Entrada(models.Model):
    #Atributos Propios del Modelo
    titulo    = models.CharField(max_length=140)
    contenido = models.TextField()
    fecha     = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('Entrada')
        verbose_name_plural = ('Entradas')

    def __unicode__(self):
        return self.titulo