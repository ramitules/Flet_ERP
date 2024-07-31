from sqlite3 import Connection
from tablas.tabladb import TablaDB
from tablas.usuarios import UsuariosDB
from tablas.estados import TransaccionEstadosDB


class ComprasDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Compras". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('fecha_hora', 'usuario', 'proveedor', 'total', 'estado', 'nota')
        super().__init__(db=db, tabla='Compras', columnas=columnas)
        # Llaves foraneas
        self.usuarios = UsuariosDB(self._db)
        self.proveedores = ProveedoresDB(self._db)
        self.estados = TransaccionEstadosDB(self._db)
        # DataFrame con columnas modificadas para mostrar nombre en lugar del ID
        self.df_fk = self.cargar_fk()

    def cargar_fk(self):
        df_aux = self.df.copy()  # Conservar el DataFrame original

        # Aplicar funcion a cada columna con llaves foraneas
        df_aux['usuario'] = df_aux['usuario'].apply(lambda v: self.usuarios.df.loc[v, 'usuario'])
        df_aux['proveedor'] = df_aux['proveedor'].apply(lambda v: self.proveedores.df.loc[v, 'nombre'])
        df_aux['estado'] = df_aux['estado'].apply(lambda v: self.estados.df.loc[v, 'nombre'])

        return df_aux


class ProveedoresDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Proveedores". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', 'contacto', 'numero', 'mail', 'direccion')
        super().__init__(db=db, tabla='Proveedores', columnas=columnas)


class ComprasDetalleDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "ComprasDetalle". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('id_compra', 'id_producto', 'cantidad', 'precio_unitario')
        super().__init__(db=db, tabla='ComprasDetalle', columnas=columnas)

