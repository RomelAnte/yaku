from django.db import models
from Aplicaciones.usuarios.models import Usuario
from Aplicaciones.medidores.models import Medidor, Consumo

# Create your models here.
class Socio(models.Model):
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
    
class Historial_propietario(models.Model):
    id_his = models.AutoField(primary_key=True)	
    fk_id_med = models.ForeignKey(Medidor, on_delete=models.CASCADE)	
    fk_id_soc = models.ForeignKey(Socio, on_delete=models.CASCADE)	
    actualizacion_his = models.DateTimeField()
    estado_his = models.CharField(max_length=50)
    observacion_his = models.TextField()
    fecha_cambio_his = models.DateTimeField()
    creacion_his = models.DateTimeField()
    propietario_actual_his	= models.CharField(max_length=15)
    
class Lectura(models.Model):
    id_lec = models.AutoField(primary_key=True)
    anio_lec = models.IntegerField()
    mes_lec = models.CharField(max_length=25)	
    estado_lec = models.CharField(max_length=50) 	
    lectura_anterior_lec = models.DecimalField(max_digits=10, decimal_places=2)
    lectura_actual_lec = models.DecimalField(max_digits=10, decimal_places=2)	
    fecha_creacion_lec = models.DateTimeField()
    fecha_actualizacion_lec = models.DateTimeField()
    fk_id_his = models.ForeignKey(Historial_propietario, on_delete=models.CASCADE)
    fk_id_consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE)
    
class Recaudacion (models.Model):
    id_rec = models.AutoField(primary_key=True)	
    numero_factura_rec = models.CharField(max_length=250)	
    numero_autorizacion_rec = models.CharField(max_length=500)	
    fecha_hora_autorizacion_rec = models.DateTimeField()	
    ambiente_rec = models.CharField(max_length=50)	
    emision_rev = models.CharField(max_length=50)	
    clave_acceso_rec = models.CharField(max_length=500)	
    email_rec = models.CharField(max_length=500)	
    observacion_rec = models.CharField(max_length=500)	
    fk_id_soc = models.ForeignKey(Socio, on_delete=models.CASCADE)	
    nombre_rec = models.CharField(max_length=500)	
    identificacion_rec = models.CharField(max_length=15) 	
    direccion_rec = models.CharField(max_length=500)	
    estado_rec = models.CharField(max_length=50)	
    fecha_emision_rec = models.DateTimeField() 	
    fecha_creacion_rec = models.DateTimeField()
    fecha_actualizacion_rec = models.DateTimeField()
    
class Detalle(models.Model):
    id_det = models.AutoField(primary_key=True)
    fk_id_lec = models.ForeignKey(Lectura, on_delete=models.CASCADE)
    fk_id_rec = models.ForeignKey(Recaudacion, on_delete=models.CASCADE)
    cantidad_det = models.DecimalField(max_digits=10, decimal_places=2)
    detalle_det = models.TextField()
    valor_unitario_det = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_det = models.DecimalField(max_digits=10, decimal_places=2)
    iva_det = models.DecimalField(max_digits=10, decimal_places=2)
