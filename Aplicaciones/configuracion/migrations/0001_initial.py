# Generated by Django 4.2.7 on 2025-02-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id_con', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_con', models.CharField(max_length=250)),
                ('ruc_con', models.CharField(max_length=13)),
                ('logo_con', models.FileField(max_length=200, upload_to='configuraciones/')),
                ('telefono_con', models.CharField(max_length=10)),
                ('direccion_con', models.CharField(max_length=50)),
                ('email_con', models.CharField(max_length=50)),
                ('servidor_con', models.CharField(max_length=50)),
                ('puerto_con', models.CharField(max_length=50)),
                ('password_con', models.CharField(max_length=50)),
                ('creacion_con', models.DateTimeField()),
                ('actualizacion_con', models.DateTimeField()),
                ('anio_inicial_con', models.IntegerField()),
                ('mes_inicial_con', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'configuracion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id_rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rut', models.CharField(max_length=500)),
                ('descripcion_rut', models.TextField()),
                ('estado_rut', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'ruta',
                'managed': False,
            },
        ),
    ]
