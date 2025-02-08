import tkinter as tk
from tkinter import messagebox, ttk
import services.usuario_service as usuario_service

class UsuarioView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Gestión de Usuarios", font=("Arial", 14))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Crear Usuario", command=self.formulario_usuario).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Actualizar Usuario", command=self.formulario_actualizar_usuario).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Eliminar Usuario", command=self.eliminar_usuario).grid(row=0, column=2, padx=5)

        self.refresh_list()

    def refresh_list(self):
        """Actualiza la lista de usuarios en la interfaz"""
        self.listbox.delete(0, tk.END)
        usuarios = usuario_service.obtener_usuarios()
        for usuario in usuarios:
            self.listbox.insert(tk.END, f"{usuario.id} | {usuario.nombre} | {usuario.email}")

    def formulario_usuario(self):
        """Muestra una ventana emergente con un formulario para crear un usuario"""
        form = tk.Toplevel(self)
        form.title("Crear Usuario")
        form.geometry("470x470")

        tk.Label(form, text="Nombre:").pack()
        nombre_entry = tk.Entry(form, width=70)
        nombre_entry.pack()

        tk.Label(form, text="Número Documento:").pack()
        documento_entry = tk.Entry(form, width=70)
        documento_entry.pack()

        tk.Label(form, text="Email:").pack()
        email_entry = tk.Entry(form, width=70)
        email_entry.pack()

        tk.Label(form, text="Contraseña:").pack()
        password_entry = tk.Entry(form, show="*", width=70)
        password_entry.pack()

        tk.Label(form, text="Selecciona un Rol:").pack()
        roles = usuario_service.obtener_roles()
        rol_var = tk.StringVar()
        rol_combobox = ttk.Combobox(form, textvariable=rol_var, values=[f"{r[0]} - {r[1]}" for r in roles], width=67)
        rol_combobox.pack()

        def guardar_usuario():
            nombre = nombre_entry.get()
            documento = documento_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            rol_seleccionado = rol_combobox.get()

            if nombre and documento and email and password and rol_seleccionado:
                rol_id = int(rol_seleccionado.split(" - ")[0])  # Extraer el ID del rol seleccionado
                usuario_service.crear_usuario(nombre, documento, email, password, rol_id)
                self.refresh_list()
                form.destroy()
                messagebox.showinfo("Éxito", "Usuario creado y rol asignado correctamente")
            else:
                messagebox.showwarning("Error", "Todos los campos son obligatorios")

        tk.Button(form, text="Guardar", command=guardar_usuario).pack(pady=10)

    def formulario_actualizar_usuario(self):
        """Muestra una ventana emergente con un formulario para actualizar un usuario"""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un usuario para actualizar")
            return

        usuario_id = int(self.listbox.get(selected[0]).split("|")[0].strip())

        # Obtener datos actuales del usuario
        usuario = usuario_service.obtener_usuario_por_id(usuario_id)
        if not usuario:
            messagebox.showerror("Error", "No se pudo obtener la información del usuario")
            return

        # Extraer datos del usuario
        usuario_id, nombre_actual, documento_actual, email_actual, password_actual = usuario

        # Crear la ventana de actualización
        self.form_update = tk.Toplevel(self)  # Guardamos referencia global
        self.form_update.title("Actualizar Usuario")
        self.form_update.geometry("470x470")

        tk.Label(self.form_update, text="Nuevo Nombre:").pack()
        nombre_entry = tk.Entry(self.form_update, width=70)
        nombre_entry.insert(0, nombre_actual)  # Rellenar con el nombre actual
        nombre_entry.pack()

        tk.Label(self.form_update, text="Nuevo Número Documento:").pack()
        documento_entry = tk.Entry(self.form_update, width=70)
        documento_entry.insert(0, documento_actual)  # Rellenar con el documento actual
        documento_entry.pack()

        tk.Label(self.form_update, text="Nuevo Email:").pack()
        email_entry = tk.Entry(self.form_update, width=70)
        email_entry.insert(0, email_actual)  # Rellenar con el email actual
        email_entry.pack()

        tk.Label(self.form_update, text="Nueva Contraseña:").pack()
        password_entry = tk.Entry(self.form_update, show="*", width=70)
        password_entry.insert(0, password_actual)  # Rellenar con la contraseña actual
        password_entry.pack()

        tk.Label(self.form_update, text="Selecciona un Nuevo Rol:").pack()
        roles = usuario_service.obtener_roles()
        rol_var = tk.StringVar()
        rol_combobox = ttk.Combobox(self.form_update, textvariable=rol_var, values=[f"{r[0]} - {r[1]}" for r in roles], width=67)
        rol_combobox.pack()

        def actualizar_usuario():
            try:
                nombre = nombre_entry.get()
                documento = documento_entry.get()
                email = email_entry.get()
                password = password_entry.get()
                rol_seleccionado = rol_combobox.get()

                if nombre and documento and email and password and rol_seleccionado:
                    rol_id = int(rol_seleccionado.split(" - ")[0])  # Extraer el ID del rol seleccionado
                    usuario_service.actualizar_usuario(usuario_id, nombre, documento, email, password, rol_id)
                    self.refresh_list()
                    self.form_update.destroy()  # Cerrar la ventana después de actualizar
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                else:
                    messagebox.showwarning("Error", "Todos los campos son obligatorios")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(self.form_update, text="Actualizar", command=actualizar_usuario).pack(pady=10)

    def eliminar_usuario(self):
        """Función para eliminar un usuario"""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un usuario para eliminar")
            return

        usuario_id = int(self.listbox.get(selected[0]).split("|")[0].strip())
        usuario_service.eliminar_usuario(usuario_id)
        self.refresh_list()
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
