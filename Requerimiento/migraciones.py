# Migraciones de Modelos de Django para Footballer MVP

"""
Este archivo contiene la definicion de los modelos de Django basados en el Modelo ER objetivo v06.
Estos modelos representan la estructura de la base de datos para la aplicacion Footballer.
"""

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

# Incremento 2: Participacion y plantillas

class LigaEquipo(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('liga', 'equipo')

    def __str__(self):
        return f'{self.equipo.nombre} en {self.liga.nombre}'

class TemporadaEquipo(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('temporada', 'equipo')

    def __str__(self):
        return f'{self.equipo.nombre} en {self.temporada.nombre}'

# Incremento 3: Arbitros y permisos

class Arbitro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    es_arbitro_general = models.BooleanField(default=False, help_text="Permite capturar resultados de cualquier partido.")
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Incremento 4: Calendario

class Jornada(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name='jornadas')
    numero = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('temporada', 'numero')
        ordering = ['numero']

    def __str__(self):
        return f'Jornada {self.numero} - {self.temporada.nombre}'

class Partido(models.Model):
    class EstadoPartido(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        PROGRAMADO = 'programado', 'Programado'
        EN_CAPTURA = 'en_captura', 'En Captura'
        JUGADO = 'jugado', 'Jugado'
        SUSPENDIDO = 'suspendido', 'Suspendido'
        CANCELADO = 'cancelado', 'Cancelado'
        REPROGRAMADO = 'reprogramado', 'Reprogramado'

    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name='partidos')
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoPartido.choices, default=EstadoPartido.PENDIENTE)
    arbitro_asignado = models.ForeignKey(Arbitro, on_delete=models.SET_NULL, null=True, blank=True)
    goles_local = models.PositiveIntegerField(null=True, blank=True)
    goles_visitante = models.PositiveIntegerField(null=True, blank=True)
    usuario_captura = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='partidos_capturados')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.local.nombre} vs {self.visitante.nombre} - {self.jornada}'

# Incremento 5: Operacion de partidos

class EventoPartido(models.Model):
    class TipoEvento(models.TextChoices):
        GOL = 'gol', 'Gol'
        TARJETA_AMARILLA = 'tarjeta_amarilla', 'Tarjeta Amarilla'
        TARJETA_ROJA = 'tarjeta_roja', 'Tarjeta Roja'

    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='eventos')
    tipo = models.CharField(max_length=20, choices=TipoEvento.choices)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    minuto = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} de {self.jugador} en minuto {self.minuto}'
