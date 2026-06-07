# Footballer - Epica y requerimientos a nivel feature

## 1. Vision de producto

Footballer es una aplicacion web para administrar multiples ligas de futbol, sus temporadas, equipos, jugadores, calendarios de partidos, resultados, goleadores y tabla general.

El sistema debe permitir que distintos roles participen en la operacion de una liga:

- Administrador general: administra ligas.
- Administrador de liga: administra temporadas, equipos, jugadores y calendario.
- Arbitro: registra resultados y eventos de partido, principalmente goles.
- Usuario de consulta: visualiza jornadas, resultados, progreso de temporada y tabla general.

## 2. Epica propuesta

Como organizacion administradora de ligas de futbol, quiero gestionar ligas, temporadas, equipos, jugadores, calendarios, resultados y estadisticas de competencia, para controlar la operacion deportiva de cada temporada y consultar su progreso de forma confiable.

## 3. Objetivos de la epica

- Centralizar la administracion de ligas, temporadas, equipos y jugadores.
- Generar y administrar calendarios de partidos por jornada.
- Registrar resultados de partidos y goles por jugador.
- Calcular automaticamente la tabla general por temporada.
- Permitir la consulta del avance de jornadas, partidos y posiciones.
- Separar permisos segun responsabilidad operativa.

## 4. Alcance funcional

### Incluido

- Alta, edicion, habilitacion y deshabilitacion de ligas.
- Alta, edicion, habilitacion y deshabilitacion de temporadas.
- Alta, edicion, habilitacion y deshabilitacion de equipos.
- Alta, edicion, habilitacion y deshabilitacion de jugadores.
- Asociacion de equipos a temporadas.
- Asociacion de jugadores a equipos.
- Creacion de calendario por temporada.
- Soporte para calendario a una vuelta o doble vuelta.
- Administracion de jornadas y partidos.
- Registro de marcador final por partido.
- Registro de goleadores por partido, incluyendo minuto del gol.
- Consulta de calendario, resultados y avance por jornada.
- Consulta de tabla general por temporada.

### Fuera de alcance inicial sugerido

- Pagos, inscripciones o cuotas.
- Sanciones, tarjetas, lesiones o suspensiones.
- Estadisticas avanzadas de jugador.
- Playoffs, liguilla o fases eliminatorias.
- Transferencias historicas entre equipos.
- App movil nativa.
- Notificaciones en tiempo real.

## 5. Features propuestas

### F01. Gestion de ligas

Permite al administrador general crear y mantener las ligas que seran administradas en el sistema.

Capacidades:

- Crear liga.
- Editar datos de liga.
- Habilitar o deshabilitar liga.
- Consultar listado de ligas.
- Relacionar liga con una federacion u organismo, si aplica.

Criterios de aceptacion feature:

- Una liga deshabilitada no debe permitir crear nuevas temporadas.
- El nombre de liga debe ser obligatorio.
- No debe permitirse duplicar una liga activa con el mismo nombre dentro de la misma federacion, si se conserva la entidad Federacion.

### F02. Gestion de temporadas

Permite al administrador de liga crear temporadas para una liga especifica.

Capacidades:

- Crear temporada asociada a una liga.
- Editar temporada.
- Habilitar o deshabilitar temporada.
- Definir nombre de temporada, por ejemplo Apertura 2026 o Clausura 2026.
- Definir configuracion de calendario: una vuelta o doble vuelta.
- Definir estado de temporada: planeada, activa, finalizada o cancelada.

Criterios de aceptacion feature:

- Una temporada debe pertenecer a una sola liga.
- No debe poder registrarse resultado de partidos si la temporada esta finalizada o cancelada.
- La configuracion de una o doble vuelta debe quedar definida antes de generar calendario.

### F03. Gestion de equipos

Permite administrar el catalogo de equipos y su participacion en temporadas.

Capacidades:

- Crear equipo.
- Editar equipo.
- Habilitar o deshabilitar equipo.
- Asociar equipo a una liga.
- Asociar equipo a una temporada.
- Consultar equipos participantes por temporada.

