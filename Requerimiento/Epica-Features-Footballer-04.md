# Footballer - Epica y requerimientos a nivel feature v04

## 1. Control de version

- Version: 04.
- Documento base: `Requerimiento/Epica-Features-Footballer-03.md`.
- Respuesta incorporada: `Requerimiento/Respuesta-Epica-Features-Footballer-03.md`.
- Enfoque: Spec Driven Development.
- Stack definido: Python, Django, PostgreSQL y Bootstrap.
- Estado del modelo ER: sugerencias aceptadas y consideradas como base para el diseno.

## 2. Vision de producto

Footballer es una aplicacion web para administrar multiples ligas de futbol, sus temporadas, equipos, jugadores, calendarios de partidos, arbitros, sedes, resultados, eventos de partido, tabla general y tabla de goleadores.

El sistema debe permitir operar una liga desde su configuracion inicial hasta la consulta de resultados de temporada, manteniendo reglas claras de captura, validacion, permisos, exportacion y consistencia de datos.

## 3. Epica propuesta

Como organizacion administradora de ligas de futbol, quiero gestionar federaciones, ligas, temporadas, equipos, jugadores, arbitros, sedes, calendarios, partidos, resultados, eventos deportivos, tabla general y tabla de goleadores, para controlar la operacion completa de cada temporada y consultar su progreso de forma confiable.

## 4. Roles iniciales

- Administrador general: administra federaciones, ligas, usuarios base y configuracion global.
- Administrador de liga: administra temporadas, equipos, jugadores, sedes, calendarios y asignaciones de arbitros dentro de su alcance.
- Arbitro asignado: registra resultado y eventos de los partidos que tiene asignados.
- Arbitro con permiso general: puede registrar resultado y eventos de cualquier partido autorizado, aunque no este asignado al partido.
- Usuario de consulta: visualiza jornadas, resultados, progreso de temporada, tabla general y tabla de goleadores.

## 5. Objetivos de la epica

- Centralizar la administracion de federaciones, ligas, temporadas, equipos, jugadores, arbitros y sedes.
- Permitir que un equipo participe en multiples ligas y temporadas.
- Generar calendarios automaticamente a partir de equipos participantes.
- Permitir carga masiva de calendario, equipos y jugadores mediante layout descargable.
- Validar layouts antes de guardar informacion.
- Registrar resultados de partidos con goleadores obligatorios.
- Registrar goles, tarjetas amarillas y tarjetas rojas por jugador y minuto.
- Calcular automaticamente tabla general por temporada.
- Calcular tabla de goleadores por temporada.
- Exportar informacion operativa a Excel.
- Definir reglas de captura segun estado del partido y permisos del usuario.

## 6. Alcance funcional MVP

### Incluido

- Gestion de federaciones.
- Gestion de ligas.
- Gestion de temporadas.
- Gestion de equipos.
- Gestion de jugadores.
- Gestion basica de arbitros.
- Permiso booleano para identificar arbitro con captura general.
- Gestion de sedes con nombre, direccion, ciudad, referencia y foto.
- Asociacion de equipos a ligas.
- Asociacion de equipos a temporadas.
- Asociacion de jugadores a equipos antes de iniciar temporada.
- Generacion automatica de calendario por temporada.
- Carga masiva de calendario mediante layout Excel, solo antes de iniciar temporada.
- Carga masiva de equipos mediante layout Excel por liga.
- Carga masiva de jugadores mediante layout Excel a partir de un equipo existente.
- Validacion de layouts antes de confirmar la carga.
- Soporte para calendario a una vuelta o doble vuelta.
- Administracion de jornadas y partidos.
- Sede obligatoria para todos los partidos.
- Asignacion y cambio de arbitro antes de registrar resultado.
- Cambio de arbitro y sede en partidos suspendidos o reprogramados.
- Registro de marcador final por partido.
- Registro obligatorio de goleadores y minuto para cerrar resultado.
- Registro de eventos de partido: gol, tarjeta amarilla y tarjeta roja.
- Consulta de calendario, resultados y avance por jornada.
- Consulta de tabla general por temporada.
- Consulta de tabla de goleadores por temporada.
- Exportacion a Excel de calendario, tabla general, tabla de goleadores, equipos y jugadores.
- Estados de partido: pendiente, programado, en captura, jugado, suspendido, cancelado o reprogramado.

