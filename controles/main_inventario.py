import flet as ft
from controles.fila import FilaCuerpo


class Inventario(ft.Column):
    def __init__(self):
        super().__init__(expand=True, run_spacing=8)
        self.controls = [
            Fila1(),
            Fila2()
        ]


class Fila1(FilaCuerpo):
    def __init__(self):
        super().__init__()
        self.controls = [
            InvStock(),
            InvProveedores(),
            InvStock()
        ]


class Fila2(FilaCuerpo):
    def __init__(self):
        super().__init__()
        self.controls = [
            InvPlanilla()
        ]


class InvStock(ft.Card):
    def __init__(self):
        super().__init__(width=400)
        self.content = self.set_contenido()

    def set_contenido(self):
        en_stock = 6
        sin_stock = 4
        porcentaje = (en_stock / (en_stock + sin_stock))
        boton_stock = ft.TextButton(
            content=ft.Text(
                f'En stock\n{en_stock}',
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.BLUE_900
            )
        )
        boton_s_stock = ft.TextButton(
            content=ft.Text(
                f'Sin stock\n{sin_stock}',
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.BLUE_900
            )
        )

        controles_columna = [
            ft.TextButton(content=ft.Text('Stock', size=20)),
            ft.Column(
                controls=[
                    ft.ProgressBar(porcentaje, bgcolor="#eeeeee", width=350),
                    ft.Text(
                        f'{porcentaje * 100}% disponible',
                        weight=ft.FontWeight.W_600
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[boton_stock, boton_s_stock],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]

        contenido = ft.Column(
            controls=controles_columna,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return contenido


class InvProveedores(ft.Card):
    def __init__(self):
        super().__init__(width=400)
        self.content = self.set_contenido()

    def set_contenido(self):
        controles_columna = [
            ft.TextButton(content=ft.Text('Proveedores', size=20))
        ]

        contenido = ft.Column(
            controls=controles_columna,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return contenido


class InvPlanilla(ft.GridView):
    def __init__(self):
        super().__init__(expand=True)
        self.titulos = (
            'ID',
            'SKU',
            'Nombre',
            'Descripcion',
            'Categoria',
            'Subcategoria',
            'Marca',
            'Modelo',
            'Precio costo',
            'Precio venta',
            'Stock',
            'Ubicacion',
            'Ultimo ingreso'
        )

        self.runs_count = len(self.titulos)
        # Titulos como texto
        self.controls = [ft.Text(value=c, weight=ft.FontWeight.W_900) for c in self.titulos]
        # Datos
        self.controls.extend([ft.Text(value=c, weight=ft.FontWeight.W_900) for c in self.titulos])

    def cargar_celdas(self):
        """
        Carga de celdas por columna
        :return:
        """
        controles = []

        return controles
