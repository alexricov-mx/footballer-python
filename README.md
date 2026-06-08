# Footballer - Gestor de Ligas de Fútbol

Footballer es una aplicación web desarrollada en Django para la gestión integral de ligas, equipos, jugadores y temporadas de fútbol.

## Estado Actual del Proyecto

Este proyecto sigue una metodología de **Specs-Driven Development (SDD)**. Todo el trabajo se organiza en "Incrementos", y cada incremento está documentado en su propia carpeta dentro de `docs/specs/`.

-   **Último Incremento Completado:** `Incremento 03: Gestión de Calendarios y Partidos`.
    -   **Resumen:** Se ha añadido la capacidad de gestionar árbitros, jornadas y partidos. El sistema ahora puede generar un calendario completo para una temporada, sentando las bases para el registro de resultados.
    -   **Documentación:** Puedes encontrar todos los detalles en [docs/specs/004-incremento-03-calendarios-partidos/](docs/specs/004-incremento-03-calendarios-partidos/).

### ¿Cómo continuar el desarrollo?

1.  **Revisa las Épicas Pendientes:** El trabajo a futuro está definido en los archivos de épicas que se encuentran en el directorio `Requerimiento/`.
2.  **Inicia el Siguiente Incremento:** El siguiente paso es el **Incremento 04: Registro de Resultados y Eventos**. La `spec` para este incremento se comenzará a definir en `docs/specs/005-incremento-04-resultados-eventos/`.

---

## Guía de Instalación y Configuración

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local.

### Prerrequisitos

-   **Python 3.10+**
-   **Podman** y **Podman-Compose**: Para la gestión de la base de datos. Asegúrate de que el servicio de Podman esté en ejecución.

### 1. Configuración de la Base de Datos

El proyecto utiliza PostgreSQL en un contenedor de Podman.

```bash
# Levanta el contenedor de la base de datos en segundo plano
podman compose up -d
podman compose down
podman compose logs -f
podman compose ps
```

en caso que falle, bajamos el contenedor
```bash
podman compose -f docker-compose.yml down
```

Eliminamos el volumen
```bash
podman volume rm footballer-python_postgres-data
```

Verificamos que no este el volumen
```bash
podman volume ls
```

Recreamos el contenedor
```bash
podman compose -f docker-compose.yml up -d
```

### Verifica que quedó correctamente
Entra al contenedor:
```bash
podman exec -it footballer_postgres psql -U footballer_user -d footballer_db
```

### 2. Configuración del Entorno de Python

1.  **Crea y activa el entorno virtual:**

    ```bash
     # Crear el entorno virtual (si no existe)
    python -m venv .venv

    # Activar en Windows (PowerShell)
    .venv\Scripts\Activate.ps1

    # Activar en Linux/macOS
    source .venv/bin/activate
    ```

2.  **Instala las dependencias:**

    ```bash
    # Actualiza pip
    python -m pip install --upgrade pip
    
    # Instala Django
    pip install django

    # Instala librerias
    pip install -r requirements.txt
    ```

### 3. Configuración de Variables de Entorno

1.  **Crea el archivo `.env`:**
    Copia el contenido del archivo `.env.example` (si existe) o crea un nuevo archivo `.env` en la raíz del proyecto.

2.  **Añade las siguientes variables:**
    Asegúrate de que las credenciales de la base de datos coincidan con las definidas en `docker-compose.yml`.

    ```ini
    # Clave secreta de Django (puedes generar una nueva)
    SECRET_KEY='django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxx'

    # Activa el modo debug solo para desarrollo
    DEBUG=True

    # Configuración de la Base de Datos
    POSTGRES_DB=footballer_db
    POSTGRES_USER=footballer_user
    POSTGRES_PASSWORD=footballer_pass
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

### 4. Migraciones y Datos Iniciales

1.  **Aplica las migraciones de la base de datos:**
    Esto creará las tablas necesarias para los modelos de Django.

    ```bash
    python manage.py migrate
    ```

2.  **Crea un superusuario:**
    Necesitarás un usuario para acceder al panel de administración de Django. Sigue las instrucciones en la terminal.

    ```bash
    python manage.py createsuperuser
    ```

3.  **Puebla la base de datos con datos de prueba:**
    Este comando llenará las tablas con datos ficticios de federaciones, ligas, equipos, etc.

    ```bash
    python manage.py seed_data
    ```

### 5. Ejecutar el Servidor de Desarrollo

Una vez completados todos los pasos, puedes iniciar el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

-   **Panel de Administración:** Accede a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e inicia sesión con las credenciales del superusuario que creaste.
-   **Media Files:** Los archivos subidos (como las fotos de las sedes) se guardarán en el directorio `mediafiles/`.

---

## Estructura del Proyecto

-   `footballer_project/`: Contiene la configuración principal del proyecto Django (`settings.py`, `urls.py`).
-   `core/`: Es la aplicación principal donde residen los modelos, la lógica de negocio y los comandos de gestión.
-   `docs/specs/`: Contiene la documentación de diseño y planificación para cada incremento de trabajo (Specs-Driven Development).
-   `Requerimiento/`: Contiene los documentos de requisitos y épicas que definen el trabajo a realizar.
-   `manage.py`: Utilidad de línea de comandos de Django.
-   `docker-compose.yml`: Define el servicio de la base de datos PostgreSQL.
-   `requirements.txt`: Lista de dependencias de Python.
-   `.env`: Archivo para variables de entorno (no debe ser versionado).
