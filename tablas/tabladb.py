from sqlite3 import Connection
from tablas.func_db import obtener_todo, insertar_fila
import pandas as pd


class TablaDB:
    def __init__(self, db: Connection, tabla: str, columnas: tuple):
        self.db = db
        self.columnas = columnas
        self.tabla = tabla
        self.df = pd.read_sql(sql=f'SELECT * FROM {self.tabla}', con=self.db)

    def insertar(self, vals: tuple):
        query = (f'INSERT INTO {self.tabla} ({', '.join(self.columnas)}) '
                 f'VALUES ({', '.join('?' * len(self.columnas))})')
        return insertar_fila(self.db, query, vals)
