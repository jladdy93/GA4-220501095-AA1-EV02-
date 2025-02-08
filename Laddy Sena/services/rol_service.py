from connection.db_connection import get_db_connection
from models.rol_model import Rol

def crear_rol(nombre):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO roles (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    conn.close()

def obtener_roles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    conn.close()
    return [Rol(*row) for row in roles]

def actualizar_rol(rol_id, nombre):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE roles SET nombre = %s WHERE id = %s", (nombre, rol_id))
    conn.commit()
    conn.close()

def eliminar_rol(rol_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM roles WHERE id = %s", (rol_id,))
    conn.commit()
    conn.close()