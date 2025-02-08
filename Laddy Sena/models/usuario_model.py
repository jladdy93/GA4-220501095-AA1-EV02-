class Usuario:
    def __init__(self, id, nombre, numero_documento, email, password, created_at, update_at):
        self.id = id
        self.nombre = nombre
        self.numero_documento = numero_documento
        self.email = email
        self.password = password
        self.created_at = created_at
        self.update_at = update_at