### Fuera de alcance inicial

- Fases eliminatorias o playoffs.
- Cambios de jugador durante una temporada iniciada.
- Historico detallado de transferencias de jugadores.
- Modulo de ajustes administrativos para modificar resultados ya cerrados.
- Pagos, inscripciones o cuotas.
- Estadisticas avanzadas de jugador fuera de goles y tarjetas.
- App movil nativa.
- Notificaciones en tiempo real.

## 7. Features propuestas

### F01. Gestion de federaciones

Permite al administrador general administrar federaciones u organismos que agrupan ligas.

Capacidades:

- Crear federacion.
- Editar federacion.
- Habilitar o deshabilitar federacion.
- Consultar federaciones.
- Asociar ligas a una federacion.

Criterios de aceptacion feature:

- Una federacion deshabilitada no debe permitir crear nuevas ligas asociadas.
- El nombre de federacion debe ser obligatorio.
- No debe permitirse duplicar una federacion activa con el mismo nombre.

### F02. Gestion de ligas

Permite al administrador general crear y mantener ligas dentro de una federacion.

Capacidades:

- Crear liga.
- Editar liga.
- Habilitar o deshabilitar liga.
- Consultar listado de ligas.
- Asociar liga a una federacion.

Criterios de aceptacion feature:

- Una liga debe pertenecer a una federacion.
- Una liga deshabilitada no debe permitir crear nuevas temporadas.
- No debe permitirse duplicar una liga activa con el mismo nombre dentro de la misma federacion.

### F03. Gestion de temporadas

Permite crear temporadas para una liga especifica y definir su configuracion operativa.

Capacidades:

- Crear temporada asociada a una liga.
- Editar temporada mientras no haya iniciado.
- Habilitar o deshabilitar temporada.
- Definir nombre de temporada, por ejemplo Apertura 2026 o Clausura 2026.
- Definir modalidad de calendario: una vuelta o doble vuelta.
- Definir estado de temporada: planeada, activa, finalizada o cancelada.
- Bloquear carga de calendario cuando la temporada ya esta en progreso.

Criterios de aceptacion feature:

- Una temporada debe pertenecer a una sola liga.
- La configuracion de calendario debe definirse antes de generar o cargar calendario.
- No debe poder modificarse la plantilla de jugadores de un equipo cuando la temporada ya inicio.
- No debe poder registrarse resultado si la temporada esta finalizada o cancelada.
- La carga de calendario por layout solo debe permitirse cuando la temporada no ha iniciado.

### F04. Gestion de equipos

Permite administrar equipos y su participacion en multiples ligas y temporadas.

Capacidades:

- Crear equipo.
- Editar equipo.
- Habilitar o deshabilitar equipo.
- Asociar equipo a una o mas ligas.
- Asociar equipo a una temporada.
- Consultar equipos participantes por temporada.
- Descargar layout de equipos por liga.
- Cargar equipos mediante layout por liga.
- Exportar equipos a Excel.

Criterios de aceptacion feature:

- Un equipo deshabilitado no debe poder agregarse a nuevas temporadas.
- Un equipo no debe repetirse dentro de la misma temporada.
- Una temporada debe tener al menos dos equipos para generar calendario.
- El modelo debe permitir que un equipo participe en multiples ligas.
- El layout de equipos debe descargarse en el contexto de una liga.

### F05. Gestion de jugadores

Permite administrar jugadores y asociarlos a equipos antes del inicio de temporada.

Capacidades:

- Crear jugador.
- Editar jugador.
- Habilitar o deshabilitar jugador.
- Asociar jugador a un equipo.
- Consultar plantilla de jugadores por equipo.
- Descargar layout de jugadores desde un equipo existente.
- Cargar jugadores mediante layout Excel para un equipo existente.
- Exportar jugadores a Excel.

Criterios de aceptacion feature:

- Un jugador deshabilitado no debe poder registrarse en eventos de partido.
- Un jugador debe pertenecer a un equipo participante para poder aparecer en eventos de partido.
- No se permiten cambios de jugador durante una temporada ya iniciada.
- Para cargar jugadores por layout, primero debe existir el equipo.
- Para el MVP no se requiere historico de cambios de equipo.

