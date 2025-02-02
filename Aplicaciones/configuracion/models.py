from django.db import models

# Create your models here.

class Configuracion(models.Model):
    id_con 	= models.AutoField(primary_key = True)
    nombre_con 	= models.CharField(max_length = 250)
    ruc_con = models.CharField(max_length = 13)	
    logo_con = models.CharField(max_length = 200)	
    telefono_con = models.CharField(max_length = 10) 	
    direccion_con = models.CharField(max_length = 50)	
    email_con = models.CharField(max_length = 50)	
    servidor_con = models.CharField(max_length = 50)
    puerto_con = models.CharField(max_length = 50)	
    password_con = models.CharField(max_length=50)	
    creacion_con = models.DateTimeField()	
    actualizacion_con = models.DateTimeField()	
    anio_inicial_con = models.IntegerField()	
    mes_inicial_con = models.CharField(max_length=25)
