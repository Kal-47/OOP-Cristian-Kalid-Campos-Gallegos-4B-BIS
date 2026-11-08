"""Tema visual de la aplicación (negro + rojo).

Para cambiar la paleta completa basta con editar las constantes de abajo.
Llama a aplicar_tema(root) en main.py ANTES de crear las ventanas, porque
los valores por defecto solo afectan a los widgets que se creen después.
"""
from tkinter import ttk

# ---------- Paleta ----------
FONDO = "#000000"          # fondo de ventanas y paneles
ACENTO = "#E60000"         # botones, selección, pestaña activa
ACENTO_HOVER = "#B30000"   # botón mientras se presiona
SUPERFICIE = "#141414"     # entradas de texto, tabla, pestañas inactivas
SUPERFICIE_ALT = "#242424" # encabezados de tabla, bordes sutiles
TEXTO = "#FFFFFF"
TEXTO_SUAVE = "#B0B0B0"

# ---------- Estilos reutilizables para tk.Button ----------
ESTILO_BOTON = dict(
    bg=ACENTO,
    fg=TEXTO,
    activebackground=ACENTO_HOVER,
    activeforeground=TEXTO,
    relief="flat",
    bd=0,
    cursor="hand2",
)


def aplicar_tema(root):
    """Aplica colores por defecto a widgets tk y ttk."""
    root.configure(bg=FONDO)

    # --- Widgets tk: valores por defecto para todo lo que se cree después ---
    root.option_add("*Label.Background", FONDO)
    root.option_add("*Label.Foreground", TEXTO)
    root.option_add("*Frame.Background", FONDO)
    # OJO: la clase de tk.LabelFrame en Tk se llama "Labelframe" (f minúscula)
    root.option_add("*Labelframe.Background", FONDO)
    root.option_add("*Labelframe.Foreground", TEXTO)

    root.option_add("*Entry.Background", SUPERFICIE)
    root.option_add("*Entry.Foreground", TEXTO)
    root.option_add("*Entry.insertBackground", TEXTO)  # cursor de escritura
    root.option_add("*Entry.relief", "flat")
    root.option_add("*Entry.highlightThickness", 1)
    root.option_add("*Entry.highlightBackground", SUPERFICIE_ALT)
    root.option_add("*Entry.highlightColor", ACENTO)  # borde al enfocar

    # Lista desplegable del Combobox (es un Listbox interno)
    root.option_add("*TCombobox*Listbox.Background", SUPERFICIE)
    root.option_add("*TCombobox*Listbox.Foreground", TEXTO)
    root.option_add("*TCombobox*Listbox.selectBackground", ACENTO)
    root.option_add("*TCombobox*Listbox.selectForeground", TEXTO)

    # --- Widgets ttk: se controlan con Style (ignoran bg=) ---
    estilo = ttk.Style(root)
    estilo.theme_use("clam")  # el tema por defecto ignora varios colores en Linux

    estilo.configure(".", background=FONDO, foreground=TEXTO)

    # Tabla
    estilo.configure(
        "Treeview",
        background=SUPERFICIE, fieldbackground=SUPERFICIE,
        foreground=TEXTO, rowheight=26, borderwidth=1,
        bordercolor=SUPERFICIE_ALT, lightcolor=SUPERFICIE, darkcolor=SUPERFICIE,
    )
    estilo.map(
        "Treeview",
        background=[("selected", ACENTO)],
        foreground=[("selected", TEXTO)],
    )
    estilo.configure(
        "Treeview.Heading",
        background=SUPERFICIE_ALT, foreground=TEXTO,
        relief="flat", borderwidth=0, padding=6,
    )
    estilo.map("Treeview.Heading", background=[("active", ACENTO_HOVER)])

    # Pestañas
    estilo.configure(
        "TNotebook", background=FONDO, borderwidth=1,
        bordercolor=SUPERFICIE_ALT, lightcolor=FONDO, darkcolor=FONDO,
    )
    estilo.configure(
        "TNotebook.Tab",
        background=SUPERFICIE, foreground=TEXTO_SUAVE,
        padding=(14, 6), borderwidth=0,
        bordercolor=FONDO, lightcolor=SUPERFICIE, darkcolor=SUPERFICIE,
    )
    estilo.map(
        "TNotebook.Tab",
        background=[("selected", ACENTO)],
        foreground=[("selected", TEXTO)],
        lightcolor=[("selected", ACENTO)],
        darkcolor=[("selected", ACENTO)],
    )

    # Combobox
    estilo.configure(
        "TCombobox",
        fieldbackground=SUPERFICIE, background=SUPERFICIE_ALT,
        foreground=TEXTO, arrowcolor=TEXTO,
        bordercolor=SUPERFICIE_ALT, lightcolor=SUPERFICIE_ALT,
        darkcolor=SUPERFICIE_ALT, selectbackground=SUPERFICIE,
        selectforeground=TEXTO,
    )
    estilo.map(
        "TCombobox",
        fieldbackground=[("readonly", SUPERFICIE)],
        foreground=[("readonly", TEXTO)],
        selectbackground=[("readonly", SUPERFICIE)],
        selectforeground=[("readonly", TEXTO)],
        bordercolor=[("focus", ACENTO)],
    )

    # Barra de desplazamiento
    estilo.configure(
        "Vertical.TScrollbar",
        background=SUPERFICIE_ALT, troughcolor=FONDO,
        arrowcolor=TEXTO, bordercolor=FONDO,
        lightcolor=SUPERFICIE_ALT, darkcolor=SUPERFICIE_ALT,
    )
    estilo.map("Vertical.TScrollbar", background=[("active", ACENTO)])