### F06. Gestion de arbitros

Permite registrar arbitros y asignarlos a partidos.

Capacidades:

- Crear arbitro.
- Editar arbitro.
- Habilitar o deshabilitar arbitro.
- Asignar arbitro a partido.
- Cambiar arbitro asignado antes de registrar resultado.
- Cambiar arbitro asignado cuando el partido este suspendido o reprogramado.
- Marcar si un arbitro tiene permiso general de captura mediante un campo booleano.

Criterios de aceptacion feature:

- Un partido debe tener un arbitro asignado para registrar resultado.
- El arbitro asignado solo puede capturar partidos que tenga asignados.
- Un arbitro con permiso general puede capturar cualquier partido autorizado.
- El permiso general debe modelarse como permiso o atributo booleano del arbitro, no como rol separado.
- Cuando un partido ya tiene resultado registrado, no se puede cambiar el arbitro asignado en la funcionalidad base.
- En partidos suspendidos o reprogramados si debe permitirse cambiar el arbitro.

### F07. Gestion de sedes

Permite administrar un catalogo de estadios o sedes para asignarlos a partidos.

Campos minimos:

- Nombre.
- Direccion.
- Ciudad.
- Referencia.
- Foto.

Capacidades:

- Crear sede.
- Editar sede.
- Habilitar o deshabilitar sede.
- Asociar sede a uno o varios partidos.
- Permitir que varios equipos compartan una sede.
- Permitir operar con una sede unica si la liga asi lo requiere.
- Cambiar sede cuando el partido este suspendido o reprogramado.
- Consultar sedes disponibles.

Criterios de aceptacion feature:

- La sede debe ser obligatoria para todos los partidos del MVP.
- Una sede deshabilitada no debe poder asignarse a nuevos partidos.
- Una sede puede ser compartida por multiples equipos o partidos.
- En partidos suspendidos o reprogramados si debe permitirse cambiar la sede.
- La foto de la sede debe poder registrarse como parte del catalogo.

### F08. Generacion y carga de calendario

Permite crear los partidos de una temporada por generacion automatica o carga masiva.

Capacidades:

- Generar calendario a partir de equipos participantes.
- Definir jornadas.
- Crear partidos con equipo local y visitante.
- Definir fecha y sede obligatoria de partido.
- Soportar una vuelta.
- Soportar doble vuelta invirtiendo local y visitante.
- Descargar layout Excel para calendario.
- Cargar calendario desde layout Excel solo antes de iniciar temporada.
- Validar layout y reportar anomalias antes de confirmar.
- Exportar calendario a Excel.

Criterios de aceptacion feature:

- Un partido debe tener local y visitante distintos.
- Local y visitante deben participar en la temporada.
- Todo partido debe tener sede.
- En doble vuelta deben existir dos partidos por cada par de equipos, invirtiendo local y visitante.
- El layout debe validar equipos inexistentes, equipos duplicados, sedes inexistentes, fechas invalidas, jornadas invalidas y partidos repetidos.
- El sistema debe mostrar un resultado de validacion antes de guardar la carga.
- La carga por layout debe bloquearse cuando la temporada ya esta en progreso.
- Si la carga de calendario crea jornadas, solo debe hacerlo durante la etapa inicial de temporada.

### F09. Registro de resultados de partido

Permite al arbitro registrar el marcador final de un partido.

Capacidades:

- Registrar goles de local.
- Registrar goles de visitante.
- Registrar eventos de gol con jugador y minuto.
- Marcar partido como jugado.
- Registrar usuario arbitro que captura.
- Bloquear edicion base despues del cierre del partido.

Criterios de aceptacion feature:

- Los goles del marcador deben ser enteros mayores o iguales a cero.
- Solo un arbitro asignado o un arbitro con permiso general puede registrar resultado.
- Para cerrar el partido, siempre deben capturarse goleadores y minuto de cada gol.
- La cantidad de eventos de gol por equipo debe coincidir con el marcador final.
- Al registrar resultado, el sistema calcula victoria local, empate o victoria visitante.
- Un partido jugado debe impactar la tabla general y la tabla de goleadores.
- Cuando un partido ya tiene resultado, no se puede modificar marcador ni arbitro en la funcionalidad base.

### F10. Registro de eventos de partido

