from Models.products_model import Producto
from exportadores import (
    ExportadorCSV,
    ExportadorTXT,
    ExportadorJSON,
    ExportadorPDF,
)


class ReporteController:
    """Controlador del módulo de exportación.

    Aquí NO se importan csv, json ni fpdf: esa lógica vive en exportadores.py.
    """

    # Cada formato apunta a su clase hija de Exportador.
    EXPORTADORES = {
        "CSV": ExportadorCSV,
        "TXT": ExportadorTXT,
        "JSON": ExportadorJSON,
        "PDF": ExportadorPDF,
    }
    FORMATOS = tuple(EXPORTADORES)

    def generar_reporte(self, formato, ruta_archivo):
        """Exporta el inventario actual al formato elegido en la Vista.

        Lanza ValueError (formato inválido o sin productos) y deja pasar
        ConnectionError / OSError para que la Vista muestre el mensaje.
        """
        clase_exportador = self.EXPORTADORES.get(formato)
        if clase_exportador is None:
            raise ValueError(f"Formato no soportado: {formato}")

        datos = Producto().obtener_todos()
        if not datos:
            raise ValueError("No hay productos registrados para exportar.")

        exportador = clase_exportador()
        # Llamada polimórfica: al controlador no le importa el formato.
        exportador.exportar(datos, ruta_archivo)
        return ruta_archivo
