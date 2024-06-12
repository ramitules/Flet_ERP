import flet as ft
from controles.fila import FilaCuerpo
from tablas.inventario import InventarioDB
from sqlite3 import Connection
from validadores import filtrar_vacios, es_numerica


class Inventario(ft.Column):
    def __init__(self, db: Connection):
        super().__init__(expand=True, run_spacing=8)
        self.db = db
        self.controls = [
            Fila1(),
            Fila2(self.db)
        ]


class Fila1(FilaCuerpo):
    def __init__(self, db: Connection | None = None):
        super().__init__()
        self.controls = [
            InvStock(),
            InvProveedores(),
            InvStock()
        ]


class Fila2(FilaCuerpo):
    def __init__(self, db: Connection | None = None):
        super().__init__()
        self.controls = [
            InvPlanilla(db)
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


class InvPlanilla(ft.DataTable):
    def __init__(self, db: Connection):
        self.db = db
        self.inventario = InventarioDB(self.db)
        self.titulos = (
            'SKU',
            'Nombre',
            'Descripcion',
            'Categoria',
            'Sub categoria',
            'Marca',
            'Modelo',
            'Precio costo',
            'Precio venta',
            'Stock',
            'Ubicacion',
            'Ultimo ingreso'
        )

        super().__init__(
            columns=[ft.DataColumn(
                ft.Text(t, weight=ft.FontWeight.W_600),
                numeric=es_numerica(t)
            ) for t in self.titulos]
        )
        # Datos
        self.cargar_celdas()

    def cargar_celdas(self):
        """
        Carga de celdas por fila
        """
        inventario = InventarioDB(self.db)
        for i, fila in inventario.df_fk.iterrows():
            self.rows.append(ft.DataRow([ft.DataCell(ft.Text(filtrar_vacios(v))) for v in fila]))
