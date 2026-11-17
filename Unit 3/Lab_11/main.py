from inventory import *
from producto import *
def main():
    inventario = Inventario()
    codigo = input("Codigo del producto: ")
    try:
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
        print(
            "Retiro realizado. Stock restante:",
            inventario.productos[codigo].stock
            )
    except ValueError:
        print("La cantidad debe ser un número entero")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operacion: {error}")

if __name__ == "__main__":
    main()