import flet as ft
from pandas import DataFrame
from validadores import filtrar_vacios, es_numerica


class Planilla(ft.DataTable):
    def __init__(self, df: DataFrame):
        self.df = df
        self.titulos = tuple()
        super().__init__()

    def cargar_columnas(self):
        for titulo in self.titulos:
            self.columns.append(ft.DataColumn(
                label=ft.Text(titulo, weight=ft.FontWeight.W_600),
                numeric=es_numerica(titulo)
            ))

    def cargar_celdas(self):
        """
        Carga de celdas por fila
        """
        for i, fila in self.df.iterrows():
            self.rows.append(ft.DataRow([ft.DataCell(ft.Text(filtrar_vacios(v))) for v in fila]))