Permite capturar eventos ocurridos durante el partido.

Eventos MVP:

- Gol.
- Tarjeta amarilla.
- Tarjeta roja.

Capacidades:

- Registrar tipo de evento.
- Registrar jugador.
- Registrar equipo del jugador.
- Registrar minuto.
- Asociar evento a partido.
- Consultar eventos por partido.

Criterios de aceptacion feature:

- El jugador del evento debe pertenecer a uno de los equipos del partido.
- El minuto debe ser obligatorio y numerico.
- Los eventos de gol son obligatorios para cerrar un partido con marcador mayor a cero.
- Las tarjetas se usan como criterio de desempate de tabla general.
- Los goles se usan para calcular tabla de goleadores.

### F11. Consulta de jornadas y progreso de temporada

Permite visualizar el avance de una temporada por jornada.

Capacidades:

- Consultar jornadas de una temporada.
- Ver partidos por jornada.
- Ver fecha, sede, local, visitante, marcador y estado.
- Ver arbitro asignado.
- Ver eventos registrados por partido.
- Identificar partidos pendientes, jugados, suspendidos, cancelados o reprogramados.
- Exportar calendario o resultados a Excel.

Criterios de aceptacion feature:

- La consulta debe filtrar por federacion, liga y temporada.
- El avance debe mostrar que partidos ya tienen resultado y cuales estan pendientes.
- La informacion debe actualizarse al registrar resultados o eventos.
- La exportacion debe respetar los filtros seleccionados.

### F12. Tabla general por temporada

Permite consultar la clasificacion de equipos de una temporada.

Capacidades:

- Calcular partidos jugados.
- Calcular partidos ganados.
- Calcular partidos empatados.
- Calcular partidos perdidos.
- Calcular goles a favor.
- Calcular goles en contra.
- Calcular diferencia de goles.
- Calcular tarjetas amarillas.
- Calcular tarjetas rojas.
- Calcular puntos.
- Ordenar tabla por criterios definidos.
- Exportar tabla general a Excel.

Reglas de puntuacion:

- Victoria: 3 puntos.
- Empate: 1 punto.
- Derrota: 0 puntos.

Criterios de ordenamiento:

1. Mayor cantidad de puntos.
2. Mayor cantidad de goles a favor.
3. Menor cantidad de goles en contra.
4. Menor cantidad de tarjetas rojas.
5. Menor cantidad de tarjetas amarillas.
6. Nombre del equipo en orden alfabetico ascendente, A-Z.

Criterios de aceptacion feature:

- La tabla debe calcularse por temporada.
- Solo deben considerarse partidos jugados.
- Los eventos de tarjeta deben impactar los criterios de desempate.
- La tabla puede calcularse bajo demanda a partir de partidos y eventos.
- La exportacion debe conservar el orden aplicado en pantalla.

### F13. Tabla de goleadores

Permite consultar el ranking de jugadores con goles registrados en una temporada.

Capacidades:

- Calcular goles por jugador.
- Filtrar por federacion, liga y temporada.
- Mostrar equipo del jugador.
- Ordenar por cantidad de goles descendente.
- En caso de empate en goles, visualizar por nombre de jugador A-Z.
- Permitir multiples campeones de goleo si tienen la misma cantidad de goles.
- Exportar tabla de goleadores a Excel.

Criterios de aceptacion feature:

- La tabla de goleadores debe calcularse a partir de eventos de tipo gol.
- Solo deben considerarse partidos jugados.
- Cada gol debe tener jugador y minuto.
- Si un partido tiene marcador mayor a cero, no puede cerrarse sin eventos de gol correspondientes.
- No hay desempate deportivo para campeon de goleo; jugadores empatados comparten posicion o reconocimiento.
- La exportacion a Excel debe estar disponible en el MVP.

### F14. Cargas masivas y layouts

Permite descargar layouts y cargar informacion inicial o masiva.

Layouts MVP:

- Equipos por liga.
- Jugadores por equipo existente.
- Calendario por temporada.

Capacidades:

- Descargar layout Excel.
- Cargar archivo Excel.
- Validar archivo.
- Mostrar errores y advertencias.
- Confirmar carga solo si no hay errores bloqueantes.
- Exportar equipos, jugadores, calendario y tablas a Excel.

