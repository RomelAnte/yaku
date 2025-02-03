from django.db import models
from Aplicaciones.configuracion.models import Ruta
from Aplicaciones.tarifas.models import Tarifa
from Aplicaciones.facturacion.models import Consumo
#from Aplicaciones.socios.models import Historial_propietario

# Create your models here.
class Medidor (models.Model):
    id_med = models.AutoField(primary_key=True)
    fk_id_rut = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fk_id_tar = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    numero_med = models.CharField(max_length=50)
    serie_med = models.CharField(max_length=100)
    marca_med = models.CharField(max_length=100)	
    observacion_med = models.TextField()
    estado_med = models.CharField(max_length=25)
    foto_med = models.CharField(max_length=500)
    creacion_med = models.DateTimeField()
    actualizacion_med = models.DateTimeField()
    lectura_inicial_med = models.DecimalField(max_digits=10, decimal_places=2)
    
class Lectura(models.Model):
    id_lec = models.AutoField(primary_key=True)
    anio_lec = models.IntegerField()
    mes_lec = models.CharField(max_length=25)	
    estado_lec = models.CharField(max_length=50) 	
    lectura_anterior_lec = models.DecimalField(max_digits=10, decimal_places=2)
    lectura_actual_lec = models.DecimalField(max_digits=10, decimal_places=2)	
    fecha_creacion_lec = models.DateTimeField()
    fecha_actualizacion_lec = models.DateTimeField()
    #fk_id_his = models.ForeignKey(Historial_propietario, on_delete=models.CASCADE)
    fk_id_consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE)