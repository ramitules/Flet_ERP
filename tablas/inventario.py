from sqlite3 import Connection
from tablas.tabladb import TablaDB


class InventarioDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = (
            'id', 'sku', 'nombre', 'descripcion', 'categoria', 'subcategoria', 'marca',
            'modelo', 'precio_costo', 'precio_venta', 'stock', 'ubicacion', 'ultimo_ingreso'
        )
        super().__init__(db=db, tabla='Inventario', columnas=columnas)


class InvProveedoresDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = ('id', 'nombre', 'contacto', 'numero', 'mail', 'direccion')
        super().__init__(db=db, tabla='InvProveedores', columnas=columnas)


class InvCategoriasDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = ('id', 'nombre')
        super().__init__(db=db, tabla='InvCategorias', columnas=columnas)


class InvSubCategoriasDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = ('id', 'categoria', 'nombre')
        super().__init__(db=db, tabla='InvSubcategorias', columnas=columnas)


class InvMarcasDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = ('id', 'nombre')
        super().__init__(db=db, tabla='InvMarcas', columnas=columnas)


class RefInvProveedoresDB(TablaDB):
    def __init__(self, db: Connection):
        columnas = ('id', 'nombre')
        super().__init__(db=db, tabla='RefInvProveedores', columnas=columnas)