Criterios de aceptacion feature:

- El sistema debe reportar fila, columna y descripcion del error.
- El sistema debe detectar duplicados dentro del archivo.
- El sistema debe detectar referencias inexistentes.
- La carga no debe guardar datos parcialmente si existen errores bloqueantes.
- La carga de equipos debe realizarse en contexto de una liga.
- La carga de jugadores requiere equipo existente.
- La carga de calendario solo puede realizarse antes de iniciar temporada.

### F15. Seguridad y administracion de permisos

Permite controlar acciones por rol y alcance.

Capacidades:

- Definir usuarios con rol.
- Restringir administracion global al administrador general.
- Restringir administracion operativa al administrador de liga.
- Permitir captura de partidos a arbitros asignados.
- Permitir captura general a arbitros con permiso booleano.
- Permitir consultas a usuarios autorizados.

Criterios de aceptacion feature:

- Un usuario no debe modificar informacion fuera de su alcance.
- Toda accion critica debe registrar usuario y fecha.
- Los permisos deben aplicarse en vistas Django y en cualquier endpoint futuro.
- El permiso de arbitro general debe evaluarse junto con el rol de arbitro.

## 8. Modelo ER objetivo v04

Las sugerencias al diagrama ER quedan aceptadas para la siguiente version del modelo. El diseno objetivo del MVP debe considerar estas entidades:

- Federacion.
- Liga.
- Temporada.
- Equipo.
- LigaEquipo.
- TemporadaEquipo.
- Jugador.
- Arbitro.
- Sede.
- Jornada.
- Partido.
- EventoPartido.
- Usuario.
- Rol o Grupo Django.

Relaciones objetivo:

- Federacion 1:N Liga.
- Liga N:M Equipo mediante `LigaEquipo`.
- Liga 1:N Temporada.
- Temporada N:M Equipo mediante `TemporadaEquipo`.
- Equipo 1:N Jugador para MVP.
- Temporada 1:N Jornada.
- Jornada 1:N Partido.
- Partido N:1 Equipo como local.
- Partido N:1 Equipo como visitante.
- Partido N:1 Arbitro asignado.
- Partido N:1 Sede obligatoria.
- Partido 1:N EventoPartido.
- EventoPartido N:1 Jugador.
- EventoPartido N:1 Equipo.
- Usuario asociado a Arbitro cuando aplique.

Campos conceptuales relevantes:

- `Arbitro.es_arbitro_general`: booleano para permiso de captura general.
- `Sede.nombre`: obligatorio.
- `Sede.direccion`: obligatorio.
- `Sede.ciudad`: obligatorio.
- `Sede.referencia`: obligatorio.
- `Sede.foto`: obligatorio u opcional por configuracion tecnica, pero contemplado en MVP.
- `Partido.sede`: obligatoria.
- `Partido.estado`: pendiente, programado, en captura, jugado, suspendido, cancelado o reprogramado.
- `EventoPartido.tipo`: gol, tarjeta_amarilla, tarjeta_roja.
- `EventoPartido.minuto`: obligatorio.

Decisiones de modelado aceptadas:

- Federacion queda en el MVP.
- Jornada y Partido son entidades separadas.
- Gol se modela como `EventoPartido` de tipo gol.
- Tarjetas se modelan como `EventoPartido` de tipo tarjeta amarilla o tarjeta roja.
- Equipo se modela como catalogo independiente y se relaciona con Liga mediante `LigaEquipo`.
- Participacion de equipos en temporada se controla mediante `TemporadaEquipo`.
- Sede es entidad obligatoria para Partido.
- Arbitro incluye permiso booleano de captura general.
- Se agregan estados y auditoria a entidades principales.

## 9. Reglas de negocio iniciales

