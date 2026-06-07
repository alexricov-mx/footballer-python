# Footballer - Epica y requerimientos a nivel feature v02

## 1. Control de version

- Version: 02.
- Documento base: `Epica-Features-Footballer-01.md`.
- Respuesta incorporada: `Respuesta-Epica-Features-Footballer-01.md`.
- Enfoque: Spec Driven Development.
- Stack definido: Python, Django, PostgreSQL y Bootstrap.

## 2. Vision de producto

Footballer es una aplicacion web para administrar multiples ligas de futbol, sus temporadas, equipos, jugadores, calendarios de partidos, arbitros, sedes, resultados, eventos de partido y tabla general.

El sistema debe permitir operar una liga desde su configuracion inicial hasta la consulta de resultados de temporada, manteniendo reglas claras de captura, validacion, permisos y consistencia de datos.

## 3. Epica propuesta

Como organizacion administradora de ligas de futbol, quiero gestionar federaciones, ligas, temporadas, equipos, jugadores, arbitros, sedes, calendarios, partidos, resultados y eventos deportivos, para controlar la operacion completa de cada temporada y consultar su progreso de forma confiable.

## 4. Roles iniciales

- Administrador general: administra federaciones, ligas, usuarios base y configuracion global.
- Administrador de liga: administra temporadas, equipos, jugadores, sedes, calendarios y asignaciones de arbitros dentro de su alcance.
- Arbitro asignado: registra resultado y eventos de los partidos que tiene asignados.
- Arbitro general: puede registrar resultado y eventos de cualquier partido autorizado, aunque no este asignado al partido.
- Usuario de consulta: visualiza jornadas, resultados, progreso de temporada y tabla general.

## 5. Objetivos de la epica

- Centralizar la administracion de federaciones, ligas, temporadas, equipos, jugadores, arbitros y sedes.
- Permitir que un equipo participe en multiples ligas y temporadas.
- Generar calendarios automaticamente a partir de equipos participantes.
- Permitir carga masiva de calendarios, equipos y jugadores mediante layout descargable.
- Registrar resultados de partidos y eventos deportivos.
- Registrar goles, tarjetas amarillas y tarjetas rojas por jugador y minuto.
- Calcular automaticamente la tabla general por temporada.
- Definir reglas de captura segun estado del partido y permisos del usuario.

## 6. Alcance funcional MVP

### Incluido

- Gestion de federaciones.
- Gestion de ligas.
- Gestion de temporadas.
- Gestion de equipos.
- Gestion de jugadores.
- Gestion basica de arbitros.
- Gestion basica de sedes o estadios.
- Asociacion de equipos a temporadas.
- Asociacion de jugadores a equipos antes de iniciar temporada.
- Generacion automatica de calendario por temporada.
- Carga masiva de calendario mediante layout Excel.
- Carga masiva de equipos y jugadores mediante layout Excel.
- Validacion de layouts antes de confirmar la carga.
- Soporte para calendario a una vuelta o doble vuelta.
- Administracion de jornadas y partidos.
- Asignacion y cambio de arbitro antes de registrar resultado.
- Registro de marcador final por partido.
- Registro de eventos de partido: gol, tarjeta amarilla y tarjeta roja.
- Consulta de calendario, resultados y avance por jornada.
- Consulta de tabla general por temporada.
- Estados de partido: pendiente, programado, en captura, jugado, suspendido, cancelado o reprogramado.

### Fuera de alcance inicial

- Fases eliminatorias o playoffs.
- Cambios de jugador durante una temporada iniciada.
- Historico detallado de transferencias de jugadores.
- Modulo de ajustes administrativos para modificar resultados ya cerrados.
- Pagos, inscripciones o cuotas.
- Estadisticas avanzadas de jugador.
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

Criterios de aceptacion feature:

- Una temporada debe pertenecer a una sola liga.
- La configuracion de calendario debe definirse antes de generar calendario.
- No debe poder modificarse la plantilla de jugadores de un equipo cuando la temporada ya inicio.
- No debe poder registrarse resultado si la temporada esta finalizada o cancelada.

### F04. Gestion de equipos

Permite administrar equipos y su participacion en multiples ligas y temporadas.

Capacidades:

- Crear equipo.
- Editar equipo.
- Habilitar o deshabilitar equipo.
- Asociar equipo a una o mas ligas.
- Asociar equipo a una temporada.
- Consultar equipos participantes por temporada.

