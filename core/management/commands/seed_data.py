from django.core.management.base import BaseCommand
from core.models import (
    Federacion, Liga, Temporada, Equipo, Jugador, Sede,
    EquipoTemporada, PlantillaJugador
)
import random
from datetime import date

class Command(BaseCommand):
    help = 'Crea datos de prueba para la aplicación, incluyendo Liga MX y MLS.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Limpiando la base de datos...")
        PlantillaJugador.objects.all().delete()
        EquipoTemporada.objects.all().delete()
        Jugador.objects.all().delete()
        Equipo.objects.all().delete()
        Sede.objects.all().delete()
        Temporada.objects.all().delete()
        Liga.objects.all().delete()
        Federacion.objects.all().delete()

        self.stdout.write("Creando datos de prueba...")

        # 1. Federaciones
        self.stdout.write("Creando Federaciones...")
        federacion_uefa = Federacion.objects.create(nombre='UEFA', activa=True)
        federacion_conmebol = Federacion.objects.create(nombre='CONMEBOL', activa=True)
        federacion_concacaf = Federacion.objects.create(nombre='CONCACAF', activa=True)

        # 2. Ligas
        self.stdout.write("Creando Ligas...")
        liga_esp = Liga.objects.create(nombre='La Liga', federacion=federacion_uefa, activa=True)
        liga_arg = Liga.objects.create(nombre='Liga Profesional', federacion=federacion_conmebol, activa=True)
        liga_mx = Liga.objects.create(nombre='Liga MX', federacion=federacion_concacaf, activa=True)
        liga_mls = Liga.objects.create(nombre='MLS', federacion=federacion_concacaf, activa=True)

        # 3. Temporadas
        self.stdout.write("Creando Temporadas...")
        temporada_2425_laliga = Temporada.objects.create(
            liga=liga_esp, nombre='2024-2025', estado=Temporada.EstadoTemporada.PLANEADA,
            modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA, fecha_inicio_propuesta=date(2024, 8, 16)
        )
        temporada_2024_arg = Temporada.objects.create(
            liga=liga_arg, nombre='2024', estado=Temporada.EstadoTemporada.ACTIVA,
            modalidad=Temporada.ModalidadCalendario.UNA_VUELTA, fecha_inicio_propuesta=date(2024, 1, 28)
        )
        temporada_2024_mls = Temporada.objects.create(
            liga=liga_mls, nombre='2024', estado=Temporada.EstadoTemporada.ACTIVA,
            modalidad=Temporada.ModalidadCalendario.DOBLE_VUELTA, fecha_inicio_propuesta=date(2024, 2, 21)
        )
        temporada_ap24_mx = Temporada.objects.create(
            liga=liga_mx, nombre='Apertura 2024', estado=Temporada.EstadoTemporada.ACTIVA,
            modalidad=Temporada.ModalidadCalendario.UNA_VUELTA, fecha_inicio_propuesta=date(2024, 7, 5)
        )

        # 4. Sedes
        self.stdout.write("Creando Sedes...")
        sedes = {
            # Sedes existentes
            'bernabeu': Sede.objects.create(nombre='Santiago Bernabéu', ciudad='Madrid', direccion='Av. de Concha Espina, 1', activa=True),
            'monumental': Sede.objects.create(nombre='Estadio Monumental', ciudad='Buenos Aires', direccion='Av. Pres. Figueroa Alcorta 7597', activa=True),
            'dignity': Sede.objects.create(nombre='Dignity Health Sports Park', ciudad='Carson', direccion='18400 Avalon Blvd', activa=True),
            'chase': Sede.objects.create(nombre='Chase Stadium', ciudad='Fort Lauderdale', direccion='1350 NW 55th St', activa=True),

            # Sedes Liga MX
            'ciudad_deportes': Sede.objects.create(nombre='Estadio Ciudad de los Deportes', ciudad='Ciudad de México', direccion='C. Indiana 255', activa=True),
            'jalisco': Sede.objects.create(nombre='Estadio Jalisco', ciudad='Guadalajara', direccion='C. 7 Colinas 1772', activa=True),
            'alfonso_lastras': Sede.objects.create(nombre='Estadio Alfonso Lastras Ramírez', ciudad='San Luis Potosí', direccion='C. Zenith 105', activa=True),
            'olimpico_juarez': Sede.objects.create(nombre='Estadio Olímpico Benito Juárez', ciudad='Ciudad Juárez', direccion='Av. Heroico Colegio Militar s/n', activa=True),
            'akron': Sede.objects.create(nombre='Estadio Akron', ciudad='Zapopan', direccion='C. Cto. JVC 2800', activa=True),
            'leon': Sede.objects.create(nombre='Estadio León', ciudad='León', direccion='Blvd. Adolfo López Mateos 1810', activa=True),
            'el_encanto': Sede.objects.create(nombre='Estadio El Encanto', ciudad='Mazatlán', direccion='Av. Múnich s/n', activa=True),
            'bbva': Sede.objects.create(nombre='Estadio BBVA', ciudad='Guadalupe', direccion='Av. Pablo Livas 2011', activa=True),
            'victoria': Sede.objects.create(nombre='Estadio Victoria', ciudad='Aguascalientes', direccion='C. Manuel Zavala Madrigal 101', activa=True),
            'hidalgo': Sede.objects.create(nombre='Estadio Hidalgo', ciudad='Pachuca', direccion='Blvd. Felipe Ángeles s/n', activa=True),
            'cuauhtemoc': Sede.objects.create(nombre='Estadio Cuauhtémoc', ciudad='Puebla', direccion='Calz. Ignacio Zaragoza 666', activa=True),
            'corregidora': Sede.objects.create(nombre='Estadio Corregidora', ciudad='Querétaro', direccion='Av. de las Torres s/n', activa=True),
            'tsm_corona': Sede.objects.create(nombre='Estadio TSM Corona', ciudad='Torreón', direccion='Carretera Torreón - San Pedro km 7', activa=True),
            'universitario': Sede.objects.create(nombre='Estadio Universitario', ciudad='San Nicolás de los Garza', direccion='C. Pedro de Alba s/n', activa=True),
            'caliente': Sede.objects.create(nombre='Estadio Caliente', ciudad='Tijuana', direccion='Blvd. Agua Caliente 12027', activa=True),
            'nemesio_diez': Sede.objects.create(nombre='Estadio Nemesio Díez', ciudad='Toluca', direccion='Av. Constituyentes Pte. 1000', activa=True),
            'olimpico_universitario': Sede.objects.create(nombre='Estadio Olímpico Universitario', ciudad='Ciudad de México', direccion='Av. de los Insurgentes Sur s/n', activa=True),
        }

        # 5. Equipos
        self.stdout.write("Creando Equipos...")
        equipos = {
            # Equipos existentes
            'rm': Equipo.objects.create(nombre='Real Madrid', federacion=federacion_uefa, activo=True),
            'river': Equipo.objects.create(nombre='River Plate', federacion=federacion_conmebol, activo=True),
            'galaxy': Equipo.objects.create(nombre='LA Galaxy', federacion=federacion_concacaf, activo=True),
            'miami': Equipo.objects.create(nombre='Inter Miami CF', federacion=federacion_concacaf, activo=True),

            # Equipos Liga MX
            'america': Equipo.objects.create(nombre='Club América', federacion=federacion_concacaf, activo=True),
            'atlas': Equipo.objects.create(nombre='Atlas', federacion=federacion_concacaf, activo=True),
            'san_luis': Equipo.objects.create(nombre='Atlético de San Luis', federacion=federacion_concacaf, activo=True),
            'cruz_azul': Equipo.objects.create(nombre='Cruz Azul', federacion=federacion_concacaf, activo=True),
            'juarez': Equipo.objects.create(nombre='FC Juárez', federacion=federacion_concacaf, activo=True),
            'chivas': Equipo.objects.create(nombre='Guadalajara', federacion=federacion_concacaf, activo=True),
            'leon': Equipo.objects.create(nombre='León', federacion=federacion_concacaf, activo=True),
            'mazatlan': Equipo.objects.create(nombre='Mazatlán FC', federacion=federacion_concacaf, activo=True),
            'monterrey': Equipo.objects.create(nombre='Monterrey', federacion=federacion_concacaf, activo=True),
            'necaxa': Equipo.objects.create(nombre='Necaxa', federacion=federacion_concacaf, activo=True),
            'pachuca': Equipo.objects.create(nombre='Pachuca', federacion=federacion_concacaf, activo=True),
            'puebla': Equipo.objects.create(nombre='Puebla', federacion=federacion_concacaf, activo=True),
            'queretaro': Equipo.objects.create(nombre='Querétaro', federacion=federacion_concacaf, activo=True),
            'santos': Equipo.objects.create(nombre='Santos Laguna', federacion=federacion_concacaf, activo=True),
            'tigres': Equipo.objects.create(nombre='Tigres UANL', federacion=federacion_concacaf, activo=True),
            'tijuana': Equipo.objects.create(nombre='Club Tijuana', federacion=federacion_concacaf, activo=True),
            'toluca': Equipo.objects.create(nombre='Toluca', federacion=federacion_concacaf, activo=True),
            'pumas': Equipo.objects.create(nombre='UNAM', federacion=federacion_concacaf, activo=True),
        }

        # 6. Jugadores
        self.stdout.write("Creando Jugadores...")
        jugadores = []
        nombres = ['Juan', 'Carlos', 'Luis', 'Miguel', 'Javier', 'Andrés', 'Leo', 'Cris', 'Ney', 'Kylian', 'Santiago', 'Julián', 'Diego', 'Héctor', 'Raúl']
        apellidos = ['García', 'Rodríguez', 'Messi', 'Ronaldo', 'Martínez', 'Hernández', 'López', 'Pérez', 'Mbappé', 'Giménez', 'Quiñones', 'Valdés', 'Herrera', 'Jiménez']
        posiciones = [p[0] for p in Jugador.PosicionJugador.choices]
        
        for _ in range(500): # Aumentar el pool de jugadores para cubrir todos los equipos
            jugadores.append(Jugador.objects.create(
                nombre=random.choice(nombres),
                apellido=random.choice(apellidos),
                fecha_nacimiento=date(random.randint(1990, 2005), random.randint(1, 12), random.randint(1, 28)),
                posicion=random.choice(posiciones),
                activo=True
            ))

        # 7. EquipoTemporada (Asociar equipos a temporadas y sedes)
        self.stdout.write("Asociando Equipos a Temporadas...")
        equipos_temporada = [
            # Otras ligas
            EquipoTemporada.objects.create(equipo=equipos['rm'], temporada=temporada_2425_laliga, sede=sedes['bernabeu']),
            EquipoTemporada.objects.create(equipo=equipos['river'], temporada=temporada_2024_arg, sede=sedes['monumental']),
            EquipoTemporada.objects.create(equipo=equipos['galaxy'], temporada=temporada_2024_mls, sede=sedes['dignity']),
            EquipoTemporada.objects.create(equipo=equipos['miami'], temporada=temporada_2024_mls, sede=sedes['chase']),
            
            # Liga MX
            EquipoTemporada.objects.create(equipo=equipos['america'], temporada=temporada_ap24_mx, sede=sedes['ciudad_deportes']),
            EquipoTemporada.objects.create(equipo=equipos['atlas'], temporada=temporada_ap24_mx, sede=sedes['jalisco']),
            EquipoTemporada.objects.create(equipo=equipos['san_luis'], temporada=temporada_ap24_mx, sede=sedes['alfonso_lastras']),
            EquipoTemporada.objects.create(equipo=equipos['cruz_azul'], temporada=temporada_ap24_mx, sede=sedes['ciudad_deportes']),
            EquipoTemporada.objects.create(equipo=equipos['juarez'], temporada=temporada_ap24_mx, sede=sedes['olimpico_juarez']),
            EquipoTemporada.objects.create(equipo=equipos['chivas'], temporada=temporada_ap24_mx, sede=sedes['akron']),
            EquipoTemporada.objects.create(equipo=equipos['leon'], temporada=temporada_ap24_mx, sede=sedes['leon']),
            EquipoTemporada.objects.create(equipo=equipos['mazatlan'], temporada=temporada_ap24_mx, sede=sedes['el_encanto']),
            EquipoTemporada.objects.create(equipo=equipos['monterrey'], temporada=temporada_ap24_mx, sede=sedes['bbva']),
            EquipoTemporada.objects.create(equipo=equipos['necaxa'], temporada=temporada_ap24_mx, sede=sedes['victoria']),
            EquipoTemporada.objects.create(equipo=equipos['pachuca'], temporada=temporada_ap24_mx, sede=sedes['hidalgo']),
            EquipoTemporada.objects.create(equipo=equipos['puebla'], temporada=temporada_ap24_mx, sede=sedes['cuauhtemoc']),
            EquipoTemporada.objects.create(equipo=equipos['queretaro'], temporada=temporada_ap24_mx, sede=sedes['corregidora']),
            EquipoTemporada.objects.create(equipo=equipos['santos'], temporada=temporada_ap24_mx, sede=sedes['tsm_corona']),
            EquipoTemporada.objects.create(equipo=equipos['tigres'], temporada=temporada_ap24_mx, sede=sedes['universitario']),
            EquipoTemporada.objects.create(equipo=equipos['tijuana'], temporada=temporada_ap24_mx, sede=sedes['caliente']),
            EquipoTemporada.objects.create(equipo=equipos['toluca'], temporada=temporada_ap24_mx, sede=sedes['nemesio_diez']),
            EquipoTemporada.objects.create(equipo=equipos['pumas'], temporada=temporada_ap24_mx, sede=sedes['olimpico_universitario']),
        ]

        # 8. PlantillaJugador (Crear plantillas)
        self.stdout.write("Creando Plantillas...")
        jugadores_disponibles = list(jugadores)
        
        for et in equipos_temporada:
            dorsales_usados = set()
            for _ in range(random.randint(18, 25)): # Cada equipo tendrá entre 18 y 25 jugadores
                if not jugadores_disponibles:
                    break
                
                # Asegurar dorsal único
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

        self.stdout.write(self.style.SUCCESS('¡Datos de prueba creados exitosamente!'))
