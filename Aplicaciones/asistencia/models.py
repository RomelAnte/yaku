from django.db import models

# Create your models here.
class Asistencia(models.Model):
    id_asi 	= models.AutoField(primary_key=True)
    
    fk_id_eve 	fk_id_soc 	tipo_asi 	valor_asi 	atraso_asi 	valor_atraso_asi 	creacion_asi 	actualizacion_asi 	
    