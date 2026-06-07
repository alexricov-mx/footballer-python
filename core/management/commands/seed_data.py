from django.core.management.base import BaseCommand
from core.models import Federacion, Liga, Temporada, Equipo, Jugador, Sede
import random
from datetime import date

class Command(BaseCommand):
    help = 'Crea datos de prueba para la aplicación'

    def handle(self, *args, **kwargs):
        self.stdout.write("Limpiando la base de datos...")
        Jugador.objects.all().delete()
        Equipo.objects.all().delete()
        Sede.objects.all().delete()
        Temporada.objects.all().delete()
        Liga.objects.all().delete()
        Federacion.objects.all().delete()

        self.stdout.write("Creando datos de prueba...")

        # Federaciones
        federacion_uefa = Federacion.objects.create(nombre='UEFA', activa=True)
        federacion_conmebol = Federacion.objects.create(nombre='CONMEBOL', activa=True)

        # Ligas
        liga_esp = Liga.objects.create(nombre='La Liga', federacion=federacion_uefa, activa=True)
        liga_eng = Liga.objects.create(nombre='Premier League', federacion=federacion_uefa, activa=True)
        liga_arg = Liga.objects.create(nombre='Liga Profesional', federacion=federacion_conmebol, activa=True)

        # Temporadas
        temporada_2324_laliga = Temporada.objects.create(
            liga=liga_esp,
            nombre='2023-2024',
            estado=Temporada.EstadoTemporada.FINALIZADA,
            modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA,
            fecha_inicio_propuesta=date(2023, 8, 11)
        )
        temporada_2425_laliga = Temporada.objects.create(
            liga=liga_esp,
            nombre='2024-2025',
            estado=Temporada.EstadoTemporada.PLANEADA,
            modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA,
            fecha_inicio_propuesta=date(2024, 8, 16)
        )
        temporada_2024_arg = Temporada.objects.create(
            liga=liga_arg,
            nombre='2024',
            estado=Temporada.EstadoTemporada.ACTIVA,
            modalidad=Temporada.ModalidadCalendario.UNA_VUELTA,
            fecha_inicio_propuesta=date(2024, 1, 28)
        )

        # Sedes
        sede_bernabeu = Sede.objects.create(nombre='Santiago Bernabéu', ciudad='Madrid', direccion='Av. de Concha Espina, 1', activa=True)
        sede_campnou = Sede.objects.create(nombre='Camp Nou', ciudad='Barcelona', direccion='C. de Arístides Maillol, 12', activa=True)
        sede_monumental = Sede.objects.create(nombre='Estadio Monumental', ciudad='Buenos Aires', direccion='Av. Pres. Figueroa Alcorta 7597', activa=True)

        # Equipos
        equipo_rm = Equipo.objects.create(nombre='Real Madrid', activo=True)
        equipo_barca = Equipo.objects.create(nombre='FC Barcelona', activo=True)
        equipo_river = Equipo.objects.create(nombre='River Plate', activo=True)

        # Jugadores
        nombres = ['Juan', 'Carlos', 'Luis', 'Miguel', 'Javier', 'Andrés']
        apellidos = ['García', 'Rodríguez', 'Martínez', 'Hernández', 'López', 'Pérez']

        for equipo in [equipo_rm, equipo_barca, equipo_river]:
            for i in range(15):
                Jugador.objects.create(
                    equipo=equipo,
                    nombre=random.choice(nombres),
                    apellido=random.choice(apellidos),
                    activo=True
                )

        self.stdout.write(self.style.SUCCESS('¡Datos de prueba creados exitosamente!'))
