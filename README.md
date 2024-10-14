# Tablero Central de Ejecuciones

Este proyecto es una aplicación de interfaz gráfica creada con `tkinter` para facilitar la ejecución de consultas SQL y scripts de Python mediante una interfaz interactiva. El proyecto incluye funciones de manejo de fechas, selección de archivos y conexión a una base de datos SQL Server, permitiendo al usuario realizar consultas y exportar los resultados a un archivo `.txt`.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos y módulos:

### 1. `main.py` (Script principal)

**Descripción**: Crea la interfaz gráfica para seleccionar y ejecutar consultas SQL y scripts. Utiliza `tkinter` para la creación de la interfaz, `tkcalendar` para la selección de fechas, y `subprocess` para la ejecución de scripts de Python externos.

**Funciones principales**:

- `mostrar_opcion()`: Muestra la opción seleccionada en un `Combobox`.
- `ejecutar_consulta()`: Captura datos de la interfaz, realiza una consulta SQL, y guarda el resultado en un archivo `.txt`.
- `ejecutar_script(nombre_script)`: Ejecuta un script de Python y muestra un mensaje de éxito o error.
- `seleccionar_archivo()`: Permite al usuario seleccionar un archivo a través de un explorador de archivos.
- `actualizar_estado_campos()`: Habilita o deshabilita campos según la selección en el `Combobox`.
- `capturar_datos()`: Captura los valores de los campos de entrada.

### 2. `config.py` (Módulo de configuración)

**Descripción**: Este módulo utiliza `dotenv` para cargar variables de entorno desde un archivo `.env`, que contiene rutas a las consultas SQL y credenciales para la conexión a la base de datos.

**Variables**:

- `Consulta`: Ruta del archivo de la consulta SQL.
- `credenciales`: Ruta del archivo JSON que contiene las credenciales de acceso a la base de datos.


### 3. `utils.py` (Módulo de utilidades)

**Descripción**: Este módulo incluye funciones auxiliares para la conexión a la base de datos, la lectura de archivos SQL, y la carga de credenciales desde un archivo JSON.

**Funciones**:

- `lectura_planos(ruta_archivo: str)`: Lee una consulta SQL desde un archivo de texto y la devuelve como un string.
- `Lectura_json(ruta_archivo: str)`: Carga y devuelve el contenido de un archivo JSON, usado para cargar las credenciales de la base de datos.
- `conexion_base_de_datos`:Establece la conexión con una base de datos SQL Server y ejecuta una consulta SQL.
   - Devuelve los resultados en un DataFrame de pandas.
   - Cierra la conexión después de la consulta, y maneja errores relacionados con la conexión.

## Características

- **Interfaz gráfica con tkinter**: Permite al usuario seleccionar opciones, ingresar datos, y ejecutar scripts.
- **Ejecución de consultas SQL**: Genera consultas SQL personalizadas y las ejecuta contra un servidor SQL Server.
- **Manejo de archivos**: Ofrece la opción de seleccionar archivos mediante un explorador y de manejar datos masivos o individuales.
- **Automatización**: Ejecuta scripts de Python externos y maneja el resultado de las consultas de manera automática.
- **Módulos auxiliares**: Se apoya en dos módulos adicionales para la gestión de configuraciones y utilidades de conexión.

## Requisitos

- Python 3.x
- Librerías de Python:
  - `tkinter`
  - `tkcalendar`
  - `pyodbc`
  - `pandas`
  - `dotenv`
- Conexión a un servidor de base de datos SQL Server.

## Estructura del Proyecto

```plaintext
├── main.py               # Script principal con la interfaz de usuario
├── config.py             # Módulo para cargar configuraciones desde el archivo .env
├── utils.py              # Módulo con funciones auxiliares para la conexión y manejo de archivos
├── .env                  # Archivo con las rutas a consultas SQL y credenciales
└── credenciales.json     # Archivo JSON con las credenciales de la base de datos
```

###  Archivo `credenciales.json` (Archivo JSON de credenciales)
**Descripción**: Archivo JSON que contiene la información de acceso a la base de datos SQL Server.

**Ejemplo**:
```json
{
    "SQLSERVER": {
        "Servidor": "nombre_del_servidor",
        "Usuario": "tu_usuario",
        "Password": "tu_contraseña",
        "Database": "nombre_de_la_base_de_datos"
    }
}
```

###  Archivo `.env` (Archivo de configuración)
**Descripción**: Este archivo contiene las rutas de las consultas SQL y el archivo JSON con las credenciales necesarias para conectarse a la base de datos.

**Ejemplo**:
```.env

Query=path_to_your_sql_query.sql 
credenciales=path_to_your_credentials.json
``` 