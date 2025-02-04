from django.db import models

# Create your models here.
class Perfil (models.Model):
    id_per = models.AutoField(primary_key=True)	
    nombre_per = models.CharField(max_length=50)	
    descripcion_per = models.TextField()	
    estado_per = models.CharField(max_length=50) 
    creacion_per = models.DateTimeField()	
    actualizacion_per = models.DateTimeField() 	

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'perfil'  # Nombre exacto de la tabla en MySQL

class Usuario (models.Model):
    id_usu = models.AutoField(primary_key=True)	
    apellido_usu = models.CharField(max_length=150) 	
    nombre_usu = models.CharField(max_length=150) 	
    email_usu = models.CharField(max_length=150) 	
    password_usu = models.CharField(max_length=500) 	
    estado_usu = models.CharField(max_length=50) 	
    fk_id_per = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        managed = False  # Django no tocará la tabla
        db_table = 'usuario'  # Nombre exacto de la tabla en MySQL
    