Criterios de aceptacion feature:

- Un equipo deshabilitado no debe poder agregarse a nuevas temporadas.
- Un equipo no debe repetirse dentro de la misma temporada.
- Una temporada debe tener al menos dos equipos para generar calendario.

### F04. Gestion de jugadores

Permite administrar jugadores y asociarlos a equipos.

Capacidades:

- Crear jugador.
- Editar jugador.
- Habilitar o deshabilitar jugador.
- Asociar jugador a un equipo.
- Consultar plantilla de jugadores por equipo.

Criterios de aceptacion feature:

- Un jugador deshabilitado no debe poder registrarse como goleador.
- Un jugador debe pertenecer a un equipo para poder participar en los registros de partido.
- El sistema debe validar que el goleador pertenezca a uno de los dos equipos del partido.

### F05. Generacion y administracion de calendario

Permite crear los partidos de una temporada organizados por jornadas.

Capacidades:

- Generar calendario para una temporada.
- Definir jornadas.
- Crear partidos con equipo local y visitante.
- Definir fecha de partido.
- Soportar modalidad una vuelta: cada par de equipos juega una vez.
- Soportar modalidad doble vuelta: cada par de equipos juega dos veces, invirtiendo local y visitante.
- Editar fecha de partidos antes de jugarse.

Criterios de aceptacion feature:

- Un partido debe tener un equipo local y un equipo visitante distintos.
- En doble vuelta, si Equipo A es local contra Equipo B en el primer partido, Equipo B debe ser local contra Equipo A en el segundo.
- No debe poder modificarse el local o visitante de un partido ya jugado, salvo que exista una regla administrativa especial.
- El calendario debe estar asociado a una temporada.

### F06. Registro de resultados de partido

Permite al arbitro registrar el marcador final de cada partido.

Capacidades:

- Registrar goles de local.
- Registrar goles de visitante.
- Marcar partido como jugado.
- Editar resultado bajo permisos definidos.
- Validar que el partido pertenezca a una temporada activa.

Criterios de aceptacion feature:

- Los goles del marcador deben ser numeros enteros mayores o iguales a cero.
- Al registrar el resultado, el sistema debe calcular el resultado deportivo: victoria local, empate o victoria visitante.
- Un partido jugado debe impactar la tabla general de la temporada.
- No debe permitirse registrar resultado de un partido sin local, visitante o fecha definida.

### F07. Registro de goleadores

Permite capturar que jugadores anotaron en cada partido y en que minuto.

Capacidades:

- Registrar goleador de equipo local o visitante.
- Registrar minuto del gol.
- Consultar goles por partido.
- Editar o eliminar registros de gol bajo permisos definidos.

Criterios de aceptacion feature:

- El jugador seleccionado como goleador debe pertenecer al equipo local o visitante del partido.
- El minuto del gol debe ser obligatorio y numerico.
- La cantidad de goles registrados por equipo deberia coincidir con el marcador final del partido.
- Si no coincide, el sistema debe bloquear el cierre del partido o mostrar una validacion pendiente.

### F08. Consulta de jornadas y progreso de temporada

Permite visualizar el avance de la temporada por jornada.

Capacidades:

- Consultar jornadas de una temporada.
- Ver partidos por jornada.
- Ver fechas, equipos, marcadores y estado del partido.
- Ver goleadores registrados por partido.
- Identificar partidos pendientes, jugados o en captura.

Criterios de aceptacion feature:

- La consulta debe filtrar por liga y temporada.
- El avance debe mostrar claramente que partidos ya tienen resultado y cuales estan pendientes.
- La informacion debe actualizarse al registrar resultados o goleadores.

### F09. Tabla general por temporada

Permite consultar la clasificacion de equipos de una temporada.

Capacidades:

- Calcular partidos jugados.
- Calcular partidos ganados.
- Calcular partidos empatados.
- Calcular partidos perdidos.
- Calcular goles a favor.
- Calcular goles en contra.
- Calcular diferencia de goles.
- Calcular puntos.
- Ordenar tabla por puntos.

