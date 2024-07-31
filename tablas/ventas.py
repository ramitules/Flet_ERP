from sqlite3 import Connection
from tablas.tabladb import TablaDB
from tablas.usuarios import UsuariosDB
from tablas.estados import TransaccionEstadosDB


class VentasDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Ventas". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('fecha_hora', 'id_cliente', 'id_usuario', 'total', 'descuento', 'recargo', 'estado', 'nota')
        super().__init__(db=db, tabla='Ventas', columnas=columnas)
        # Llaves foraneas
        self.clientes = ClientesDB(self._db)
        self.usuarios = UsuariosDB(self._db)
        self.estados = TransaccionEstadosDB(self._db)
        # DataFrame con columnas modificadas para mostrar nombre en lugar del ID
        self.df_fk = self.cargar_fk()

    def cargar_fk(self):
        df_aux = self.df.copy()  # Conservar el DataFrame original

        # Aplicar funcion a cada columna con llaves foraneas
        df_aux['id_cliente'] = df_aux['id_cliente'].apply(lambda v: self.clientes.df.loc[v, 'nombre'])
        df_aux['id_usuario'] = df_aux['id_usuario'].apply(lambda v: self.usuarios.df.loc[v, 'usuario'])
        df_aux['estado'] = df_aux['estado'].apply(lambda v: self.estados.df.loc[v, 'nombre'])

        return df_aux


class ClientesDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Clientes". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', 'email', 'telefono', 'direccion')
        super().__init__(db=db, tabla='Clientes', columnas=columnas)


class VentasDetalle(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "VentasDetalle". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('id_venta', 'id_producto', 'cantidad')
        super().__init__(db=db, tabla='VentasDetalle', columnas=columnas)
