## Ajustes
Para F08, vamos a considerar que se puedan definir los dias de partido, es decir, si la liga tiene partidos en sabado y domingo, tendriamos que ver cuantos partidos son por jornada, cuantas sedes y asi poder "repartir" partidos y asignar horarios. Por lo que tendriamos que indicar un dia de inicio y apartir de ahi, calcular fechas y organizacion de cruzes de partidos. Esto no debe romper con las capacidades y criterios, solo es extenderlos, por lo que debe convivir la definicion.

La carga de cualquier excel, debe tener una pre-visualizacion de los datos antes de confirmar la carga.

## 12. Preguntas abiertas actualizadas

1. La foto de sede sera obligatoria para guardar la sede o puede quedar opcional en la implementacion?
2. Se requiere registrar capacidad de la sede o queda fuera del MVP?
3. En tabla de goleadores, si hay empate en goles, la misma posicion se comparte o solo se muestran nombres A-Z sin posicion compartida?
4. Para partidos suspendidos, se conservaran eventos capturados previamente o en MVP no se capturan eventos hasta cerrar partido?
5. El layout de calendario debe incluir sede por nombre, codigo o identificador?
6. Los archivos Excel exportados deben incluir logotipo/nombre de liga o solo datos tabulares?

## 12. Respuestas
1. Puede quedar opcional, pero podemos considerar el uso de una generica como inicial en la visualizacion.
2. queda fuera del MVP.
3. la posicion si seria compartida, es decir, si los 3 primeros estan igualados en mismos goles, los 3 serian el numero 1
4. para partidos suspendidos dejemos el MVP en solo "reagendar", cambio sede y fechas.
5. Que incluya todos los campos necesarios para que en alguna herramenta de analitica maneje la informacion que yo quiera usar.
6. solo datos tabulares.

