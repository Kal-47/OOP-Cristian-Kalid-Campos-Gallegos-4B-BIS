from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.passw = passw
        self.db = Database_connection()

    def auth(self):
        """Devuelve el registro del usuario (dict) o None si las credenciales fallan."""
        query = "SELECT * FROM users WHERE username = %s AND passw = %s"
        result = self.db.ejecutar_consulta(query, (self.username, self.passw))
        if result:
            return result[0]
        return None
