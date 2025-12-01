import sqlite3

def conectar():
    """
    Establece conexión con la base de datos SQLite y activa claves foráneas.
    
    Devuelve:
        tupla: (conexión, cursor) o (None, None) en caso de que haya un error
    """
    try:
        con = sqlite3.connect("Empresa.db")
        con.execute("PRAGMA foreign_keys = ON;")
        cur = con.cursor()
        print("Conexión establecida correctamente")
        return con, cur
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

if __name__ == "__main__":
    conectar()