Reglas de puntuacion:

- Victoria: 3 puntos.
- Empate: 1 punto.
- Derrota: 0 puntos.

Criterios de aceptacion feature:

- La tabla debe calcularse por temporada.
- Solo deben considerarse partidos jugados.
- El orden principal debe ser por puntos descendente.
- Se recomienda definir criterios de desempate: diferencia de goles, goles a favor, resultado directo o nombre del equipo.

### F10. Seguridad y administracion de permisos

Permite controlar que acciones puede realizar cada tipo de usuario.

Capacidades:

- Definir usuarios con rol.
- Restringir administracion de ligas al administrador general.
- Restringir administracion de temporadas, equipos y jugadores al administrador de liga.
- Permitir registro de resultados a arbitros.
- Permitir consultas a usuarios autorizados.

Criterios de aceptacion feature:

- Un usuario no debe poder modificar ligas, temporadas o partidos fuera de su alcance.
- Toda accion critica debe registrar usuario y fecha de modificacion.
- Los permisos deben aplicarse tanto en interfaz como en API.

## 6. Modelo de dominio inicial

Entidades identificadas desde requerimiento y diagrama ER:

- Federacion.
- Liga.
- Temporada.
- Equipo.
- Jugador.
- Jornada.
- Partido.
- Gol.
- Usuario.
- Rol.

Relaciones sugeridas:

- Federacion 1:N Liga.
- Liga 1:N Temporada.
- Liga 1:N Equipo, si los equipos pertenecen principalmente a una liga.
- Temporada N:M Equipo mediante una entidad intermedia `TemporadaEquipo`.
- Equipo 1:N Jugador, si no se requiere historico de transferencias.
- Temporada 1:N Jornada.
- Jornada 1:N Partido.
- Partido N:1 Equipo como local.
- Partido N:1 Equipo como visitante.
- Partido 1:N Gol.
- Gol N:1 Jugador.
- Usuario N:M Rol o Usuario N:1 Rol, segun complejidad requerida.

## 7. Sugerencias al diagrama ER

- Separar `Jornada` y `Partido`. En el diagrama, Jornada contiene columnas de partido; para un modelo relacional mas flexible conviene que Jornada agrupe partidos y Partido tenga local, visitante, fecha y marcador.
- Agregar `TemporadaEquipo` para modelar que un equipo participa en una temporada. Esto evita asumir que todos los equipos de una liga participan siempre en todas sus temporadas.
- Evaluar si `Jugador` debe relacionarse directo a `Equipo` o a una entidad historica como `EquipoJugador`. Para MVP basta `Jugador -> Equipo`; para historico conviene `EquipoJugador` con fechas de alta/baja.
- Agregar `PartidoGol` o `Gol` como entidad separada con partido, jugador, equipo y minuto.
- Agregar estados: liga, temporada, equipo, jugador y partido necesitan un campo de estado o activo/inactivo.
- Agregar auditoria: creadoPor, creadoEn, modificadoPor, modificadoEn.
- Definir reglas de integridad para que local y visitante no sean el mismo equipo.
- Definir criterios de desempate de tabla general desde el inicio.

## 8. Reglas de negocio iniciales

- Una liga puede tener muchas temporadas.
- Una temporada pertenece a una sola liga.
- Una temporada tiene multiples equipos participantes.
- Una temporada tiene multiples jornadas.
- Una jornada tiene multiples partidos.
- Un partido pertenece a una sola jornada.
- Un partido tiene exactamente un equipo local y un equipo visitante.
- El equipo local y visitante deben participar en la temporada del partido.
- Un partido puede estar pendiente, programado, en captura, jugado, cancelado o suspendido.
- Los puntos se calculan solo con partidos jugados.
- Si local anota mas goles que visitante, local suma 3 puntos y visitante 0.
- Si visitante anota mas goles que local, visitante suma 3 puntos y local 0.
- Si ambos anotan la misma cantidad de goles, ambos suman 1 punto.
- Un gol registrado debe pertenecer a un jugador de alguno de los equipos del partido.
- El total de goles registrados por equipo debe coincidir con el marcador cuando el partido se cierre.

