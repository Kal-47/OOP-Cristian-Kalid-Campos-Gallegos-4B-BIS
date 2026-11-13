import csv
import json
from decimal import Decimal

from fpdf import FPDF


class Exportador:

    COLUMNAS = ("id", "nombre", "precio", "stock")

    def exportar(self, datos, ruta_archivo):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def _a_diccionario(self, fila):
        if isinstance(fila, dict):
            return fila
        return dict(zip(self.COLUMNAS, fila))


class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for fila in datos:
                p = self._a_diccionario(fila)
                file.write(
                    f"ID: {p['id']} | Nombre: {p['nombre']} | "
                    f"Precio: ${p['precio']:.2f} | Stock: {p['stock']}\n"
                )
        print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorCSV(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(self.COLUMNAS)
            for fila in datos:
                p = self._a_diccionario(fila)
                writer.writerow([p[columna] for columna in self.COLUMNAS])
        print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):
    @staticmethod
    def _serializar(valor):
        if isinstance(valor, Decimal):
            return float(valor)
        return str(valor)

    def exportar(self, datos, ruta_archivo):
        registros = []
        for fila in datos:
            p = self._a_diccionario(fila)
            registros.append({columna: p[columna] for columna in self.COLUMNAS})

        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(
                registros, file,
                indent=4, ensure_ascii=False, default=self._serializar
            )
        print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):
    @staticmethod
    def _seguro(texto):
        return str(texto).encode("latin-1", "replace").decode("latin-1")

    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align="C")

        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        for fila in datos:
            p = self._a_diccionario(fila)
            texto_linea = (
                f"Producto: {p['nombre']} - Precio: ${p['precio']:.2f} "
                f"- Stock: {p['stock']}"
            )
            pdf.cell(200, 10, txt=self._seguro(texto_linea), ln=True)

        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
