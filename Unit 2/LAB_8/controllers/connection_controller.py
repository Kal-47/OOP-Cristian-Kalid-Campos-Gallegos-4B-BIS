import mysql.connector


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.usuario = "root"
        self.password = ""
        self.base_datos = "login_mvc"

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos
            )
            return conexion

        except mysql.connector.Error as error:
            print("Error al conectar con MySQL:", error)
            return None

# Prueba rápida: python controllers/connection_controller.py
if __name__ == "__main__":
    prueba = Conexion().conectar()

    if prueba is not None and prueba.is_connected():
        print("Conexión exitosa a la base de datos:", prueba.database)
        prueba.close()
    else:
        print("No se pudo conectar. Revisa que MySQL esté activo y que exista la base de datos.")
