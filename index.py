import sqlite3

#Conexion a la base de datos

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear tabla si no existe 

cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT,
    email TEXT
    )
"""
)

conn.commit()

# Crear registro -> C

def crear_usuario(nombre: str, email) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email))
    conn.commit()
    return "Usuario agregado"

# Obtener registros -> R

def obtener_registros() -> []:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios = cursor.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)
    return lista_usuarios

# Actualizar usuario por id -> U

def actualizar_usuario(id: int, nombre: str, email: str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id)
    )
    conn.commit()
    return "Usuario actualizado"

# Eliminar usuario -> D 

def eliminar_usuario(id: int) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"

# Leer registro por su id

def obtener_usuario(id: int) -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if usuario: 
        return usuario
    return "Usuario no encontrado"

# Crear usuario 
# crear_usuario("Juan", "juan@example.com")
# crear_usuario("Facu", "facu@example.com")
# crear_usuario("Jose", "jose@example.com")

# Obtener registros
#print(obtener_registros())

# Actualizar usuario
# print(actualizar_usuario(2, "Facu 2", "facu@gmail.com"))

# Obtener usuario 
# print(obtener_usuario())

# Eliminar usuario
# eliminar_usuario()