- Una federacion puede tener muchas ligas.
- Una liga pertenece a una federacion.
- Un equipo puede participar en multiples ligas.
- Una liga puede tener muchas temporadas.
- Una temporada pertenece a una liga.
- Una temporada tiene equipos participantes definidos antes de iniciar.
- No se permiten cambios de jugadores durante una temporada iniciada.
- El calendario se genera o carga a partir de equipos participantes.
- La carga de calendario solo se permite antes de iniciar temporada.
- Un partido debe tener local y visitante distintos.
- Local y visitante deben participar en la temporada.
- Todo partido debe tener sede.
- Una sede puede ser compartida por equipos o partidos.
- Para registrar resultado debe existir arbitro asignado, salvo captura por arbitro con permiso general.
- Si un partido ya tiene resultado, no se puede cambiar marcador ni arbitro en funcionalidad base.
- Si un partido esta suspendido o reprogramado, se puede cambiar arbitro y sede.
- Para cerrar un partido con goles, deben existir eventos de gol con jugador y minuto.
- El total de eventos de gol por equipo debe coincidir con el marcador final.
- Los puntos se calculan solo con partidos jugados.
- Un evento de partido debe pertenecer a un jugador de local o visitante.
- Las tarjetas rojas y amarillas se consideran para desempate.
- Los goles registrados alimentan la tabla de goleadores.
- La tabla general desempata finalmente por nombre de equipo A-Z.
- La tabla de goleadores no define desempate deportivo; puede haber multiples campeones de goleo.

## 10. Requerimientos no funcionales y tecnicos

- La aplicacion se desarrollara con Python y Django.
- La base de datos sera PostgreSQL.
- La interfaz web usara Bootstrap.
- Las operaciones criticas deben requerir autenticacion.
- Los permisos deben validarse en servidor.
- Las cargas Excel deben validarse antes de guardar.
- Las exportaciones Excel deben respetar filtros y ordenamientos.
- La tabla general debe calcularse consistentemente ante registros de resultado.
- La tabla de goleadores debe calcularse desde eventos de gol.
- Las fotos de sede deben almacenarse y servirse mediante la configuracion de archivos/media definida para Django.
- Se recomienda usar transacciones de base de datos para cargas masivas y cierre de partido.
- Se recomienda aprovechar Django Admin para administracion temprana de catalogos, si acelera el MVP.

## 11. Supuestos actualizados

- El MVP no contempla fases eliminatorias; se atenderan en otra fase.
- El MVP no contempla cambios de jugador durante temporada.
- El MVP si contempla tarjetas amarillas y rojas como eventos de partido.
- El calendario se genera con equipos ya definidos en temporada.
- La carga de calendario solo ocurre antes de que la temporada este en progreso.
- Los arbitros capturan resultados segun asignacion, con excepcion del permiso general.
- Los partidos suspendidos o reprogramados permiten modificar arbitro y sede.
- La tabla general se calcula con base en partidos jugados y eventos registrados.
- La tabla de goleadores se calcula con eventos de tipo gol.
- No se llevara historico de transferencias de jugadores en el MVP.

## 12. Preguntas abiertas actualizadas

- La foto de sede sera obligatoria para guardar la sede o puede quedar opcional en la implementacion?
- Se requiere registrar capacidad de la sede o queda fuera del MVP?
- En tabla de goleadores, si hay empate en goles, la misma posicion se comparte o solo se muestran nombres A-Z sin posicion compartida?
- Para partidos suspendidos, se conservaran eventos capturados previamente o en MVP no se capturan eventos hasta cerrar partido?
- El layout de calendario debe incluir sede por nombre, codigo o identificador?
- Los archivos Excel exportados deben incluir logotipo/nombre de liga o solo datos tabulares?

## 13. Propuesta de slicing para historias de usuario

### Incremento 1. Base administrativa

- Gestionar federaciones.
- Gestionar ligas.
- Gestionar temporadas.
- Gestionar equipos.
- Gestionar jugadores.
- Gestionar sedes obligatorias con foto.

### Incremento 2. Participacion y plantillas

- Asociar equipos a ligas.
- Asociar equipos a temporadas.
- Asociar jugadores a equipos antes de iniciar temporada.
- Validar minimo de equipos para calendario.

### Incremento 3. Arbitros y permisos

- Gestionar arbitros.
- Asignar arbitros a partidos.
- Configurar permiso `es_arbitro_general`.
- Restringir captura por rol, asignacion y permiso general.

### Incremento 4. Calendario

- Generar calendario una vuelta.
- Generar calendario doble vuelta.
- Descargar layout de calendario.
- Cargar calendario desde Excel solo antes de iniciar temporada.
- Validar anomalias de calendario.
- Exportar calendario.

### Incremento 5. Operacion de partidos

