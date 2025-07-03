from django.db import models

# Create your models here.

# Modelo de hotel

class Hotel(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    ubicacion = models.CharField(max_length=50)
    servicios = models.CharField(max_length=150, null=True)
    categoria = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=20)
    cantidad_habitaciones = models.IntegerField()
    url_info = models.URLField(null=True, max_length=150)

    def __str__(self):
        return f"{self.nombre} , {self.ubicacion} , {self.telefono}"


#  Modelo de habitaciones 
class Habitacion(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='habitaciones'
    )
    titulo = models.CharField(max_length=50, verbose_name="titulo")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_personas = models.IntegerField()
    descripcion = models.TextField(null=True)
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.titulo} , ${self.precio}"


# Modelo de reserva
class Reserva(models.Model):
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_entrada = models.DateField(verbose_name="Fecha de entrada")
    fecha_salida = models.DateField(verbose_name="Fecha de salida")
    cantidad_personas = models.IntegerField()

    def __str__(self):
        return f"Reserva de {self.nombre} ({self.fecha_entrada} - {self.fecha_salida})"