from django.db import models
from applications.Departamentos.models import Departamento

# Create your models here.
class Habilidades(models.Model):
    habilidades = models.CharField('Habilidades', max_length=50)
    def __str__(self):
        return str(self.id) + " - " + self.habilidades

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','Administrador'),
        ('1','Gerente'),
        ('2','Contador'),
        ('3','Docente'),
        ('4','Director'),
        ('5','Almacenero'),
        ('6','Vigilante'),
    )

    first_name = models.CharField('Nombres:', max_length=50)
    last_name = models.CharField('Apellidos:', max_length=50)
    job = models.CharField('Trabajo:', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='empleados', null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return str(self.id) + " - " + self.first_name + " - " + self.last_name

    class Meta:
        #db_table = ''
        #managed = True
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
