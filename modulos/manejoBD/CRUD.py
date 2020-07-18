from modulos.modulos_importados import *


# setup
nombreBD = modulos.modulos_importados.NOMBREBD

# funciones CRUD


def crearCliente(datos):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO CLIENTE VALUES (NULL,?,?,?,?,?,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def crearServicio(datos):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO SERVICIO VALUES (NULL,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def crearFactura(datos):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO FACTURA VALUES (NULL,?,?,?,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def leerRegistro(tabla, campo, valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    clientes = miCursor.execute(f'SELECT * FROM {tabla} WHERE {campo} = ?', datos).fetchall()
    print(clientes)
    return clientes
    miConexion.commit()
    miConexion.close()


def leerTodo(tabla):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()

    query = miCursor.execute(f'SELECT * FROM {tabla}').fetchall()
    print(query)
    miConexion.commit()
    miConexion.close()
    return query


def actualizarRegistro(tabla, campo, valor, condicion_columna, condicion_valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor, condicion_valor)

    # miCursor.execute(f'UPDATE {tabla} SET {campo} = {valor} WHERE {condicion}')
    miCursor.execute(f'UPDATE {tabla} SET {campo} = ? WHERE {condicion_columna} = ?', datos)
    miConexion.commit()
    miConexion.close()


def borrarRegistro(tabla, campo, valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    clientes = miCursor.execute(f'DELETE FROM {tabla} WHERE {campo} = ?', datos)
    print(clientes.fetchall())
    miConexion.commit()
    miConexion.close()


"""

#PROBANDO SERVICIOS, LEER DATOS, CAMBIAR, .

leerTodo('SERVICIO')
actualizarRegistro('SERVICIO','TRATAMIENTO','CAMBIADO EL TRATAMIENTO', 'ID',1)
leerTodo('SERVICIO')

leerTodo('FACTURA')
"""
