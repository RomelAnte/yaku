from django.db import models

# Create your models here.       
class Impuesto (models.Model):
    id_imp = models.AutoField(primary_key=True)
    nombre_imp = models.CharField(max_length=100)
    descripcion_imp = models.TextField()
    porcentaje_imp = models.DecimalField(max_digits=10, decimal_places=2)
    retencion_imp = models.DecimalField(max_digits=10, decimal_places=2)
    estado_imp = models.CharField(max_length=50)
    creacion_imp = models.DateTimeField()
    actualizacion_imp = models.DateTimeField()
    
