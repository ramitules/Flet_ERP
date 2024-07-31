import flet as ft
from pandas import DataFrame
from tablas.ventas import VentasDB
from sqlite3 import Connection
from controles.columna_body import Columna
from controles.planilla import Planilla


class Ventas(Columna):
    def __init__(self, db: Connection):
        super().__init__()
        self.tabla = VentasDB(db)

        self.cargar_filas()

    def cargar_filas(self):
        self.controls[1].controls = [
            VenPlanilla(self.tabla.df_fk)
        ]


class VenPlanilla(Planilla):
    def __init__(self, ventas: DataFrame):
        super().__init__(ventas)
        self.titulos = ('Fecha y hora', 'Cliente', 'Usuario', 'Total', 'Descuento', 'Recargo', 'Estado', 'Nota')
        # Columnas
        self.cargar_columnas()
        # Filas
        self.cargar_celdas()
