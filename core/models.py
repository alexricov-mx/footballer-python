from django.db import models
from django.contrib.auth.models import User

# Incremento 1: Base administrativa

class Federacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Liga(models.Model):
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE, related_name='ligas')
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('federacion', 'nombre')

    def __str__(self):
        return f'{self.nombre} ({self.federacion.nombre})'

class Temporada(models.Model):
    class EstadoTemporada(models.TextChoices):
        PLANEADA = 'planeada', 'Planeada'
        ACTIVA = 'activa', 'Activa'
        FINALIZADA = 'finalizada', 'Finalizada'
        CANCELADA = 'cancelada', 'Cancelada'

    class ModalidadCalendario(models.TextChoices):
        UNA_VUELTA = 'una_vuelta', 'Una Vuelta'
        DOBLE_VUELTA = 'doble_vuelta', 'Doble Vuelta'

    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='temporadas')
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=EstadoTemporada.choices, default=EstadoTemporada.PLANEADA)
    modalidad = models.CharField(max_length=20, choices=ModalidadCalendario.choices)
    fecha_inicio_propuesta = models.DateField(null=True, blank=True)
    dias_partido = models.CharField(max_length=50, null=True, blank=True, help_text="Ej: 'sabado,domingo'")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} - {self.liga.nombre}'

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    referencia = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='sedes/', blank=True, null=True)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
