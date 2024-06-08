"""Modulo con funciones utiles para manipular una base de datos"""
from sqlite3 import Connection, Error
from datetime import datetime


def obtener_todo(db: Connection, query: str, params: tuple | None = None):
    """
    Obtiene todas las filas de una tabla con SELECT * FROM tabla
    :param db: Conexion a base de datos sqlite3
    :param query: str(SELECT * FROM tabla)
    :param params: tupla de parametros para la query
    :return: lista con resultados o lista vacia
    """
    tabla = []

    try:
        tabla = db.execute(query, params).fetchall()
    except Error as err:
        # En caso de error, exportarlo a un archivo de texto
        with open('log.txt', 'a') as f:
            f.write(f'\n{datetime.now()} - {err}')
        print(f'A ocurrido un error: {err}')

    return tabla


def insertar_fila(db: Connection, query: str, vals: tuple):
    """
    Inserta datos en una tabla con INSERT INTO tabla(col1, col2, ...) VALUES (val1, val2, ...)
    :param db: Conexion a base de datos sqlite3
    :param query: str(INSERT INTO ... VALUES ...)
    :param vals: valores a ingresar desde una tupla
    :return: True o False dependiendo el resultado de la insercion
    """
    try:
        db.execute(query, parameters=vals)
    except Error as err:
        # En caso de error, exportarlo a un archivo de texto
        with open('log.txt', 'a') as f:
            f.write(f'\n{datetime.now()} - {err} - INSERT: {vals}')
        return False
    return True
