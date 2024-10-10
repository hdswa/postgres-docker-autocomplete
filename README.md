# Configuración del Entorno de Desarrollo

Este documento proporciona instrucciones para configurar el entorno de desarrollo, incluyendo cómo levantar la base de datos y cómo instalar las dependencias de Python del servidor.

Autor: Felipe Ye Chen
Correo: yefelipe78@gmail.com


## Documentaición de cambios realizado
    https://docs.google.com/document/d/1A4qI3s-chSef3anDG6LPnCRY5iQaE78xwhA8RLDObBs/edit?usp=sharing
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
    SELECT * FROM "Chile";
    ```


## Instalar Dependencias de Python

1. Asegúrate de tener Python 3.8 o superior instalado en tu máquina.
2. Navega al directorio del proyecto donde se encuentra el archivo `requirements.txt`.
3. Crea un entorno virtual (opcional pero recomendado):

    ```sh
    python -m venv venv
    ```

4. Activa el entorno virtual:

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


## Requisitos adicionales 
1. Salida de Linea 1 caracter 33
    ```
    PS C:\Users\Felipe\Downloads\lsppg-main> python src/cliente.py --fichero examples/completado_columna.sql --linea 1 --caracter 33 --bd-servidor localhost --bd-usuario admin --bd-puerto 5433 --bd-nombre mydb --bd-clave adminpassword
    INFO:__main__:Iniciando cliente
    INFO:pygls.feature_manager:Registered builtin feature exit
    INFO:pygls.feature_manager:Registered builtin feature initialize
    INFO:pygls.feature_manager:Registered builtin feature initialized
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didChange
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didClose
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didOpen
    INFO:pygls.feature_manager:Registered builtin feature $/setTrace
    INFO:pygls.feature_manager:Registered builtin feature shutdown
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didChange
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didClose
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didOpen
    INFO:pygls.feature_manager:Registered builtin feature window/workDoneProgress/cancel
    INFO:pygls.feature_manager:Registered builtin feature workspace/didChangeWorkspaceFolders
    INFO:pygls.feature_manager:Registered builtin feature workspace/executeCommand
    INFO:pygls.protocol.json_rpc:Sending data: {"id": "d557f64e-4bd0-4e71-88e3-4c5ea2fcd954", "params": {"capabilities": {}, "processId": null, "rootPath": null, "rootUri": null, "workspaceFolders": null, "initializationOptions": {"bd_servidor": "localhost", "bd_usuario": "admin", "bd_puerto": 5433, "bd_nombre": "mydb", "bd_clave": "adminpassword"}}, "method": "initialize", "jsonrpc": "2.0"}
    INFO:__main__:Inicialización completada
    INFO:pygls.protocol.json_rpc:Sending data: {"id": "a32550a4-61ac-4fef-a4fe-665e8eeedaf4", "params": {"textDocument": {"uri": "file:///C:/Users/Felipe/Downloads/lsppg-main/examples/completado_columna.sql"}, "position": {"line": 1, "character": 33}}, "method": "textDocument/completion", "jsonrpc": "2.0"}
    INFO:__main__:Recibido resultado
    INFO:__main__:  fecha_creacion
    ```
2. Salida de Linea 1 Caracter 32
    ```
    PS C:\Users\Felipe\Downloads\lsppg-main> python src/cliente.py --fichero examples/completado_columna.sql --linea 1 --caracter 32 --bd-servidor localhost --bd-usuario admin --bd-puerto 5433 --bd-nombre mydb --bd-clave adminpassword
    INFO:__main__:Iniciando cliente
    INFO:pygls.feature_manager:Registered builtin feature exit
    INFO:pygls.feature_manager:Registered builtin feature initialize
    INFO:pygls.feature_manager:Registered builtin feature initialized
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didChange
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didClose
    INFO:pygls.feature_manager:Registered builtin feature notebookDocument/didOpen
    INFO:pygls.feature_manager:Registered builtin feature $/setTrace
    INFO:pygls.feature_manager:Registered builtin feature shutdown
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didChange
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didClose
    INFO:pygls.feature_manager:Registered builtin feature textDocument/didOpen
    INFO:pygls.feature_manager:Registered builtin feature window/workDoneProgress/cancel
    INFO:pygls.feature_manager:Registered builtin feature workspace/didChangeWorkspaceFolders
    INFO:pygls.feature_manager:Registered builtin feature workspace/executeCommand
    INFO:pygls.protocol.json_rpc:Sending data: {"id": "334a753e-466d-4071-9485-db2b3f80b816", "params": {"capabilities": {}, "processId": null, "rootPath": null, "rootUri": null, "workspaceFolders": null, "initializationOptions": {"bd_servidor": "localhost", "bd_usuario": "admin", "bd_puerto": 5433, "bd_nombre": "mydb", "bd_clave": "adminpassword"}}, "method": "initialize", "jsonrpc": "2.0"}
    INFO:__main__:Inicialización completada
    INFO:pygls.protocol.json_rpc:Sending data: {"id": "58c8e549-e0c6-496c-b1e7-b6618376f9f9", "params": {"textDocument": {"uri": "file:///C:/Users/Felipe/Downloads/lsppg-main/examples/completado_columna.sql"}, "position": {"line": 1, "character": 32}}, "method": "textDocument/completion", "jsonrpc": "2.0"}
    INFO:__main__:Recibido resultado
    ```
