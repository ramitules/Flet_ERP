import flet as ft


class Logo(ft.Text):
    def __init__(self):
        super().__init__(
            value='Tul',
            font_family='fuente_logo',
            color=ft.colors.BLUE_800,
            theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            spans=[ft.TextSpan('ify', ft.TextStyle(color=ft.colors.BLACK87))]
        )
