from sqlite3 import Connection
from tablas.tabladb import TablaDB


class UsuariosDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Usuarios". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('usuario', 'contrasena', 'email', 'rol')
        super().__init__(db=db, tabla='Usuarios', columnas=columnas)
        # Llaves foraneas
        self.roles = RolesDB(self._db)
        # DataFrame con columnas modificadas para mostrar nombre en lugar del ID
        self.df_fk = self.cargar_fk()

    def cargar_fk(self):
        df_aux = self.df.copy()  # Conservar el DataFrame original

        # Aplicar funcion a cada columna con llaves foraneas
        df_aux['rol'] = df_aux['rol'].apply(lambda v: self.roles.df.loc[v, 'nombre'])

        return df_aux


class RolesDB(TablaDB):
    def __init__(self, db: Connection):
        """
        Tabla "Roles". Utilizar self.df para trabajar con Pandas.DataFrame
        :param db: Conexion a base de datos sqlite3.Connection
        """
        columnas = ('nombre', )
        super().__init__(db=db, tabla='Roles', columnas=columnas)
