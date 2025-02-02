from django.db import models
from Aplicaciones.usuarios.models import Usuario
from Aplicaciones.medidores.models import Medidor

# Create your models here.
class Socio (models.Model):
    id_soc = models.AutoField(primary_key=True)
    tipo_soc = models.CharField(max_length=50)
    identificacion_soc = models.CharField(max_length=13)	
    primer_apellido_soc = models.CharField(max_length=50)	
    segundo_apellido_soc = models.CharField(max_length=50) 	
    nombres_soc = models.CharField(max_length=50)	
    email_soc = models.CharField(max_length=100)	
    foto_soc = models.CharField(max_length=100)	
    telefono_soc = models.CharField(max_length=13) 	
    direccion_soc = models.CharField(max_length=200)	
    fecha_nacimiento_soc = models.DateField()	
    discapacidad_soc = models.BooleanField() 	
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado_soc = models.BooleanField()
    
class Historial_propietario (models.Model):
    id_his = models.AutoField(primary_key=True)	
    fk_id_med = models.ForeignKey(Medidor, on_delete=models.CASCADE)	
    fk_id_soc = models.ForeignKey(Socio, on_delete=models.CASCADE)	
    actualizacion_his = models.DateTimeField()
    estado_his = models.CharField(max_length=50)
    observacion_his = models.TextField()
    fecha_cambio_his = models.DateTimeField()
    creacion_his = models.DateTimeField()
    propietario_actual_his	= models.CharField(max_length=15)