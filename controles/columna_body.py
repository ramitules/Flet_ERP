import flet as ft


class Columna(ft.Column):
    def __init__(self):
        super().__init__(expand=True, run_spacing=8)
        self.tabla = None  # TablaDB(db)
        self.controls = [
            ft.Row(height=250, alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row(height=250, alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ]

    def cargar_filas(self):
        pass
