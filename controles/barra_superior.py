import flet as ft


class BarraSuperior(ft.AppBar):
    def __init__(self):
        super().__init__(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            toolbar_height=75,
        )
        self.items_appbar = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]
        self.actions = ft.PopupMenuButton(items=self.items_appbar)
        actions = [
            ft.Container(
                content=ft.PopupMenuButton(
                    items=self.items_appbar
                ),
                margin=ft.margin.only(left=50, right=25)
            )
        ]
