import flet as ft
from pandas import DataFrame
from tablas.compras import ComprasDB, ComprasDetalleDB, ProveedoresDB
from sqlite3 import Connection
from controles.columna_body import Columna
from controles.planilla import Planilla
from datetime import timedelta, datetime


class Compras(Columna):
    def __init__(self, db: Connection):
        super().__init__()
        self.tabla = ComprasDB(db)

        self.cargar_filas()

    def cargar_filas(self):
        self.controls[1].controls = [
            CompPlanilla(self.tabla.df_fk)
        ]

    def __set_contenido_mes(self):
        ahora = datetime.today()
        un_mes = ahora - timedelta(days=30)
        fechas = self.tabla.df['fecha_hora']

class CompPlanilla(Planilla):
    def __init__(self, compras: DataFrame):
        super().__init__(compras)
        self.titulos = ('Fecha y hora', 'Usuario', 'Proveedor', 'Total', 'Estado', 'Nota')
        # Columnas
        self.cargar_columnas()
        # Filas
        self.cargar_celdas()
