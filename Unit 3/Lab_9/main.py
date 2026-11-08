import tkinter as tk
from Views.login_view import LoginVentana
from Views.theme import aplicar_tema

if __name__ == "__main__":
    root = tk.Tk()
    aplicar_tema(root)  # tema negro/rojo: antes de crear las ventanas
    app = LoginVentana(root)
    root.mainloop()
