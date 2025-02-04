# Generated by Django 4.2.7 on 2025-02-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_det', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_det', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detalle_det', models.TextField()),
                ('valor_unitario_det', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal_det', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva_det', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historial_propietario',
            fields=[
                ('id_his', models.AutoField(primary_key=True, serialize=False)),
                ('actualizacion_his', models.DateTimeField()),
                ('estado_his', models.CharField(max_length=50)),
                ('observacion_his', models.TextField()),
                ('fecha_cambio_his', models.DateTimeField()),
                ('creacion_his', models.DateTimeField()),
                ('propietario_actual_his', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'historial_propietario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id_lec', models.AutoField(primary_key=True, serialize=False)),
                ('anio_lec', models.IntegerField()),
                ('mes_lec', models.CharField(max_length=25)),
                ('estado_lec', models.CharField(max_length=50)),
                ('lectura_anterior_lec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lectura_actual_lec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion_lec', models.DateTimeField()),
                ('fecha_actualizacion_lec', models.DateTimeField()),
            ],
            options={
                'db_table': 'lectura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recaudacion',
            fields=[
                ('id_rec', models.AutoField(primary_key=True, serialize=False)),
                ('numero_factura_rec', models.CharField(max_length=250)),
                ('numero_autorizacion_rec', models.CharField(max_length=500)),
                ('fecha_hora_autorizacion_rec', models.DateTimeField()),
                ('ambiente_rec', models.CharField(max_length=50)),
                ('emision_rev', models.CharField(max_length=50)),
                ('clave_acceso_rec', models.CharField(max_length=500)),
                ('email_rec', models.CharField(max_length=500)),
                ('observacion_rec', models.CharField(max_length=500)),
                ('nombre_rec', models.CharField(max_length=500)),
                ('identificacion_rec', models.CharField(max_length=15)),
                ('direccion_rec', models.CharField(max_length=500)),
                ('estado_rec', models.CharField(max_length=50)),
                ('fecha_emision_rec', models.DateTimeField()),
                ('fecha_creacion_rec', models.DateTimeField()),
                ('fecha_actualizacion_rec', models.DateTimeField()),
            ],
            options={
                'db_table': 'recaudacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id_soc', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_soc', models.CharField(max_length=50)),
                ('identificacion_soc', models.CharField(max_length=13)),
                ('primer_apellido_soc', models.CharField(max_length=50)),
                ('segundo_apellido_soc', models.CharField(max_length=50)),
                ('nombres_soc', models.CharField(max_length=50)),
                ('email_soc', models.CharField(max_length=100)),
                ('foto_soc', models.CharField(max_length=100)),
                ('telefono_soc', models.CharField(max_length=13)),
                ('direccion_soc', models.CharField(max_length=200)),
                ('fecha_nacimiento_soc', models.DateField()),
                ('discapacidad_soc', models.BooleanField()),
                ('estado_soc', models.BooleanField()),
            ],
            options={
                'db_table': 'socio',
                'managed': False,
            },
        ),
    ]
