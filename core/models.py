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
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE, related_name='equipos')
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

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

class Jugador(models.Model):
    class PosicionJugador(models.TextChoices):
        PORTERO = 'portero', 'Portero'
        DEFENSA = 'defensa', 'Defensa'
        MEDIOCAMPISTA = 'mediocampista', 'Mediocampista'
        DELANTERO = 'delantero', 'Delantero'

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    posicion = models.CharField(max_length=20, choices=PosicionJugador.choices, null=True)
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class EquipoTemporada(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name='equipos_participantes')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='participaciones')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipos_como_sede')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('temporada', 'equipo')

    def __str__(self):
        return f'{self.equipo.nombre} en {self.temporada.nombre}'

class PlantillaJugador(models.Model):
    equipo_temporada = models.ForeignKey(EquipoTemporada, on_delete=models.CASCADE, related_name='plantilla')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='historial_equipos')
    dorsal = models.PositiveIntegerField()
    posicion_secundaria = models.CharField(max_length=20, choices=Jugador.PosicionJugador.choices, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('equipo_temporada', 'jugador')
        ordering = ['dorsal']

    def __str__(self):
        return f'{self.jugador} - {self.equipo_temporada.equipo.nombre} ({self.dorsal})'

# Incremento 3: Calendarios y Partidos

class Arbitro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno}'

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
        FINALIZADO = 'finalizado', 'Finalizado'
        CANCELADO = 'cancelado', 'Cancelado'
        SUSPENDIDO = 'suspendido', 'Suspendido'

    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name='partidos')
    equipo_local = models.ForeignKey(EquipoTemporada, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(EquipoTemporada, on_delete=models.CASCADE, related_name='partidos_visitante')
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, related_name='partidos')
    arbitro = models.ForeignKey(Arbitro, on_delete=models.SET_NULL, null=True, blank=True, related_name='partidos_arbitrados')
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoPartido.choices, default=EstadoPartido.PENDIENTE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.equipo_local.equipo} vs {self.equipo_visitante.equipo} - {self.jornada}'
