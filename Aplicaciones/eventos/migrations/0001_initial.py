# Generated by Django 4.2.7 on 2025-02-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_eve', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_eve', models.TextField()),
                ('fecha_hora_eve', models.DateTimeField()),
                ('lugar_eve', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id_te', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_te', models.CharField(max_length=150)),
                ('estado_te', models.CharField(max_length=50)),
                ('creacion_te', models.DateTimeField()),
                ('actualizacion_te', models.DateTimeField()),
            ],
            options={
                'db_table': 'tipo_evento',
                'managed': False,
            },
        ),
    ]
