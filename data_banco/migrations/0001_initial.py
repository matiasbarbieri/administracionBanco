# Generated by Django 4.2.2 on 2023-06-29 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipo_documento', models.CharField(max_length=20)),
                ('numero_documento', models.CharField(max_length=20)),
                ('cuit_cuil', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('habitacion_id', models.IntegerField(primary_key=True, serialize=False)),
                ('numero_habitacion', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('numero_camas', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reserva_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('total_pagar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_banco.cliente')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_banco.habitacion')),
            ],
        ),
    ]