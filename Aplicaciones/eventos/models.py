from django.db import models
# Create your models here.

class TipoEvento(models.Model):
    id_te = models.AutoField(primary_key=True)	
    nombre_te = models.CharField(max_length = 150)	
    estado_te = models.CharField(max_length = 50) 
    creacion_te = models.DateTimeField()	
    actualizacion_te = models.DateTimeField()

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'tipo_evento'  # Nombre exacto de la tabla en MySQL
    
class Evento(models.Model):
    id_eve = models.AutoField(primary_key=True)
    descripcion_eve = models.TextField()
    fecha_hora_eve = models.DateTimeField()
    lugar_eve = models.CharField(max_length = 250)
    fk_id_te = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'evento'  # Nombre exacto de la tabla en MySQL