Criterios de aceptacion feature:

- Un equipo deshabilitado no debe poder agregarse a nuevas temporadas.
- Un equipo no debe repetirse dentro de la misma temporada.
- Una temporada debe tener al menos dos equipos para generar calendario.
- El modelo debe permitir que un equipo participe en multiples ligas.

### F05. Gestion de jugadores

Permite administrar jugadores y asociarlos a equipos antes del inicio de temporada.

Capacidades:

- Crear jugador.
- Editar jugador.
- Habilitar o deshabilitar jugador.
- Asociar jugador a un equipo.
- Consultar plantilla de jugadores por equipo.
- Cargar jugadores mediante layout Excel.

Criterios de aceptacion feature:

- Un jugador deshabilitado no debe poder registrarse en eventos de partido.
- Un jugador debe pertenecer a un equipo participante para poder aparecer en eventos de partido.
- No se permiten cambios de jugador durante una temporada ya iniciada.
- Para el MVP no se requiere historico de cambios de equipo.

### F06. Gestion de arbitros

Permite registrar arbitros y asignarlos a partidos.

Capacidades:

- Crear arbitro.
- Editar arbitro.
- Habilitar o deshabilitar arbitro.
- Asignar arbitro a partido.
- Cambiar arbitro asignado antes de registrar resultado.
- Definir si un arbitro tiene permiso general de captura.

Criterios de aceptacion feature:

- Un partido debe tener un arbitro asignado para registrar resultado.
- El arbitro asignado solo puede capturar partidos que tenga asignados.
- El arbitro general puede capturar cualquier partido autorizado.
- Cuando un partido ya tiene resultado registrado, no se puede cambiar el arbitro asignado en la funcionalidad base.

### F07. Gestion de sedes

Permite administrar un catalogo basico de estadios o sedes para asignarlos a partidos.

Capacidades:

- Crear sede.
- Editar sede.
- Habilitar o deshabilitar sede.
- Asociar sede a un partido.
- Consultar sedes disponibles.

Criterios de aceptacion feature:

- La sede debe ser un catalogo simple en el MVP.
- Una sede deshabilitada no debe poder asignarse a nuevos partidos.
- Un partido puede tener sede opcional o requerida segun configuracion de liga; se recomienda definirla como opcional al inicio para no bloquear calendario.

### F08. Generacion y carga de calendario

Permite crear los partidos de una temporada por generacion automatica o carga masiva.

Capacidades:

- Generar calendario a partir de equipos participantes.
- Definir jornadas.
- Crear partidos con equipo local y visitante.
- Definir fecha y sede de partido.
- Soportar una vuelta.
- Soportar doble vuelta invirtiendo local y visitante.
- Descargar layout Excel para calendario.
- Cargar calendario desde layout Excel.
- Validar layout y reportar anomalias antes de confirmar.

Criterios de aceptacion feature:

- Un partido debe tener local y visitante distintos.
- Local y visitante deben participar en la temporada.
- En doble vuelta deben existir dos partidos por cada par de equipos, invirtiendo local y visitante.
- El layout debe validar equipos inexistentes, equipos duplicados, fechas invalidas, jornadas invalidas y partidos repetidos.
- El sistema debe mostrar un resultado de validacion antes de guardar la carga.

### F09. Registro de resultados de partido

Permite al arbitro registrar el marcador final de un partido.

Capacidades:

- Registrar goles de local.
- Registrar goles de visitante.
- Marcar partido como jugado.
- Registrar usuario arbitro que captura.
- Bloquear edicion base despues del cierre del partido.

Criterios de aceptacion feature:

- Los goles del marcador deben ser enteros mayores o iguales a cero.
- Solo un arbitro asignado o arbitro general puede registrar resultado.
- Al registrar resultado, el sistema calcula victoria local, empate o victoria visitante.
- Un partido jugado debe impactar la tabla general.
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
- Los eventos de gol deben poder conciliarse contra el marcador final.
- La cantidad de goles registrados por equipo debe coincidir con el marcador para cerrar el partido, salvo que se defina captura simplificada sin goleadores.
- Las tarjetas se usan como criterio de desempate de tabla general.

### F11. Consulta de jornadas y progreso de temporada

Permite visualizar el avance de una temporada por jornada.

Capacidades:

