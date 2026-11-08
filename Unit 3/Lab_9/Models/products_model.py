from Controller.database_connection import Database_connection

class Producto:
    def __init__(self, id=None, nombre=None, precio=None, stock=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def obtener_todos(self):
        "Retorna una lista con todos los productos registrados."
        query = "SELECT id, nombre, precio, stock FROM productos"
        return self.db.ejecutar_consulta(query)

    def guardar(self):
        """Inserta un nuevo producto en la base de datos. Devuelve True o False."""
        query = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        try:
            self.db.ejecutar_comando(query, (self.nombre, self.precio, self.stock))
            return True
        except ConnectionError as e:
            print(f"Error al guardar producto: {e}")
            return False
