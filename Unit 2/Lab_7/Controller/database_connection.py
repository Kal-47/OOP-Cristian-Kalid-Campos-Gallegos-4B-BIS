import mysql.connector
from mysql.connector import Error
from Controller.config import DB_config


class Database_connection:
    def __init__(self):
        self.config = DB_config

    def get_connection(self):
        """Abre la conexión. Lanza ConnectionError con el motivo real si falla."""
        try:
            conexion = mysql.connector.connect(**self.config)
        except Error as e:
            raise ConnectionError(f"No se pudo conectar con MySQL: {e}") from e
        return conexion

    def ejecutar_consulta(self, query, params=()):
        """Devuelve una lista de filas (vacía si no hay coincidencias).
        Lanza ConnectionError si la conexión o la consulta fallan."""
        conexion = self.get_connection()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            raise ConnectionError(f"Error en la consulta SQL: {e}") from e
        finally:
            cursor.close()
            conexion.close()

    def ejecutar_comando(self, query, params=()):
        """Para INSERT/UPDATE/DELETE: ejecuta, confirma (commit) y devuelve las filas afectadas.
        Lanza ConnectionError si la conexión o la consulta fallan."""
        conexion = self.get_connection()
        cursor = conexion.cursor()
        try:
            cursor.execute(query, params)
            conexion.commit()
            return cursor.rowcount
        except Error as e:
            conexion.rollback()
            raise ConnectionError(f"Error en la consulta SQL: {e}") from e
        finally:
            cursor.close()
            conexion.close()
