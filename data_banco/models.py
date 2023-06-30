from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    cuit_cuil = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Habitacion(models.Model):
    habitacion_id = models.IntegerField(primary_key=True)
    numero_habitacion = models.IntegerField()
    capacidad = models.IntegerField()
    numero_camas = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Habitación {self.numero_habitacion}"

class Reserva(models.Model):
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva - Entrada: {self.fecha_entrada}, Salida: {self.fecha_salida}"
