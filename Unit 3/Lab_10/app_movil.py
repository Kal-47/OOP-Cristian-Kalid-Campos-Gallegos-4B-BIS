
class AppMovilError(Exception):
    """Error base para toda la aplicacion  """


class SuscripcionExpiradaError(AppMovilError):
    """Error cuando una suscripcion es invalida   """


class PuntosInsuficientesError(AppMovilError):
    """Error cuando se tienen gemas insuficientes"""


class PerfilMovil:
    GEMAS_INICIALES = 50

    def __init__(self, username: str, gemas: int = GEMAS_INICIALES,
                 racha_dias: int = 1, notificaciones_activas: bool = True):
        self.username = username
        self.gemas = gemas 
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    @property
    def gemas(self) -> int:
        return self._gemas

    @gemas.setter
    def gemas(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise ValueError("Las gemas deben ser un entero.")
        if valor < 0:
            raise ValueError("Las gemas no pueden ser negativas.")
        self._gemas = valor

    @staticmethod
    def _validar_cantidad(cantidad) -> None:
        """La cantidad debe ser un entero estrictamente positivo."""
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero estrictamente positivo.")

    def ganar_gemas(self, cantidad: int) -> int:
        """Incrementa el saldo y devuelve el nuevo balance."""
        self._validar_cantidad(cantidad)
        self._gemas += cantidad
        return self._gemas

    def gastar_gemas(self, cantidad: int) -> int:
        """Decrementa el saldo (si alcanza) y devuelve el nuevo balance."""
        self._validar_cantidad(cantidad)
        if cantidad > self._gemas:
            raise PuntosInsuficientesError(
                f"Saldo insuficiente: tienes {self._gemas} y necesitas {cantidad}."
            )
        self._gemas -= cantidad
        return self._gemas


class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, **kwargs):
        if (not isinstance(meses_suscripcion, int) or isinstance(meses_suscripcion, bool)
                or meses_suscripcion <= 0):
            raise ValueError("meses_suscripcion debe ser un entero mayor que cero.")
        super().__init__(username, **kwargs)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        """Si la suscripción llegó a 0 meses, desactiva es_pro y propaga el error."""
        if self.meses_suscripcion <= 0 or not self.es_pro:
            self.es_pro = False
            raise SuscripcionExpiradaError(
                f"La suscripción de {self.username} expiró."
            )
        return f"Contenido offline descargado para {self.username}."
