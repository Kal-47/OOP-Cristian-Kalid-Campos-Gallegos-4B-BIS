
from inventory import Inventario
from exceptions import ErrorInventario

def main():
    inventario = Inventario()
    codigo = input("Codigo del producto: ").strip()

    try:
        cantidad = int(input("Cantidad a retirar: "))
        stock_restante = inventario.retirar(codigo, cantidad)

    except ValueError:
        print("La cantidad debe ser un número entero")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operacion ({type(error).__name__}): {error}")

    else:
        print("Retiro realizado. Stock restante:", stock_restante)


if __name__ == "__main__":
    main()