- Registrar marcador.
- Registrar eventos de gol obligatorios.
- Registrar tarjetas.
- Cerrar partido.
- Bloquear cambios base despues del cierre.
- Permitir cambio de arbitro y sede si el partido esta suspendido o reprogramado.

### Incremento 6. Consulta y tablas

- Consultar jornadas y progreso.
- Consultar resultados por temporada.
- Calcular tabla general.
- Calcular tabla de goleadores.
- Aplicar criterios de ordenamiento.

### Incremento 7. Cargas y exportaciones

- Descargar layout de equipos por liga.
- Cargar equipos por liga.
- Descargar layout de jugadores desde equipo existente.
- Cargar jugadores.
- Exportar equipos, jugadores, calendario, tabla general y tabla de goleadores.
- Reportar errores de validacion.

## 14. Borrador de especificaciones SDD

### Spec: Crear liga con federacion

Given una federacion activa
When el administrador general crea una liga con nombre valido
Then la liga queda asociada a la federacion
And queda disponible para crear temporadas

### Spec: Asociar equipo a multiples ligas

Given un equipo activo
And dos ligas activas
When el administrador asocia el equipo a ambas ligas
Then el equipo queda disponible en el catalogo de cada liga
And puede participar en temporadas distintas segun configuracion

### Spec: Crear sede

Given un administrador de liga autenticado
When registra una sede con nombre, direccion, ciudad, referencia y foto
Then la sede queda disponible para asignarse a partidos

### Spec: Generar calendario doble vuelta con sede

Given una temporada planeada con equipos participantes
And la configuracion de calendario es doble vuelta
When el administrador genera el calendario
Then se crean dos partidos por cada par de equipos
And el segundo partido invierte local y visitante respecto al primero
And cada partido debe tener una sede antes de quedar programado

### Spec: Validar layout de calendario antes de iniciar temporada

Given una temporada planeada que no ha iniciado
When el administrador carga un layout de calendario
Then el sistema valida equipos, jornadas, fechas, sedes y duplicados
And muestra el resultado de validacion antes de guardar

### Spec: Bloquear carga de calendario con temporada en progreso

Given una temporada en progreso
When el administrador intenta cargar un layout de calendario
Then el sistema rechaza la carga
And explica que el calendario no puede modificarse por layout despues del inicio

### Spec: Cambiar arbitro y sede en partido reprogramado

Given un partido en estado reprogramado o suspendido
When el administrador de liga cambia arbitro o sede
Then el sistema guarda los nuevos datos
And conserva la trazabilidad del cambio

### Spec: Registrar resultado con goleadores obligatorios

Given un partido programado con arbitro asignado
When el arbitro captura el marcador y los eventos de gol correspondientes
Then el partido queda con resultado registrado
And la cantidad de goles por equipo coincide con el marcador
And la tabla general y la tabla de goleadores se actualizan en consulta

### Spec: Rechazar cierre sin goleadores

Given un partido con marcador mayor a cero
When el arbitro intenta cerrar el partido sin indicar goleadores y minuto
Then el sistema rechaza el cierre
And muestra que cada gol requiere jugador y minuto

### Spec: Registrar evento de tarjeta

Given un partido programado con equipos local y visitante
When el arbitro registra una tarjeta amarilla o roja para un jugador
Then el sistema guarda el evento con jugador, equipo, minuto y tipo
And valida que el jugador pertenezca a uno de los equipos del partido

### Spec: Consultar tabla general con desempate A-Z

Given una temporada con partidos jugados y eventos registrados
When el usuario consulta la tabla general
Then el sistema ordena por puntos, goles a favor, goles en contra, tarjetas rojas, tarjetas amarillas y nombre de equipo A-Z
And muestra estadisticas por equipo de la temporada

### Spec: Consultar tabla de goleadores con empate permitido

Given una temporada con goles registrados
When el usuario consulta la tabla de goleadores
Then el sistema ordena por goles descendente y nombre de jugador A-Z
And permite que dos o mas jugadores compartan campeonato de goleo si tienen la misma cantidad de goles

### Spec: Exportar informacion a Excel

Given una consulta filtrada de calendario, tabla general, tabla de goleadores, equipos o jugadores
When el usuario solicita exportar a Excel
Then el sistema genera un archivo con los datos filtrados
And conserva el orden visible en la consulta

