import flet as ft


class FilaCuerpo(ft.Row):
    def __init__(self):
        """
        Fila predeterminada para el cuerpo del programa
        """
        super().__init__()
        self.height = 250
        self.alignment = ft.MainAxisAlignment.SPACE_EVENLY
