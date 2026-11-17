class ErrorInventario(Exception):
    pass

class ProductEncontrado(ErrorInventario):
    pass

class CantidadInvalida(ErrorInventario):
    pass
class StockInsuficiente(ErrorInventario):
    pass

#Clase inventario
class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5),
            "P02": Producto("P02", 5),
            "P03": Producto("P03", 5)
        }

    def retirar(self, codigo, cantidad):
        pass

    #Step 4: Verify the product exists.abs

    #Step 5: Delegate the discount to the product class.abs