- Consultar jornadas de una temporada.
- Ver partidos por jornada.
- Ver fecha, sede, local, visitante, marcador y estado.
- Ver arbitro asignado.
- Ver eventos registrados por partido.
- Identificar partidos pendientes, jugados, suspendidos, cancelados o reprogramados.

Criterios de aceptacion feature:

- La consulta debe filtrar por federacion, liga y temporada.
- El avance debe mostrar que partidos ya tienen resultado y cuales estan pendientes.
- La informacion debe actualizarse al registrar resultados o eventos.

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
6. Criterio pendiente por definir si persiste empate.

Criterios de aceptacion feature:

- La tabla debe calcularse por temporada.
- Solo deben considerarse partidos jugados.
- Los eventos de tarjeta deben impactar los criterios de desempate.
- La tabla puede calcularse bajo demanda a partir de partidos y eventos.

### F13. Cargas masivas y layouts

Permite descargar layouts y cargar informacion inicial o masiva.

Layouts MVP:

- Equipos.
- Jugadores.
- Calendario.

Capacidades:

- Descargar layout Excel.
- Cargar archivo Excel.
- Validar archivo.
- Mostrar errores y advertencias.
- Confirmar carga solo si no hay errores bloqueantes.

Criterios de aceptacion feature:

- El sistema debe reportar fila, columna y descripcion del error.
- El sistema debe detectar duplicados dentro del archivo.
- El sistema debe detectar referencias inexistentes.
- La carga no debe guardar datos parcialmente si existen errores bloqueantes.

### F14. Seguridad y administracion de permisos

Permite controlar acciones por rol y alcance.

Capacidades:

- Definir usuarios con rol.
- Restringir administracion global al administrador general.
- Restringir administracion operativa al administrador de liga.
- Permitir captura de partidos a arbitros asignados o arbitros generales.
- Permitir consultas a usuarios autorizados.

Criterios de aceptacion feature:

- Un usuario no debe modificar informacion fuera de su alcance.
- Toda accion critica debe registrar usuario y fecha.
- Los permisos deben aplicarse en vistas Django y en cualquier endpoint futuro.

## 8. Modelo de dominio inicial v02

Entidades sugeridas:

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

Relaciones sugeridas:

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
- Partido N:1 Sede.
- Partido 1:N EventoPartido.
- EventoPartido N:1 Jugador.
- EventoPartido N:1 Equipo.
- Usuario asociado a Arbitro cuando aplique.

## 9. Sugerencias al diagrama ER

- Mantener Federacion en el MVP, como entidad padre de Liga.
- Modelar Equipo como catalogo independiente y relacionarlo con Liga mediante `LigaEquipo`.
- Usar `TemporadaEquipo` para controlar que equipos participan en una temporada concreta.
- Separar `Jornada` y `Partido`; Jornada agrupa, Partido contiene local, visitante, fecha, sede, arbitro y marcador.
- Reemplazar `Gol` por `EventoPartido`, para soportar goles y tarjetas desde el MVP.
- Agregar entidad `Arbitro` o perfil de usuario con rol arbitro.
- Agregar entidad `Sede` como catalogo simple.
- Agregar estados a temporada, partido y entidades principales.
- Agregar auditoria: creado_por, creado_en, modificado_por, modificado_en.
- Definir restricciones para evitar local igual a visitante.

## 10. Reglas de negocio iniciales

- Una federacion puede tener muchas ligas.
- Una liga pertenece a una federacion.
- Un equipo puede participar en multiples ligas.
- Una liga puede tener muchas temporadas.
- Una temporada pertenece a una liga.
- Una temporada tiene equipos participantes definidos antes de iniciar.
- No se permiten cambios de jugadores durante una temporada iniciada.
- El calendario se genera o carga a partir de equipos participantes.
- Un partido debe tener local y visitante distintos.
- Local y visitante deben participar en la temporada.
- Para registrar resultado debe existir arbitro asignado, salvo captura por arbitro general.
- Si un partido ya tiene resultado, no se puede cambiar marcador ni arbitro en funcionalidad base.
- Los puntos se calculan solo con partidos jugados.
- Un evento de partido debe pertenecer a un jugador de local o visitante.
- Las tarjetas rojas y amarillas se consideran para desempate.

## 11. Requerimientos no funcionales y tecnicos

