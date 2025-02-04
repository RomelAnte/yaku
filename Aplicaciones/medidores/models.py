from django.db import models
from Aplicaciones.configuracion.models import Ruta
from Aplicaciones.tarifas.models import Tarifa

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

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'medidor'  # Nombre exacto de la tabla en MySQL
    
class Consumo (models.Model):
    id_consumo = models.AutoField(primary_key=True)
    anio_consumo = models.IntegerField()	
    mes_consumo = models.CharField(max_length = 20)	
    estado_consumo = models.CharField(max_length = 20)	
    fecha_creacion_consumo = models.DateTimeField()	
    fecha_actualizacion_consumo = models.DateTimeField()	
    numero_mes_consumo = models.IntegerField()	
    fecha_vencimiento_consumo = models.DateField()    

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'consumo'  # Nombre exacto de la tabla en MySQL
    
