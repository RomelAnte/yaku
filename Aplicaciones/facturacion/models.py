from django.db import models

# Create your models here.
class Consumo (models.Model):
    id_consumo = models.AutoField(primary_key=True)
    anio_consumo = models.IntegerField()	
    mes_consumo = models.CharField(max_length = 20)	
    estado_consumo = models.CharField(max_length = 20)	
    fecha_creacion_consumo = models.DateTimeField()	
    fecha_actualizacion_consumo = models.DateTimeField()	
    numero_mes_consumo = models.IntegerField()	
    fecha_vencimiento_consumo = models.DateField()
    