- La aplicacion se desarrollara con Python y Django.
- La base de datos sera PostgreSQL.
- La interfaz web usara Bootstrap.
- Las operaciones criticas deben requerir autenticacion.
- Los permisos deben validarse en servidor.
- Las cargas Excel deben validarse antes de guardar.
- La tabla general debe calcularse consistentemente ante registros de resultado.
- Se recomienda usar transacciones de base de datos para cargas masivas y cierre de partido.
- Se recomienda aprovechar Django Admin para administracion temprana de catalogos, si acelera el MVP.

## 12. Supuestos actualizados

- El MVP no contempla fases eliminatorias; se atenderan en otra fase.
- El MVP no contempla cambios de jugador durante temporada.
- El MVP si contempla tarjetas amarillas y rojas como eventos de partido.
- El calendario se genera con equipos ya definidos en temporada.
- Los arbitros capturan resultados segun asignacion, con excepcion de arbitro general.
- La tabla general se calcula con base en partidos jugados y eventos registrados.
- No se llevara historico de transferencias de jugadores en el MVP.

## 13. Preguntas abiertas actualizadas

- El criterio final de desempate despues de tarjetas amarillas sera sorteo, fecha de registro, nombre de equipo o partido directo?
- La sede sera obligatoria para todos los partidos o opcional en MVP?
- El arbitro general sera un rol separado o un permiso especial sobre el rol arbitro?
- Se permitira guardar marcador aunque no se capturen goleadores?
- El layout de calendario debera crear jornadas automaticamente si no existen?
- La carga masiva de jugadores permitira crear equipos automaticamente o exigira equipos previamente creados?
- Se requiere exportar tabla general y calendario a Excel?

## 14. Propuesta de slicing para historias de usuario

### Incremento 1. Base administrativa

- Gestionar federaciones.
- Gestionar ligas.
- Gestionar temporadas.
- Gestionar equipos.
- Gestionar jugadores.
- Gestionar sedes.

### Incremento 2. Participacion y plantillas

- Asociar equipos a ligas.
- Asociar equipos a temporadas.
- Asociar jugadores a equipos antes de iniciar temporada.
- Validar minimo de equipos para calendario.

### Incremento 3. Arbitros y permisos

- Gestionar arbitros.
- Asignar arbitros a partidos.
- Definir arbitro general.
- Restringir captura por rol y asignacion.

### Incremento 4. Calendario

- Generar calendario una vuelta.
- Generar calendario doble vuelta.
- Descargar layout de calendario.
- Cargar calendario desde Excel.
- Validar anomalias de calendario.

### Incremento 5. Operacion de partidos

- Registrar marcador.
- Registrar eventos de partido.
- Cerrar partido.
- Bloquear cambios base despues del cierre.

### Incremento 6. Consulta y tabla general

- Consultar jornadas y progreso.
- Consultar resultados por temporada.
- Calcular tabla general.
- Aplicar criterios de desempate.

### Incremento 7. Cargas masivas

- Descargar layout de equipos.
- Cargar equipos.
- Descargar layout de jugadores.
- Cargar jugadores.
- Reportar errores de validacion.

## 15. Borrador de especificaciones SDD

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

### Spec: Generar calendario doble vuelta

Given una temporada planeada con equipos participantes
And la configuracion de calendario es doble vuelta
When el administrador genera el calendario
Then se crean dos partidos por cada par de equipos
And el segundo partido invierte local y visitante respecto al primero

### Spec: Validar layout de calendario

Given una temporada planeada
When el administrador carga un layout de calendario
Then el sistema valida equipos, jornadas, fechas y duplicados
And muestra el resultado de validacion antes de guardar

### Spec: Registrar resultado con arbitro asignado

Given un partido programado con arbitro asignado
When el arbitro asignado captura el marcador
Then el partido queda con resultado registrado
And no se permite cambiar el arbitro ni el marcador en la funcionalidad base

### Spec: Registrar evento de tarjeta

Given un partido programado con equipos local y visitante
When el arbitro registra una tarjeta amarilla o roja para un jugador
Then el sistema guarda el evento con jugador, equipo, minuto y tipo
And valida que el jugador pertenezca a uno de los equipos del partido

### Spec: Consultar tabla general con desempate

Given una temporada con partidos jugados y eventos registrados
When el usuario consulta la tabla general
Then el sistema ordena por puntos, goles a favor, goles en contra, tarjetas rojas y tarjetas amarillas
And muestra estadisticas por equipo de la temporada

