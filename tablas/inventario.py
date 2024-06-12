from sqlite3 import Connection
from tablas.tabladb import TablaDB


class InventarioDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Inventario". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = (
            'sku', 'nombre', 'descripcion', 'categoria', 'subcategoria', 'marca',
            'modelo', 'precio_costo', 'precio_venta', 'stock', 'ubicacion', 'ultimo_ingreso'
        )
        super().__init__(db=db, tabla='Inventario', columnas=columnas)
        # Llaves foraneas
        self.inv_categorias = InvCategoriasDB(self._db)
        self.inv_sub_cat = InvSubCategoriasDB(self._db)
        self.inv_marcas = InvMarcasDB(self._db)
        # DataFrame con columnas modificadas para mostrar nombre en lugar del ID
        self.df_fk = self.cargar_fk()

    def cargar_fk(self):
        df_aux = self.df.copy()  # Conservar el DataFrame original

        # Aplicar funcion a cada columna con llaves foraneas para que devuelva columna 'nombre' en lugar de 'id'
        df_aux['categoria'] = df_aux['categoria'].apply(lambda v: self.inv_categorias.df.loc[v, 'nombre'])
        df_aux['subcategoria'] = df_aux['subcategoria'].apply(lambda v: self.inv_sub_cat.df.loc[v, 'nombre'])
        df_aux['marca'] = df_aux['marca'].apply(lambda v: self.inv_marcas.df.loc[v, 'nombre'])

        return df_aux


class InvProveedoresDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "InvProveedores". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', 'contacto', 'numero', 'mail', 'direccion')
        super().__init__(db=db, tabla='InvProveedores', columnas=columnas)


class InvCategoriasDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "InvCategorias". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', )
        super().__init__(db=db, tabla='InvCategorias', columnas=columnas)


class InvSubCategoriasDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "InvSubcategorias". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('categoria', 'nombre')
        super().__init__(db=db, tabla='InvSubcategorias', columnas=columnas)


class InvMarcasDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "InvMarcas". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', )
        super().__init__(db=db, tabla='InvMarcas', columnas=columnas)


class RefInvProveedoresDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "RefInvProveedores". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', )
        super().__init__(db=db, tabla='RefInvProveedores', columnas=columnas)
