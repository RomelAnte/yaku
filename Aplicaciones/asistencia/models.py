from django.db import models
from eventos.models import Evento
from socios.models import Socio

# Create your models here.
class Asistencia(models.Model):
    id_asi 	= models.AutoField(primary_key=True)
    fk_id_eve = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fk_id_soc = models.ForeignKey(Socio, on_delete=models.CASCADE)
    tipo_asi = 	models.CharField(max_length=100)
    valor_asi = models.DecimalField(max_digits=10, decimal_places =2)	
    atraso_asi = models.CharField(max_length=25)	
    valor_atraso_asi = models.DecimalField(max_digits=10, decimal_places = 2)	
    creacion_asi = models.DateTimeField()	
    actualizacion_asi = models.DateTimeField()
    