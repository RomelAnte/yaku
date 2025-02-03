from django.db import models
#from Aplicaciones.medidores.models import Lectura
#from Aplicaciones.socios.models import Socio

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
    #fk_id_soc = models.ForeignKey(Socio, on_delete=models.CASCADE)	
    nombre_rec = models.CharField(max_length=500)	
    identificacion_rec = models.CharField(max_length=15) 	
    direccion_rec = models.CharField(max_length=500)	
    estado_rec = models.CharField(max_length=50)	
    fecha_emision_rec = models.DateTimeField() 	
    fecha_creacion_rec = models.DateTimeField()
    fecha_actualizacion_rec = models.DateTimeField()
    
class Impuesto (models.Model):
    id_imp = models.AutoField(primary_key=True)
    nombre_imp = models.CharField(max_length=100)
    descripcion_imp = models.TextField()
    porcentaje_imp = models.DecimalField(max_digits=10, decimal_places=2)
    retencion_imp = models.DecimalField(max_digits=10, decimal_places=2)
    estado_imp = models.CharField(max_length=50)
    creacion_imp = models.DateTimeField()
    actualizacion_imp = models.DateTimeField()
    
class Detalle(models.Model):
    id_det = models.AutoField(primary_key=True)
    #fk_id_lec = models.ForeignKey(Lectura, on_delete=models.CASCADE)
    fk_id_rec = models.ForeignKey(Recaudacion, on_delete=models.CASCADE)
    cantidad_det = models.DecimalField(max_digits=10, decimal_places=2)
    detalle_det = models.TextField()
    valor_unitario_det = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_det = models.DecimalField(max_digits=10, decimal_places=2)
    iva_det = models.DecimalField(max_digits=10, decimal_places=2)
