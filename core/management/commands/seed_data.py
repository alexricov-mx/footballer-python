from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import (
    Federacion, Liga, Temporada, Equipo, Jugador, Sede,
    EquipoTemporada, PlantillaJugador,
    Arbitro, Jornada, Partido  # Nuevos modelos
)
import random
from datetime import date, timedelta, datetime

class Command(BaseCommand):
    help = 'Crea datos de prueba para la aplicación, incluyendo Liga MX y MLS.'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self._clean_db()
        self.stdout.write("Creando datos de prueba...")

        # Creación en orden de dependencia
        federaciones = self._create_federaciones()
        ligas = self._create_ligas(federaciones)
        temporadas = self._create_temporadas(ligas)
        sedes = self._create_sedes()
        arbitros = self._create_arbitros() # Nuevo
        equipos = self._create_equipos(federaciones)
        jugadores = self._create_jugadores()
        
        equipos_temporada = self._create_equipos_temporada(temporadas, equipos, sedes)
        self._create_plantillas(equipos_temporada, jugadores)
        self._create_calendario(temporadas, arbitros) # Nuevo

        self.stdout.write(self.style.SUCCESS('¡Datos de prueba creados exitosamente!'))

    def _clean_db(self):
        self.stdout.write("Limpiando la base de datos...")
        # Orden de eliminación inverso a la creación para respetar las dependencias
        Partido.objects.all().delete()
        Jornada.objects.all().delete()
        Arbitro.objects.all().delete()
        PlantillaJugador.objects.all().delete()
        EquipoTemporada.objects.all().delete()
        Jugador.objects.all().delete()
        Equipo.objects.all().delete()
        Sede.objects.all().delete()
        Temporada.objects.all().delete()
        Liga.objects.all().delete()
        Federacion.objects.all().delete()

    def _create_federaciones(self):
        self.stdout.write("Creando Federaciones...")
        return {
            'uefa': Federacion.objects.create(nombre='UEFA', activa=True),
            'conmebol': Federacion.objects.create(nombre='CONMEBOL', activa=True),
            'concacaf': Federacion.objects.create(nombre='CONCACAF', activa=True),
        }

    def _create_ligas(self, federaciones):
        self.stdout.write("Creando Ligas...")
        return {
            'laliga': Liga.objects.create(nombre='La Liga', federacion=federaciones['uefa'], activa=True),
            'arg': Liga.objects.create(nombre='Liga Profesional', federacion=federaciones['conmebol'], activa=True),
            'mx': Liga.objects.create(nombre='Liga MX', federacion=federaciones['concacaf'], activa=True),
            'mls': Liga.objects.create(nombre='MLS', federacion=federaciones['concacaf'], activa=True),
        }

    def _create_temporadas(self, ligas):
        self.stdout.write("Creando Temporadas...")
        return {
            '2425_laliga': Temporada.objects.create(
                liga=ligas['laliga'], nombre='2024-2025', estado=Temporada.EstadoTemporada.PLANEADA,
                modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA, fecha_inicio_propuesta=date(2024, 8, 16)
            ),
            '2024_arg': Temporada.objects.create(
                liga=ligas['arg'], nombre='2024', estado=Temporada.EstadoTemporada.ACTIVA,
                modalidad=Temporada.ModalidadCalendario.UNA_VUELTA, fecha_inicio_propuesta=date(2024, 1, 28)
            ),
            '2024_mls': Temporada.objects.create(
                liga=ligas['mls'], nombre='2024', estado=Temporada.EstadoTemporada.ACTIVA,
                modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA, fecha_inicio_propuesta=date(2024, 2, 21)
            ),
            'ap24_mx': Temporada.objects.create(
                liga=ligas['mx'], nombre='Apertura 2024', estado=Temporada.EstadoTemporada.ACTIVA,
                modalidad=Temporada.ModalidadCalendario.UNA_VUELTA, fecha_inicio_propuesta=date(2024, 7, 5)
            ),
        }

    def _create_sedes(self):
        self.stdout.write("Creando Sedes...")
        sedes_data = {
            'bernabeu': ('Santiago Bernabéu', 'Madrid', 'Av. de Concha Espina, 1'),
            'monumental': ('Estadio Monumental', 'Buenos Aires', 'Av. Pres. Figueroa Alcorta 7597'),
            'dignity': ('Dignity Health Sports Park', 'Carson', '18400 Avalon Blvd'),
            'chase': ('Chase Stadium', 'Fort Lauderdale', '1350 NW 55th St'),
            'ciudad_deportes': ('Estadio Ciudad de los Deportes', 'Ciudad de México', 'C. Indiana 255'),
            'jalisco': ('Estadio Jalisco', 'Guadalajara', 'C. 7 Colinas 1772'),
            'alfonso_lastras': ('Estadio Alfonso Lastras Ramírez', 'San Luis Potosí', 'C. Zenith 105'),
            'olimpico_juarez': ('Estadio Olímpico Benito Juárez', 'Ciudad Juárez', 'Av. Heroico Colegio Militar s/n'),
            'akron': ('Estadio Akron', 'Zapopan', 'C. Cto. JVC 2800'),
            'leon': ('Estadio León', 'León', 'Blvd. Adolfo López Mateos 1810'),
            'el_encanto': ('Estadio El Encanto', 'Mazatlán', 'Av. Múnich s/n'),
            'bbva': ('Estadio BBVA', 'Guadalupe', 'Av. Pablo Livas 2011'),
            'victoria': ('Estadio Victoria', 'Aguascalientes', 'C. Manuel Zavala Madrigal 101'),
            'hidalgo': ('Estadio Hidalgo', 'Pachuca', 'Blvd. Felipe Ángeles s/n'),
            'cuauhtemoc': ('Estadio Cuauhtémoc', 'Puebla', 'Calz. Ignacio Zaragoza 666'),
            'corregidora': ('Estadio Corregidora', 'Querétaro', 'Av. de las Torres s/n'),
            'tsm_corona': ('Estadio TSM Corona', 'Torreón', 'Carretera Torreón - San Pedro km 7'),
            'universitario': ('Estadio Universitario', 'San Nicolás de los Garza', 'C. Pedro de Alba s/n'),
            'caliente': ('Estadio Caliente', 'Tijuana', 'Blvd. Agua Caliente 12027'),
            'nemesio_diez': ('Estadio Nemesio Díez', 'Toluca', 'Av. Constituyentes Pte. 1000'),
            'olimpico_universitario': ('Estadio Olímpico Universitario', 'Ciudad de México', 'Av. de los Insurgentes Sur s/n'),
        }
        sedes = {}
        for key, (nombre, ciudad, direccion) in sedes_data.items():
            sedes[key] = Sede.objects.create(nombre=nombre, ciudad=ciudad, direccion=direccion, activa=True)
        return sedes

    def _create_arbitros(self):
        self.stdout.write("Creando Árbitros...")
        nombres = ['Adonai', 'César Arturo', 'Marco Antonio', 'Fernando', 'Luis Enrique', 'Óscar']
        apellidos = ['Escobedo', 'Ramos', 'Ortiz', 'Guerrero', 'Santander', 'Macías']
        arbitros = []
        for i in range(len(nombres)):
            arbitros.append(Arbitro.objects.create(
                nombre=nombres[i],
                apellido_paterno=apellidos[i],
                fecha_nacimiento=date(random.randint(1975, 1990), random.randint(1, 12), random.randint(1, 28)),
                activo=True
            ))
        return arbitros

    def _create_equipos(self, federaciones):
        self.stdout.write("Creando Equipos...")
        equipos_data = {
            'rm': ('Real Madrid', federaciones['uefa']),
            'river': ('River Plate', federaciones['conmebol']),
            'galaxy': ('LA Galaxy', federaciones['concacaf']),
            'miami': ('Inter Miami CF', federaciones['concacaf']),
            'america': ('Club América', federaciones['concacaf']),
            'atlas': ('Atlas', federaciones['concacaf']),
            'san_luis': ('Atlético de San Luis', federaciones['concacaf']),
            'cruz_azul': ('Cruz Azul', federaciones['concacaf']),
            'juarez': ('FC Juárez', federaciones['concacaf']),
            'chivas': ('Guadalajara', federaciones['concacaf']),
            'leon': ('León', federaciones['concacaf']),
            'mazatlan': ('Mazatlán FC', federaciones['concacaf']),
            'monterrey': ('Monterrey', federaciones['concacaf']),
            'necaxa': ('Necaxa', federaciones['concacaf']),
            'pachuca': ('Pachuca', federaciones['concacaf']),
            'puebla': ('Puebla', federaciones['concacaf']),
            'queretaro': ('Querétaro', federaciones['concacaf']),
            'santos': ('Santos Laguna', federaciones['concacaf']),
            'tigres': ('Tigres UANL', federaciones['concacaf']),
            'tijuana': ('Club Tijuana', federaciones['concacaf']),
            'toluca': ('Toluca', federaciones['concacaf']),
            'pumas': ('UNAM', federaciones['concacaf']),
        }
        equipos = {}
        for key, (nombre, federacion) in equipos_data.items():
            equipos[key] = Equipo.objects.create(nombre=nombre, federacion=federacion, activo=True)
        return equipos

    def _create_jugadores(self):
        self.stdout.write("Creando Jugadores...")
        nombres = ['Juan', 'Carlos', 'Luis', 'Miguel', 'Javier', 'Andrés', 'Leo', 'Cris', 'Ney', 'Kylian', 'Santiago', 'Julián', 'Diego', 'Héctor', 'Raúl']
        apellidos = ['García', 'Rodríguez', 'Messi', 'Ronaldo', 'Martínez', 'Hernández', 'López', 'Pérez', 'Mbappé', 'Giménez', 'Quiñones', 'Valdés', 'Herrera', 'Jiménez']
        posiciones = [p[0] for p in Jugador.PosicionJugador.choices]
        
        jugadores = []
        for _ in range(500):
            jugadores.append(Jugador.objects.create(
                nombre=random.choice(nombres),
                apellido=random.choice(apellidos),
                fecha_nacimiento=date(random.randint(1990, 2005), random.randint(1, 12), random.randint(1, 28)),
                posicion=random.choice(posiciones),
                activo=True
            ))
        return jugadores

    def _create_equipos_temporada(self, temporadas, equipos, sedes):
        self.stdout.write("Asociando Equipos a Temporadas...")
        asociaciones = [
            (equipos['rm'], temporadas['2425_laliga'], sedes['bernabeu']),
            (equipos['river'], temporadas['2024_arg'], sedes['monumental']),
            (equipos['galaxy'], temporadas['2024_mls'], sedes['dignity']),
            (equipos['miami'], temporadas['2024_mls'], sedes['chase']),
            (equipos['america'], temporadas['ap24_mx'], sedes['ciudad_deportes']),
            (equipos['atlas'], temporadas['ap24_mx'], sedes['jalisco']),
            (equipos['san_luis'], temporadas['ap24_mx'], sedes['alfonso_lastras']),
            (equipos['cruz_azul'], temporadas['ap24_mx'], sedes['ciudad_deportes']),
            (equipos['juarez'], temporadas['ap24_mx'], sedes['olimpico_juarez']),
            (equipos['chivas'], temporadas['ap24_mx'], sedes['akron']),
            (equipos['leon'], temporadas['ap24_mx'], sedes['leon']),
            (equipos['mazatlan'], temporadas['ap24_mx'], sedes['el_encanto']),
            (equipos['monterrey'], temporadas['ap24_mx'], sedes['bbva']),
            (equipos['necaxa'], temporadas['ap24_mx'], sedes['victoria']),
            (equipos['pachuca'], temporadas['ap24_mx'], sedes['hidalgo']),
            (equipos['puebla'], temporadas['ap24_mx'], sedes['cuauhtemoc']),
            (equipos['queretaro'], temporadas['ap24_mx'], sedes['corregidora']),
            (equipos['santos'], temporadas['ap24_mx'], sedes['tsm_corona']),
            (equipos['tigres'], temporadas['ap24_mx'], sedes['universitario']),
            (equipos['tijuana'], temporadas['ap24_mx'], sedes['caliente']),
            (equipos['toluca'], temporadas['ap24_mx'], sedes['nemesio_diez']),
            (equipos['pumas'], temporadas['ap24_mx'], sedes['olimpico_universitario']),
        ]
        
        equipos_temporada = []
        for equipo, temporada, sede in asociaciones:
            equipos_temporada.append(
                EquipoTemporada.objects.create(equipo=equipo, temporada=temporada, sede=sede)
            )
        return equipos_temporada

    def _create_plantillas(self, equipos_temporada, jugadores):
        self.stdout.write("Creando Plantillas...")
        jugadores_disponibles = list(jugadores)
        
        for et in equipos_temporada:
            dorsales_usados = set()
            for _ in range(random.randint(18, 25)):
                if not jugadores_disponibles: break
                
                dorsal = random.randint(1, 99)
                while dorsal in dorsales_usados:
                    dorsal = random.randint(1, 99)
                dorsales_usados.add(dorsal)

                jugador_a_asignar = jugadores_disponibles.pop(random.randint(0, len(jugadores_disponibles) - 1))
                
                PlantillaJugador.objects.create(
                    equipo_temporada=et,
                    jugador=jugador_a_asignar,
                    dorsal=dorsal
                )

    def _create_calendario(self, temporadas, arbitros):
        self.stdout.write("Creando Calendario para Liga MX...")
        temporada_mx = temporadas['ap24_mx']
        equipos_mx = list(EquipoTemporada.objects.filter(temporada=temporada_mx))
        
        if len(equipos_mx) < 2:
            self.stdout.write("No hay suficientes equipos en la Liga MX para crear partidos.")
            return

        fecha_inicio = temporada_mx.fecha_inicio_propuesta or date.today()

        for i in range(1, 18): # 17 Jornadas
            jornada = Jornada.objects.create(temporada=temporada_mx, numero=i)
            self.stdout.write(f"  Creando Jornada {i}...")
            
            random.shuffle(equipos_mx)
            equipos_jornada = list(equipos_mx) # Copia para manipular

            for _ in range(len(equipos_mx) // 2): # 9 partidos por jornada
                if len(equipos_jornada) < 2: break
                
                equipo_local = equipos_jornada.pop()
                equipo_visitante = equipos_jornada.pop()

                # Asignar fecha y hora al partido (ej. cada fin de semana)
                dias_partido = ((i - 1) * 7) + random.randint(1, 3) # Simula partidos en fin de semana
                hora_partido = random.choice([17, 19, 21])
                minuto_partido = random.choice([0, 30])
                fecha_partido = fecha_inicio + timedelta(days=dias_partido)
                fecha_hora_partido = datetime.combine(fecha_partido, datetime.min.time()).replace(hour=hora_partido, minute=minuto_partido)

                Partido.objects.create(
                    jornada=jornada,
                    equipo_local=equipo_local,
                    equipo_visitante=equipo_visitante,
                    sede=equipo_local.sede, # El equipo local juega en su sede
                    arbitro=random.choice(arbitros),
                    fecha_hora=fecha_hora_partido,
                    estado=Partido.EstadoPartido.PROGRAMADO
                )

