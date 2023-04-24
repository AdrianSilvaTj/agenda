#
from model_utils.models import TimeStampedModel
#
from django.db import models


#
class Hobby(TimeStampedModel):
    hobby = models.CharField('Pasa Tiempo', max_length=50)
    
    class Meta:
        verbose_name = 'Pasa Tiempo'
        verbose_name_plural = 'Pasa Tiempos'
    
    def __str__(self):
        return self.hobby

class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobby = models.ManyToManyField(Hobby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name

class Meeting(TimeStampedModel):
    """ Modelo para Reuniones """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    asunto  = models.CharField('Asunto', max_length=100)
    
    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return self.asunto