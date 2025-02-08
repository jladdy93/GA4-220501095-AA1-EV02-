import mysql.connector
from connection.db_connection import get_db_connection
from models.usuario_model import Usuario

def crear_usuario(nombre, numero_documento, email, password, rol_id):
    """Crea un usuario y le asigna un rol en la tabla usuario_rol"""
    try:
        conn = get_db_connection()
        if conn is None:
            print("❌ Error: No se pudo establecer conexión con la base de datos.")
            return
        
        cursor = conn.cursor()
        
        # Insertar el usuario en la tabla usuarios
        cursor.execute(
            "INSERT INTO usuarios (nombre, numero_documento, email, password) VALUES (%s, %s, %s, %s)",
            (nombre, numero_documento, email, password)
        )
        usuario_id = cursor.lastrowid  # Obtener el ID del usuario recién insertado
        
        # Insertar en la tabla pivote usuario_rol
        cursor.execute(
            "INSERT INTO usuario_rol (usuario_id, rol_id) VALUES (%s, %s)",
            (usuario_id, rol_id)
        )
        
        conn.commit()
        print("✅ Usuario y rol asignados correctamente")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar usuario y asignar rol: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def obtener_roles():
    """Obtiene todos los roles disponibles"""
    try:
        conn = get_db_connection()
        if conn is None:
            return []
        
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM roles")
        roles = cursor.fetchall()
        return roles
    except mysql.connector.Error as err:
        print(f"❌ Error al obtener roles: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def obtener_usuarios():
    """Obtiene todos los usuarios de la base de datos."""
    try:
        conn = get_db_connection()
        if conn is None:
            print("❌ Error: No se pudo establecer conexión con la base de datos.")
            return []
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        
        return [Usuario(*row) for row in usuarios]
    except mysql.connector.Error as err:
        print(f"❌ Error al obtener usuarios: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def actualizar_usuario(usuario_id, nombre, documento, email, password, rol_id):
    """Actualiza los datos de un usuario y su rol"""
    try:
        conn = get_db_connection()
        if conn is None:
            print("❌ Error: No se pudo establecer conexión con la base de datos.")
            return
        
        cursor = conn.cursor()
        
        # Actualizar datos del usuario
        cursor.execute(
            "UPDATE usuarios SET nombre = %s, numero_documento = %s, email = %s, password = %s WHERE id = %s",
            (nombre, documento, email, password, usuario_id)
        )

        # Actualizar el rol del usuario en la tabla pivote usuario_rol
        cursor.execute(
            "UPDATE usuario_rol SET rol_id = %s WHERE usuario_id = %s",
            (rol_id, usuario_id)
        )

        conn.commit()
        print("✅ Usuario y rol actualizados correctamente")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar usuario y rol: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def eliminar_usuario(usuario_id):
    """Elimina un usuario de la base de datos."""
    try:
        conn = get_db_connection()
        if conn is None:
            print("❌ Error: No se pudo establecer conexión con la base de datos.")
            return
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        conn.commit()
        print("✅ Usuario eliminado correctamente")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar usuario: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def obtener_usuario_por_id(usuario_id):
    """Obtiene los datos de un usuario específico por su ID."""
    try:
        conn = get_db_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, numero_documento, email, password FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
        
        return usuario  # Retorna una tupla con los datos del usuario
    except mysql.connector.Error as err:
        print(f"❌ Error al obtener usuario por ID: {err}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
