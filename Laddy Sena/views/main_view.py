import tkinter as tk
from tkinter import ttk
from views.usuario_view import UsuarioView
from views.rol_view import RolView

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Usuarios y Roles")
        self.geometry("600x400")

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        frame_usuarios = UsuarioView(notebook)
        frame_roles = RolView(notebook)

        notebook.add(frame_usuarios, text="Usuarios")
        notebook.add(frame_roles, text="Roles")

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
