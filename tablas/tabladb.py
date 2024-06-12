from sqlite3 import Connection
from tablas.func_db import insertar_fila
import pandas as pd


class TablaDB:
    def __init__(self, db: Connection, tabla: str, columnas: tuple):
        """
        Clase base para manipular una tabla de la base de datos. Se manipula
        principalmente con un DataFrame (self.df)
        :param db: Conexion a la base de datos (sqlite3.Connection)
        :param tabla: nombre de la tabla a acceder
        :param columnas: nombre de las columnas que contiene la tabla
        """
        self._db = db
        self.__columnas = columnas
        self.__tabla = tabla
        self.df = pd.read_sql(sql=f'SELECT * FROM {self.__tabla}', con=self._db, index_col='id')

    def insertar(self, vals: tuple):
        query = (f'INSERT INTO {self.__tabla} ({', '.join(self.__columnas)}) '
                 f'VALUES ({', '.join('?' * len(self.__columnas))})')
        return insertar_fila(self._db, query, vals)

    def cargar_fk(self):
        """Cargar llaves foraneas con el valor asociado a dicha tabla (id, [nombre])"""
        pass
