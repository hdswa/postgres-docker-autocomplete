"""Utilidades para el completado de sql"""

from functools import cached_property
from logging import getLogger

import pglast.parser
from base_datos import BaseDatos, Repositorio
from lsprotocol.types import CompletionItem, CompletionItemKind

logger = getLogger(__name__)


def posicion_absoluta(texto: str, linea: int, caracter: int) -> int:
    """Determina la posicion absoluta desde el inicio de la cadena dentro del texto dada la linea y el caracter"""
    lineas = texto.splitlines()

    if linea >= len(lineas):
        raise ValueError("El número de línea excede el número de líneas en el texto.")

    # Comprobar si el carácter está dentro del rango de la línea
    if caracter > len(lineas[linea]):
        raise ValueError("El número de carácter excede la longitud de la línea.")

    # Sumar la longitud de todas las líneas anteriores, incluyendo los saltos de línea
    posicion = sum(len(lineas[i]) + 1 for i in range(linea))  # +1 para contar el salto de línea

    # Añadir el desplazamiento del carácter en la línea actual
    posicion += caracter

    return posicion


class Completador:
    """Servicio de completado de palabras dentro de un fichero sql"""
    def __init__(self, bd_servidor, bd_usuario, bd_puerto, bd_nombre, bd_clave):
        """Constructor"""
        base_datos = BaseDatos(
            host=bd_servidor,
            puerto=bd_puerto,
            base_datos=bd_nombre,
            usuario=bd_usuario,
            clave=bd_clave,
        )
        self.repositorio = Repositorio(base_datos)

    @cached_property
    def _cache_tablas(self) -> list[str]:
        return self.repositorio.tablas()
    
    @cached_property
    def _cache_columnas(self) -> dict[str, list[str]]:
        columnas = {}
        for tabla in self._cache_tablas:
            columnas[tabla] = self.repositorio.columnas(tabla)
        return columnas
    
    def completar(self, sql: str, linea: int, columna: int) -> list[CompletionItem]:
        
        """Dada una consulta, y una posicion en el texto devuelve los resultados del completado"""
        resultado: list[CompletionItem] = []

        posicion = posicion_absoluta(sql, linea, columna)
        tokens = pglast.parser.scan(sql)
        tokens_previos = [token for token in tokens if token.start < posicion]
        token_cursor = tokens_previos[-1]

        #select * from Chile where Chile.f
        #token_cursor= 'f' = token_previos[-1]
        #tabla_token_cursor= 'Chile' = token_previos[-3]
        #token_previos[-2] = '.'
        if token_cursor.name == "IDENT":
            palabra = sql[token_cursor.start : token_cursor.end + 1]
            if(sql[tokens_previos[-2].start:tokens_previos[-2].end+1] == "."):
                columna=palabra
                tabla_token_cursor=tokens_previos[-3]
                tabla = sql[tabla_token_cursor.start : tabla_token_cursor.end + 1]
                columnas = self._completar_columnas(tabla, columna)
                resultado += [CompletionItem(label=col, kind=CompletionItemKind.Field) for col in columnas]
            else:
                tablas = self._completar_tablas(palabra)
                resultado += [CompletionItem(label=table, kind=CompletionItemKind.Text) for table in tablas]

        return resultado

    def _completar_tablas(self, palabra: str) -> list[str]:
        logger.info(f"Completando tabla para palabra '{palabra}'")
        tablas = [tabla for tabla in self._cache_tablas if tabla.startswith(palabra)]
        return tablas

    def _completar_columnas(self, tabla: str, palabra: str) -> list[str]:
        logger.info(f"Completando columna para tabla '{tabla}' y palabra '{palabra}'")
        columnas = self._cache_columnas.get(tabla, [])
        return [columna for columna in columnas if columna.startswith(palabra)]
    


