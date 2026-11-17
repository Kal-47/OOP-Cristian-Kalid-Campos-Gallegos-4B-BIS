
class ErrorInventario(Exception):
    """Clase base para todos los errores"""
    pass


class ProductoNoEncontrado(ErrorInventario):
    pass


class CantidadInvalida(ErrorInventario):
    pass


class StockInsuficiente(ErrorInventario):
    pass
