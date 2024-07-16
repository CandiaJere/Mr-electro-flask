from db import conectarMySQL

# CRUD

    

# Create
def cargar_nuevo_clie(nombre, email, contacto):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO clientes (nombre, email, contacto) VALUES (%s, %s, %s)"
        cursor.execute(query,(nombre, email, contacto))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    


# Read
def listarClientes():
    # conexion mysql
    conexion = conectarMySQL()
    clientes = []
    with conexion.cursor() as cursor:
        sql = """SELECT * FROM clientes"""
        cursor.execute(sql)
        clientes = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return clientes




# Update
def obtener_clie_por_id(id):
    conexion = conectarMySQL()
    clie = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM clientes WHERE id = %s", (id,))
        clie = cursor.fetchone()
    conexion.close()
    return clie


def actualizar_clie(nombre, email, contacto, id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombre = %s, email = %s, contacto = %s WHERE id = %s",(nombre, email, contacto, id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result





# Delete
def eliminar_clie(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result