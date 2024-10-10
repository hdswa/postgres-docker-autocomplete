"""Cliente utilizado sobre todo para pruebas"""
import argparse
import asyncio
import logging
from pathlib import Path
from sys import stdout

from lsprotocol.types import (
    ClientCapabilities,
    CompletionList,
    CompletionParams,
    InitializeParams,
    Position,
    TextDocumentIdentifier,
    InitializeResult,
)
from pygls.lsp.client import BaseLanguageClient


logger = logging.getLogger(__name__)


async def main():
    """Ejecucion del cliente que pide el completado dado un fichero, una linea y un character"""
    cliente = BaseLanguageClient("lsppg", "1.0.0")

    await cliente.start_io("python", "src/servidor.py")

    parser = argparse.ArgumentParser(description="levanta un servidor lsp y le envia una peticion de completado")
    parser.add_argument("--fichero", type=str, help="fichero con la consulta", required=True)
    parser.add_argument("--linea", type=int, help="linea del fichero donde completar", required=True)
    parser.add_argument("--caracter", type=int, help="caracter de la linea del fichero donde completar", required=True)

    parser.add_argument("--bd-servidor", type=str, help="servidor de la base de datos", required=True)
    parser.add_argument("--bd-usuario", type=str, help="usuario de la base de datos", required=True)
    parser.add_argument("--bd-puerto", type=int, help="puerto de la base de datos", required=True)
    parser.add_argument("--bd-nombre", type=str, help="nombre de la base de datos", required=True)
    parser.add_argument("--bd-clave", type=str, help="clave de la base de datos", required=True)
    
    args = parser.parse_args()

    init_params = InitializeParams(
        process_id=None,
        root_uri=None,
        capabilities=ClientCapabilities(),
        initialization_options={
            "bd_servidor": args.bd_servidor,
            "bd_usuario": args.bd_usuario,
            "bd_puerto": args.bd_puerto,
            "bd_nombre": args.bd_nombre,
            "bd_clave": args.bd_clave,
        },
    )
    init_result: InitializeResult = await cliente.initialize_async(init_params)
    logger.info(f"Inicialización completada")


    uri = Path(args.fichero).absolute().as_uri()
    params = CompletionParams(
        text_document=TextDocumentIdentifier(uri=uri), position=Position(line=args.linea, character=args.caracter)
    )
    resultado = await cliente.text_document_completion_async(params)
   
    if resultado:
        logger.info("Recibido resultado")
        if isinstance(resultado, CompletionList):
            resultado = resultado.items
        for item in resultado:
            logger.info(f"\t{item.label}")
    else:
        logger.info("No se recibio respuesta")

    await cliente.stop()


if __name__ == "__main__":
    logging.basicConfig(stream=stdout, level=logging.INFO)
    logger.info("Iniciando cliente")
    asyncio.run(main())
