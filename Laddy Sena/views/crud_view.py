import tkinter as tk
from tkinter import ttk
from views.usuario_view import UsuarioView
from views.rol_view import RolView

class CrudView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Usuarios y Roles")
        self.geometry("600x400")

        # Crear el Notebook (Pestañas)
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de Usuarios
        self.frame_usuarios = UsuarioView(notebook)
        notebook.add(self.frame_usuarios, text="Usuarios")

        # Pestaña de Roles
        self.frame_roles = RolView(notebook)
        notebook.add(self.frame_roles, text="Roles")

if __name__ == "__main__":
    app = CrudView()
    app.mainloop()
