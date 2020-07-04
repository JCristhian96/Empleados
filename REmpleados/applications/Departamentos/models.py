from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    anulate = models.BooleanField('Anulado', default = False)

    def __str__(self):
        return self.name + " - " + self.short_name

    class Meta:
        #db_table = ''
        #managed = True
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
