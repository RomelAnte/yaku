from django.db import models

# Create your models here.
class Tarifa (models.Model):
    id_tar = models.AutoField(primary_key=True)
    nombre_tar = models.CharField(max_length=500)	
    descripcion_tar = models.TextField()	
    estado_tar = models.CharField(max_length=25) 	
    m3_maximo_tar = models.DecimalField(max_digits=10, decimal_places=2)	
    tarifa_basica_tar = models.DecimalField(max_digits=10, decimal_places=2)	
    tarifa_excedente_tar = models.DecimalField(max_digits=10, decimal_places=2)
    valor_mora_tar = models.DecimalField(max_digits=10, decimal_places=2)
    
class Excedente (models.Model):
    id_ex = models.AutoField(primary_key=True)
    id_tar = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    limite_minimo_ex = models.DecimalField(max_digits=10, decimal_places=2)
    limite_maximo_ex = models.DecimalField(max_digits=10, decimal_places=2)
    tarifa_ex = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion_ex = models.DateTimeField()
    fecha_creacion_ex = models.DateTimeField()