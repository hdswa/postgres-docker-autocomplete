"""Servidor LSP"""
import logging
from pathlib import Path
from urllib.parse import urlparse

from completado import Completador
from lsprotocol.types import TEXT_DOCUMENT_COMPLETION, CompletionList, CompletionParams,InitializeParams
from pygls.server import LanguageServer

VERSION = "1.0.0"

logger = logging.getLogger(__name__)


class Servidor(LanguageServer):
    """Implementacion del servidor LSP"""

    def __init__(self):
        """Constructor"""
        super().__init__(name="lsppg", version=VERSION)

    def inicializar_completador(self, bd_servidor, bd_usuario, bd_puerto, bd_nombre, bd_clave):
        self.completador = Completador(
            bd_servidor=bd_servidor,
            bd_usuario=bd_usuario,
            bd_puerto=bd_puerto,
            bd_nombre=bd_nombre,
            bd_clave=bd_clave,
        )
sql_server = Servidor()


# Obtener autocompletado desde el catálogo de PostgreSQL
@sql_server.feature(TEXT_DOCUMENT_COMPLETION)
def completions(server: Servidor, params: CompletionParams):
    """Maneja la peticion de completado"""
    logger.info("Recibida peticion de completado")

    uri = urlparse(params.text_document.uri)
    ruta_fichero = Path(uri.path.lstrip("/"))

    with ruta_fichero.open() as fichero:
        contenido = fichero.read()

        logger.info(f"El contenido:\n{contenido}")
        resultado = server.completador.completar(contenido, params.position.line, params.position.character)

        return CompletionList(is_incomplete=False, items=resultado)

@sql_server.feature("initialize")
def initialize(server: Servidor, params: InitializeParams):
    """Maneja la peticion de inicialización"""
    logger.info("Recibida peticion de inicialización")
    opciones = params.initialization_options
    print("=====================================")
    print("opciones",opciones)
    server.inicializar_completador(
        bd_servidor=opciones["bd_servidor"],
        bd_usuario=opciones["bd_usuario"],
        bd_puerto=opciones["bd_puerto"],
        bd_nombre=opciones["bd_nombre"],
        bd_clave=opciones["bd_clave"],
    )
    return {}
if __name__ == "__main__":
    logging.basicConfig(filename="lsppg.log", level=logging.INFO)
    logger.info("Iniciando servidor")
    sql_server.start_io()
