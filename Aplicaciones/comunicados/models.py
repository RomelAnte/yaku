from django.db import models

# Create your models here.
class Comunicado (models.Model):
    id_com = models.AutoField(primary_key=True)
    fecha_com = models.DateField()
    mensaje_com = models.CharField(max_length=200)
    actualizacion_com = models.DateTimeField()
    creacion_com = models.DateTimeField()
    
    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'comunicado'  # Nombre exacto de la tabla en MySQL
