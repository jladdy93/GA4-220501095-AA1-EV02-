import tkinter as tk
from tkinter import messagebox
import services.rol_service as rol_service

class RolView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Gestión de Roles", font=("Arial", 14))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Crear Rol", command=self.formulario_crear_rol).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Actualizar Rol", command=self.formulario_actualizar_rol).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Eliminar Rol", command=self.eliminar_rol).grid(row=0, column=2, padx=5)

        self.refresh_list()

    def refresh_list(self):
        """Actualiza la lista de roles en la interfaz"""
        self.listbox.delete(0, tk.END)
        roles = rol_service.obtener_roles()
        for rol in roles:
            self.listbox.insert(tk.END, f"{rol.id} | {rol.nombre}")

    def formulario_crear_rol(self):
        """Muestra una ventana emergente con un formulario para crear un rol"""
        form = tk.Toplevel(self)
        form.title("Crear Rol")
        form.geometry("300x150")

        tk.Label(form, text="Nombre del Rol:").pack()
        nombre_entry = tk.Entry(form)
        nombre_entry.pack()

        def guardar_rol():
            nombre = nombre_entry.get()
            if nombre:
                rol_service.crear_rol(nombre)
                self.refresh_list()
                form.destroy()
                messagebox.showinfo("Éxito", "Rol creado correctamente")
            else:
                messagebox.showwarning("Error", "El nombre del rol es obligatorio")

        tk.Button(form, text="Guardar", command=guardar_rol).pack(pady=10)

    def formulario_actualizar_rol(self):
        """Muestra una ventana emergente con un formulario para actualizar un rol"""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un rol para actualizar")
            return

        rol_id = int(self.listbox.get(selected[0]).split("|")[0].strip())

        form = tk.Toplevel(self)
        form.title("Actualizar Rol")
        form.geometry("300x150")

        tk.Label(form, text="Nuevo Nombre del Rol:").pack()
        nombre_entry = tk.Entry(form)
        nombre_entry.pack()

        def actualizar_rol():
            nombre = nombre_entry.get()
            if nombre:
                rol_service.actualizar_rol(rol_id, nombre)
                self.refresh_list()
                form.destroy()
                messagebox.showinfo("Éxito", "Rol actualizado correctamente")
            else:
                messagebox.showwarning("Error", "El nombre del rol es obligatorio")

        tk.Button(form, text="Actualizar", command=actualizar_rol).pack(pady=10)

    def eliminar_rol(self):
        """Función para eliminar un rol"""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un rol para eliminar")
            return

        rol_id = int(self.listbox.get(selected[0]).split("|")[0].strip())
        rol_service.eliminar_rol(rol_id)
        self.refresh_list()
        messagebox.showinfo("Éxito", "Rol eliminado correctamente")
