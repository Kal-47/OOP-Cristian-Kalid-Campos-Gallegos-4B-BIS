import tkinter as tk

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.authentication_controller import Authentication


def main():
    root = tk.Tk()

    modelo = UserModel()          # Model
    vista = LoginView(root)       # View
    Authentication(modelo, vista) # Controller: conecta modelo y vista

    root.mainloop()


if __name__ == "__main__":
    main()
