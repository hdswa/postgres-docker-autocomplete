# Configuración del Entorno de Desarrollo

Este documento proporciona instrucciones para configurar el entorno de desarrollo, incluyendo cómo levantar la base de datos y cómo instalar las dependencias de Python del servidor.

## Requisitos Previos

- Docker y Docker Compose instalados en tu máquina.
- Python 3.8 o superior.
- `pip` (el gestor de paquetes de Python).

## Levantar la Base de Datos

1. Asegúrate de que Docker y Docker Compose están instalados y corriendo en tu máquina.
2. Navega al directorio del proyecto donde se encuentra el archivo `docker-compose.yml`.
3. Ejecuta los siguientes comandos para levantar la base de datos:

    ```sh
    docker-compose down
    docker-compose up
    ```

4. Una vez que los contenedores estén corriendo, accede al contenedor de PostgreSQL:

    ```sh
    docker exec -it postgres_container psql -U admin -d mydb
    ```

5. Puedes verificar que la base de datos está funcionando correctamente ejecutando una consulta simple:

    ```sql
    select * from "Argentina";
    ```

## Instalar Dependencias de Python

1. Asegúrate de tener Python 3.8 o superior instalado en tu máquina.
2. Navega al directorio del proyecto donde se encuentra el archivo `requirements.txt`.
3. Crea un entorno virtual (opcional pero recomendado):

    ```sh
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

        ```sh
        venv\Scripts\activate
        ```

5. Instala las dependencias de Python usando `pip`:

    ```sh
    pip install -r requirements.txt
    ```

## Ejecutar el Servidor

1. Asegúrate de que el entorno virtual está activado (si estás usando uno).
2. Ejecuta el programa dependiendo de los casos de uso probador:

    ```sh
    python src/cliente.py --fichero examples/completado_tabla.sql --linea 1 --caracter 15 --bd-servidor localhost --bd-usuario admin --bd-puerto 5433 --bd-nombre mydb --bd-clave adminpassword

    python src/cliente.py --fichero examples/completado_columna.sql --linea 1 --caracter 33 --bd-servidor localhost --bd-usuario admin --bd-puerto 5433 --bd-nombre mydb --bd-clave adminpassword

    python src/cliente.py --fichero examples/completado_columna.sql --linea 1 --caracter 32 --bd-servidor localhost --bd-usuario admin --bd-puerto 5433 --bd-nombre mydb --bd-clave adminpassword
    ```


Con estos pasos, deberías tener un entorno de desarrollo completamente funcional. Si encuentras algún problema, revisa los logs y asegúrate de que todos los servicios están corriendo correctamente.