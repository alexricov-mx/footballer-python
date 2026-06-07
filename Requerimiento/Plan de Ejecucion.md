# Plan de Ejecución para el MVP de Footballer

Este plan de ejecución detalla los pasos para construir el MVP de la aplicación Footballer, basado en el documento `Epica-Features-Footballer-06.md`. El desarrollo se divide en 7 incrementos funcionales.

## Incremento 1: Base administrativa

- **Objetivo:** Crear la estructura fundamental y los catálogos básicos de la aplicación.
- **Entidades a modelar:** `Federacion`, `Liga`, `Temporada`, `Equipo`, `Jugador`, `Sede`.
- **Tareas:**
    1.  **Definición de Modelos:** Escribir las clases de los modelos en `models.py` para las entidades mencionadas.
    2.  **Migraciones:** Crear y aplicar las migraciones iniciales de Django (`makemigrations` y `migrate`).
    3.  **Administración (CRUD):** Configurar el `Django Admin` para permitir la gestión (Crear, Leer, Actualizar, Eliminar) de estas entidades. Esto servirá como la primera interfaz de administración.
    4.  **Pruebas Unitarias:** Crear pruebas básicas para la creación y validación de cada modelo.

## Incremento 2: Participación y plantillas

- **Objetivo:** Implementar la lógica para que los equipos se puedan asociar a ligas y participar en temporadas.
- **Entidades a modelar:** `LigaEquipo`, `TemporadaEquipo`.
- **Tareas:**
    1.  **Definición de Modelos:** Crear los modelos intermedios para las relaciones muchos a muchos.
    2.  **Migraciones:** Generar y aplicar las nuevas migraciones.
    3.  **Lógica de Asociación:** Desarrollar las vistas o funcionalidades en el `Django Admin` para asociar equipos a ligas y temporadas.
    4.  **Validaciones:** Asegurar que un equipo no se pueda añadir dos veces a la misma temporada.
    5.  **Pruebas:** Probar la correcta asociación y desasociación de equipos.

## Incremento 3: Árbitros y permisos

- **Objetivo:** Establecer el sistema de arbitraje y los permisos para la captura de resultados.
- **Entidades a modelar:** `Arbitro`.
- **Tareas:**
    1.  **Definición de Modelo:** Crear el modelo `Arbitro` con su relación al `User` de Django y el campo `es_arbitro_general`.
    2.  **Migraciones:** Generar y aplicar la migración.
    3.  **Integración con Usuarios:** Crear la lógica para vincular un `User` de Django a un `Arbitro`.
    4.  **Sistema de Permisos:** Implementar la lógica de autorización que verifique si un usuario es un árbitro asignado o un árbitro general antes de permitir la captura de un partido.

## Incremento 4: Calendario

- **Objetivo:** Implementar la generación y gestión de los calendarios de partidos.
- **Entidades a modelar:** `Jornada`, `Partido`.
- **Tareas:**
    1.  **Definición de Modelos:** Crear los modelos `Jornada` y `Partido` con sus respectivas relaciones.
    2.  **Migraciones:** Generar y aplicar las migraciones.
    3.  **Algoritmo de Generación:** Desarrollar el servicio o función que genere automáticamente el calendario (una y doble vuelta) basándose en los equipos de la temporada, los días de juego y la fecha de inicio.
    4.  **Carga Masiva:**
        - Crear la funcionalidad para descargar el layout de Excel.
        - Implementar el proceso de carga del archivo, incluyendo la validación de datos y la pantalla de previsualización.
    5.  **Vistas:** Crear vistas para consultar el calendario por jornada.

## Incremento 5: Operación de partidos

- **Objetivo:** Permitir la captura de resultados, eventos y la gestión de estados de los partidos.
- **Entidades a modelar:** `EventoPartido`.
- **Tareas:**
    1.  **Definición de Modelo:** Crear el modelo `EventoPartido`.
    2.  **Migraciones:** Generar y aplicar la migración.
    3.  **Vistas de Captura:** Desarrollar la interfaz para que los árbitros puedan:
        - Registrar el marcador final (goles local y visitante).
        - Registrar los eventos del partido (goles con jugador y minuto, tarjetas).
        - Cambiar el estado del partido a `Jugado`.
    4.  **Reglas de Negocio:** Implementar las validaciones en el backend para asegurar que la cantidad de goles coincida con el marcador y que los goleadores sean obligatorios.
    5.  **Reagenda:** Crear la funcionalidad para modificar la fecha y sede de partidos `Suspendidos` o `Reprogramados`.

## Incremento 6: Consultas y tablas

- **Objetivo:** Mostrar la información consolidada y las clasificaciones de la temporada.
- **Tareas:**
    1.  **Lógica de Cálculo:**
        - Crear los métodos en los `managers` o servicios para calcular la tabla general dinámicamente a partir de los resultados de los partidos.
        - Implementar la lógica para calcular la tabla de goleadores a partir de los eventos de tipo `Gol`.
    2.  **Vistas de Consulta:**
        - Desarrollar las vistas que muestren la tabla general y la de goleadores, aplicando los filtros y criterios de ordenamiento especificados.
        - Asegurar que se manejen correctamente los empates y las posiciones compartidas.
    3.  **Interfaz de Usuario:** Presentar la información de forma clara y legible.

## Incremento 7: Cargas y exportaciones

- **Objetivo:** Finalizar las funcionalidades de importación y exportación de datos.
- **Tareas:**
    1.  **Cargas Masivas:**
        - Implementar la descarga de layouts y la carga masiva con previsualización para `Equipos` y `Jugadores`.
    2.  **Funcionalidad de Exportación:**
        - Crear un servicio reutilizable para exportar datos a formato Excel.
        - Implementar la funcionalidad de exportación en todas las vistas requeridas: calendario, tabla general, tabla de goleadores, equipos y jugadores.
    3.  **Pruebas End-to-End:** Realizar pruebas completas del flujo de cargas y exportaciones para asegurar la integridad de los datos.
