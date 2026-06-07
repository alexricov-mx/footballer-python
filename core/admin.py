from django.contrib import admin
from .models import (
    Federacion, Liga, Temporada, Equipo, Jugador, Sede,
    EquipoTemporada, PlantillaJugador,
    Arbitro, Jornada, Partido  # Importar nuevos modelos
)

# Inline para la plantilla de jugadores en EquipoTemporada
class PlantillaJugadorInline(admin.TabularInline):
    model = PlantillaJugador
    extra = 1  # Número de formularios extra para añadir jugadores
    autocomplete_fields = ['jugador']

# Admin para Jugador
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'posicion')
    search_fields = ['nombre', 'apellido'] # Requerido para autocomplete
    list_filter = ('posicion',)

# Admin para Equipo
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_federacion')
    search_fields = ('nombre', 'federacion__nombre')
    list_filter = ('federacion',)


    def get_federacion(self, obj):
        return obj.federacion.nombre
    get_federacion.short_description = 'Federación'
    get_federacion.admin_order_field = 'federacion__nombre'


# Admin para Sede
@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'activa')
    search_fields = ['nombre', 'ciudad']
    list_filter = ('ciudad', 'activa')

# Admin para Temporada
@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

# Admin para EquipoTemporada
@admin.register(EquipoTemporada)
class EquipoTemporadaAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'temporada', 'sede')
    search_fields = ('equipo__nombre', 'temporada__nombre', 'sede__nombre')
    list_filter = ('temporada', 'sede')
    inlines = [PlantillaJugadorInline]
    autocomplete_fields = ['equipo', 'temporada', 'sede']

# Registro de modelos simples
admin.site.register(Federacion)
admin.site.register(Liga)

# Nuevos registros para el Incremento 3
@admin.register(Arbitro)
class ArbitroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'fecha_nacimiento', 'activo')
    search_fields = ('nombre', 'apellido_paterno')
    list_filter = ('activo',)

class PartidoInline(admin.TabularInline):
    model = Partido
    extra = 0
    autocomplete_fields = ('equipo_local', 'equipo_visitante', 'sede', 'arbitro')
    readonly_fields = ('estado',)

@admin.register(Jornada)
class JornadaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'temporada')
    list_filter = ('temporada',)
    search_fields = ('temporada__nombre',)
    inlines = [PartidoInline]

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'jornada', 'fecha_hora', 'estado')
    list_filter = ('estado', 'jornada__temporada', 'jornada')
    search_fields = ('equipo_local__equipo__nombre', 'equipo_visitante__equipo__nombre', 'jornada__temporada__nombre')
    autocomplete_fields = ('jornada', 'equipo_local', 'equipo_visitante', 'sede', 'arbitro')
    list_editable = ('estado',)
