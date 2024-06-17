import flet as ft
from pandas import DataFrame
from tablas.inventario import InventarioDB
from sqlite3 import Connection
from validadores import filtrar_vacios, es_numerica


class Inventario(ft.Column):
    def __init__(self, db: Connection):
        super().__init__(expand=True, run_spacing=8)
        self.inventario = InventarioDB(db)
        self.controls = [
            ft.Row(height=250, alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row(height=250, alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ]

        self.cargar_filas()

    def cargar_filas(self):
        self.controls[1].controls = [
            InvPlanilla(self.inventario.df_fk)
        ]
        self.controls[0].controls = [
            ft.Card(width=400, content=self.__set_contenido_stock()),
            InvProveedores()
        ]

    def filtrar_stock(self, ev=None):
        del self.controls[1].controls[0]
        df_fk = self.inventario.df_fk.copy()
        df_fk = df_fk[df_fk['stock'] > 0]
        self.controls[1].controls = [InvPlanilla(df_fk)]
        self.update()

    def filtrar_sin_stock(self, ev=None):
        del self.controls[1].controls[0]
        df_fk = self.inventario.df_fk.copy()
        df_fk = df_fk[df_fk['stock'] == 0]
        self.controls[1].controls = [InvPlanilla(df_fk)]
        self.update()

    def quitar_filtro(self, ev=None):
        del self.controls[1].controls[0]
        self.controls[1].controls = [InvPlanilla(self.inventario.df_fk)]
        self.update()

    def __set_contenido_stock(self):
        cantidades = self.inventario.df['stock'].value_counts()

        if 0 in cantidades:
            sin_stock = cantidades[0]
        else:
            sin_stock = 0

        en_stock = len(self.inventario.df) - sin_stock
        porcentaje = (en_stock / (en_stock + sin_stock))
        boton_stock = ft.TextButton(
            content=ft.Text(
                f'En stock\n{en_stock}',
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.BLUE_900
            ),
            on_click=self.filtrar_stock
        )
        boton_s_stock = ft.TextButton(
            content=ft.Text(
                f'Sin stock\n{sin_stock}',
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.BLUE_900
            ),
            on_click=self.filtrar_sin_stock
        )

        controles_columna = [
            ft.TextButton(content=ft.Text('Stock', size=20), on_click=self.quitar_filtro),
            ft.Column(
                controls=[
                    ft.ProgressBar(porcentaje, bgcolor="#eeeeee", width=350),
                    ft.Text(
                        f'{int(porcentaje * 100)}% disponible',
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
    def __init__(self, inventario: DataFrame):
        self.inventario = inventario
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
        for i, fila in self.inventario.iterrows():
            self.rows.append(ft.DataRow([ft.DataCell(ft.Text(filtrar_vacios(v))) for v in fila]))
