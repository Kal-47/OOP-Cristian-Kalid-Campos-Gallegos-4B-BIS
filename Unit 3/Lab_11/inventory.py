
from products import Producto
from exceptions import ProductoNoEncontrado

class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5),
            "P02": Producto("P02", 5),
            "P03": Producto("P03", 5),
            "P04": Producto("P04", 10),   # additional product
            "P05": Producto("P05", 3),    
        }

    def retirar(self, codigo, cantidad):
    
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"el producto '{codigo}' no existe")

        return self.productos[codigo].retirar(cantidad)
