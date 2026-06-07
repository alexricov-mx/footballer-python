## 10. Supuestos
1. El MVP no contempla fases eliminatorias.
2. El MVP no contempla tarjetas, sanciones ni cambios de jugador.
3. El calendario se genera por temporada con base en los equipos participantes.
4. Los arbitros solo pueden capturar resultados de partidos asignados o autorizados.
5. La tabla general puede calcularse bajo demanda a partir de partidos jugados, evitando duplicar datos calculados al inicio.

## 10. Supuestos Respuestas
1. El MVP no contempla fases eliminatorias, sera en otra fase de desarrollo.
2. El MVP no contempla cambios de jugador, pero podemos contemplar tarjetas, es decir
registrar que tarjeta recibe un jugador y en que minuto. Podriamos llevarlo en una tabla
de eventos del partido, para que en esa tabla de eventos se lleven tipo de tarjeta y gol.
3. Si, el calendario debe generarse apartir que los equipos ya definidos en una temporada.
4. Si, solo los arbitros pueden registrar resultados, por lo que necesitamos considerar un lugar donde se tengan todos los arbitros y se puedan asignar a un partido, permitiendo tambien un arbitro general que pueda registrar cualquier partido aunque no este asignado a dicho partido.
5. si, la tabla general se basara en base a los resultados jugados.

## 11. Preguntas abiertas

1. La entidad Federacion es obligatoria para el MVP o solo es clasificacion futura?
2. Un equipo puede participar en multiples ligas o solo en una liga?
3. Un jugador puede cambiar de equipo durante una temporada?
4. Se requiere historico de jugadores por temporada?
5. Habra asignacion formal de arbitros a partidos?
6. Se permitiran partidos suspendidos, reprogramados o cancelados?
7. Cuales seran los criterios oficiales de desempate?
8. Se requiere registrar estadio o sede del partido?
9. El calendario debe generarse automaticamente o tambien permitir captura manual?
10. Se requiere importar equipos y jugadores desde archivo?

## 11. Preguntas abiertas Respuestas
1. La entidad Federacion me gustaria considerarla de una vez en el MVP, para evitar problemas en migraciones futuras.
2. Si, un equipo pudiera participar en multiples ligas.
3. no, no permitiremos cambios de jugadores en una temporada, esto se podra hacer hasta una nueva temporada y mientras no se haya iniciado.
4. En este momento, en el MVP no llevaremos historicos.
5. Si, si debera haber la asignacion de arbitro asi como cambios de arbitro, mientras no se haya registrado un partido. Para registrar un partido, debe haber un arbitro asignado, y cuando el partido tenga resultado, no se podra cambiar el resultado ni el arbitro, como funcionalidad base, talvez despues debamos considerar un modulo de ajustes.
6. si, podriamos considerar los estados que sugieres.
7. Los criterios de desempate por puntos seria, el equipo que mas goles tenga a favor (si empatan en ese rubro tambien), el equipo con menos goles en contra (si empatan en ese rubro tambien), el equipo con menos tarjetas rojas (si empatan en ese rubro tambien), el equipo con menos tarjetas amarillas (si empatan en ese rubro tambien), ya veremos.
8. si, registremos estadio o sede del partido, pero algo muy basico como un catalogo.
9. Debemos permitir las 2 opcciones, que se genere el calendario o que lo podamos subir con un layout que puedan descargar en excel. Debemos considerar un "validador" y poder entregar el resutlado en caso que se detecte alguna nomalia.
10. Si, permitamos un formulario de creacion desde la aplicacion web y ademas, permitir un layout para carga masiva de equipos  jugadores.