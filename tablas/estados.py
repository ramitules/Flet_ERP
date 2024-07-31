from sqlite3 import Connection
from tablas.tabladb import TablaDB


class TransaccionEstadosDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "TransaccionEstados". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', )
        super().__init__(db=db, tabla='TransaccionEstados', columnas=columnas)
