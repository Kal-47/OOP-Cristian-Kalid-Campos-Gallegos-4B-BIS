
from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise CantidadInvalida("la cantidad debe ser un entero mayor a cero")

        if cantidad > self.stock:
            raise StockInsuficiente(
                f"stock disponible: {self.stock}, cantidad solicitada: {cantidad}"
            )

        self.stock -= cantidad
        return self.stock