## 9. Requerimientos no funcionales sugeridos

- La aplicacion debe ser web y responsive.
- Las operaciones criticas deben requerir autenticacion.
- Los permisos deben validarse en servidor.
- La tabla general debe calcularse de forma consistente ante ediciones de resultados.
- Las consultas principales deben permitir filtro por liga y temporada.
- El sistema debe conservar trazabilidad de cambios importantes.
- El sistema debe evitar borrado fisico en catalogos principales; usar habilitar/deshabilitar.

## 10. Supuestos

- El MVP no contempla fases eliminatorias.
- El MVP no contempla tarjetas, sanciones ni cambios de jugador.
- El calendario se genera por temporada con base en los equipos participantes.
- Los arbitros solo pueden capturar resultados de partidos asignados o autorizados.
- La tabla general puede calcularse bajo demanda a partir de partidos jugados, evitando duplicar datos calculados al inicio.

## 11. Preguntas abiertas

- La entidad Federacion es obligatoria para el MVP o solo es clasificacion futura?
- Un equipo puede participar en multiples ligas o solo en una liga?
- Un jugador puede cambiar de equipo durante una temporada?
- Se requiere historico de jugadores por temporada?
- Habra asignacion formal de arbitros a partidos?
- Se permitiran partidos suspendidos, reprogramados o cancelados?
- Cuales seran los criterios oficiales de desempate?
- Se requiere registrar estadio o sede del partido?
- El calendario debe generarse automaticamente o tambien permitir captura manual?
- Se requiere importar equipos y jugadores desde archivo?

## 12. Propuesta de slicing para historias de usuario

### Incremento 1. Catalogos base

- Administrar ligas.
- Administrar temporadas.
- Administrar equipos.
- Administrar jugadores.
- Habilitar y deshabilitar registros.

### Incremento 2. Participacion de temporada

- Asociar equipos a temporada.
- Consultar equipos participantes.
- Validar minimo de equipos para calendario.

### Incremento 3. Calendario

- Generar jornadas.
- Generar partidos una vuelta.
- Generar partidos doble vuelta.
- Editar fechas de partidos.

### Incremento 4. Operacion de partidos

- Registrar marcador.
- Registrar goleadores.
- Cerrar partido.
- Validar consistencia marcador contra goles registrados.

### Incremento 5. Consulta y tabla general

- Consultar jornadas y progreso.
- Consultar resultados por temporada.
- Calcular y mostrar tabla general.
- Aplicar criterios de ordenamiento y desempate.

### Incremento 6. Seguridad operativa

- Gestionar usuarios y roles.
- Restringir permisos por rol.
- Registrar auditoria de cambios.

## 13. Borrador de especificaciones SDD

### Spec: Crear temporada

Given una liga activa
When el administrador de liga crea una temporada con nombre y configuracion de calendario
Then la temporada queda disponible en estado planeada
And puede recibir equipos participantes

### Spec: Generar calendario doble vuelta

Given una temporada planeada con equipos participantes
And la configuracion de calendario es doble vuelta
When el administrador genera el calendario
Then se crean dos partidos por cada par de equipos
And el segundo partido invierte local y visitante respecto al primero

### Spec: Registrar resultado

Given un partido programado de una temporada activa
When el arbitro captura marcador local y marcador visitante
Then el partido queda con resultado registrado
And la tabla general refleja puntos, goles a favor y goles en contra

### Spec: Registrar goleador

Given un partido con equipo local y visitante
When el arbitro registra un gol indicando jugador y minuto
Then el sistema guarda el gol asociado al partido
And valida que el jugador pertenezca a uno de los equipos del partido

### Spec: Consultar tabla general

Given una temporada con partidos jugados
When el usuario consulta la tabla general
Then el sistema muestra los equipos ordenados por puntos descendente
And muestra partidos jugados, ganados, empatados, perdidos, goles y diferencia de goles

