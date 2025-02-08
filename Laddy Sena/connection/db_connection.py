import mysql.connector

def get_db_connection():
    """Establece la conexión a la base de datos MySQL."""
    try:
        conn = mysql.connector.connect(
            host="localhost",      # Cambia si tu MySQL está en otro servidor
            user="root",           # Usuario de MySQL
            password="",           # Contraseña de MySQL (deja vacío si no tiene)
            database="empresa_proyecto",  # Nombre de la base de datos
            port=3306              # Puerto de MySQL (3306 por defecto)
        )
        print("✅ Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar: {err}")
        return None

