import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root):
        self.root = root

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.root.title("Acceso al sistema")

        # PERSONALIZAR 2:
        # Modifica el ancho y alto de la ventana.
        self.root.geometry("440x380")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.root.configure(bg="#F4ECF7")

        self.root.resizable(False, False)

        # PERSONALIZAR 4:
        # Cambia el texto, la fuente y los colores del título.
        self.titulo = tk.Label(
            root,
            text="BIENVENIDO",
            font=("Verdana", 20, "bold"),
            bg="#F4ECF7",
            fg="#6C3483"
        )
        self.titulo.pack(pady=20)

        # PERSONALIZAR 5:
        # Modifica el texto y la apariencia de las etiquetas.
        self.lbl_email = tk.Label(
            root,
            text="Tu correo:",
            font=("Arial", 11),
            bg="#F4ECF7"
        )
        self.lbl_email.pack()

        # PERSONALIZAR 6:
        # Cambia el ancho, la fuente y otros atributos del campo.
        self.entry_email = tk.Entry(
            root,
            width=35,
            font=("Arial", 11)
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Arial", 11),
            bg="#F4ECF7"
        )
        self.lbl_password.pack()

        # El atributo show oculta los caracteres al escribir.
        self.entry_password = tk.Entry(
            root,
            width=35,
            font=("Arial", 11),
            show="*"
        )
        self.entry_password.pack(pady=5)

        # PERSONALIZAR 7:
        # Cambia el texto, color, tamaño y fuente del botón.
        self.btn_login = tk.Button(
            root,
            text="Entrar",
            width=20,
            bg="#8E44AD",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        # PERSONALIZAR 8:
        # Cambia el diseño del botón para abrir el registro.
        self.btn_register = tk.Button(
            root,
            text="Registrarme",
            width=20,
            bg="#16A085",
            fg="white",
            font=("Arial", 10),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)