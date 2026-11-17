# Clase Producto

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo

    def retirar(self, cantidad, stock):
        self.cantidad = cantidad 
        self.stock = stock

        if cantidad <= 0:
            print("ERROR: la cantidad no es valida, inserta un numero mayor a cero")

        if cantidad > stock:
            pass
        else:
            pass

        cantidad = cantidad - retirar;
        
    #Step 1: Validate that the quantity is greater than zero.

    #Step 2: Validate that there is sufficient stock.

    #Step 3: dedudct the quantity from the stock
