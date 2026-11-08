import os
import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana
from Views.theme import ESTILO_BOTON

try:
    from PIL import Image, ImageTk
except ImportError:  # Pillow no instalado: la app funciona sin logo
    Image = ImageTk = None

# Ruta del logo relativa a ESTE archivo (no a la carpeta desde donde se ejecuta Python)
RUTA_LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main Spiral Logo.webp")
RUTA_ICONO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_icon.png")
ALTO_LOGO = 70

class LoginVentana:
    """Ventana de inicio de sesión."""

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("500x460")
        self.root.resizable(False, False)
        self._poner_icono()

        # Construir la interfaz
        self._crear_interfaz()

    def _poner_icono(self):
        """Pone el icono de la ventana (barra de título / barra de tareas)."""
        try:
            # tk.PhotoImage lee PNG sin necesitar Pillow
            self.icono_img = tk.PhotoImage(file=RUTA_ICONO)
            # True = también se aplica a las ventanas que se creen después
            self.root.iconphoto(True, self.icono_img)
        except Exception as e:
            print(f"No se pudo cargar el icono: {e}")

    def crear_logo(self):
        """Muestra el logo; si algo falla, muestra un texto de reemplazo."""
        try:
            if Image is None:
                raise RuntimeError("Pillow no está instalado (pip install pillow)")
            imagen_pil = Image.open(RUTA_LOGO)
            # Mantener la proporción original (el logo es ~2.5:1, no cuadrado)
            ancho = round(imagen_pil.width * ALTO_LOGO / imagen_pil.height)
            imagen_pil = imagen_pil.resize((ancho, ALTO_LOGO), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(imagen_pil)  # guardar referencia en self

            lbl_logo = tk.Label(self.root, image=self.logo_img)
            lbl_logo.pack(pady=(15, 0))
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            lbl_logo = tk.Label(self.root, text="[ LOGO ]", font=("Helvetica", 12, "italic"), fg="gray")
            lbl_logo.pack(pady=(15, 0))

    def _crear_interfaz(self):
        # Logo
        self.crear_logo()

        # Título
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=15)

        # Campo Usuario
        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        # Campo Contraseña
        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        # Botón Ingresar
        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            command=self._validar_login,
            **ESTILO_BOTON
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        # Validación básica de campos vacíos
        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        # Instanciar el modelo Usuario y autenticar
        usuario_obj = User(usuario_texto, pass_texto)
        try:
            datos_usuario = usuario_obj.auth()
        except ConnectionError as e:
            print(e)
            messagebox.showerror("Error de Base de Datos", str(e))
            return

        if datos_usuario:
            messagebox.showinfo("Bienvenido", f"¡Hola {datos_usuario['usr_name']}! Acceso concedido.")
            self._abrir_dashboard(datos_usuario['usr_name'])
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        """Limpia la ventana actual y muestra el panel principal."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.resizable(True, True)
        DashboardVentana(self.root, nombre_completo)
