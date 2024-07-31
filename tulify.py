import flet as ft
from controles.main_inventario import Inventario
from controles.main_compras import Compras
from controles.main_ventas import Ventas
from controles.logo import Logo
from sqlite3 import Connection


class Tulify(ft.Row):
    def __init__(self, pagina: ft.Page):
        super().__init__(expand=True)
        self.pagina = pagina
        self.pagina.window_maximized = True
        self.pagina.title = 'Tulify'
        self.pagina.fonts = {'fuente_logo': 'https://raw.githubusercontent.com/google/fonts/main/apache/rancho/Rancho-Regular.ttf'}
        self.pagina.theme = ft.Theme(color_scheme_seed='blue')

        self.db = Connection('base.db')
        self.destinos = [
            ft.NavigationRailDestination(
                icon=ft.icons.INVENTORY_2,
                selected_icon=ft.icons.INVENTORY_2_OUTLINED,
                label='Inventario'),
            ft.NavigationRailDestination(
                icon=ft.icons.SHOPPING_CART,
                selected_icon=ft.icons.SHOPPING_CART_OUTLINED,
                label='Compras'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SELL,
                selected_icon=ft.icons.SELL_OUTLINED,
                label='Ventas'
            )
        ]
        self.controls = [
            ft.NavigationRail(
                selected_index=0,
                label_type=ft.NavigationRailLabelType.ALL,
                min_width=100,
                min_extended_width=400,
                leading=Logo(),
                group_alignment=-0.9,
                on_change=self.cambiar_cuerpo,
                destinations=self.destinos
            ),
            ft.VerticalDivider(width=1),
            Inventario(self.db)
        ]

        self.pagina.add(self)

    def cambiar_cuerpo(self, e: ft.ControlEvent):
        """
        Cambiar informacion del cuerpo de la pagina
        :param e: evento de ft.NavigationRail['on_change']
        """
        i = e.control.selected_index
        del self.controls[2]
        if i == 0:
            self.controls.append(Inventario(self.db))
        elif i == 1:
            self.controls.append(Compras(self.db))
        elif i == 2:
            self.controls.append(Ventas(self.db))

        self.update()
        '''
        label = self.destinos[i].label
        texto_cuerpo = self.controls[-1].controls[-1]
        texto_cuerpo.value = label
        texto_cuerpo.update()
        '''
