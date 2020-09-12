

import sqlite3

nombreBD = "clinica.db"
# aydas sql query varias tablas a la vez https://www.campusmvp.es/recursos/post/Fundamentos-de-SQL-Consultas-SELECT-multi-tabla-JOIN.aspx
# funciones CRUD
print(nombreBD)

def crearCliente(datos):
    """Crea un nuevo cliente, hay que incluir una lista de datos con 9 valores:
    (DNI, NOMBRE, APELLIDO, DIRECCIÓN, MUNICIPIO, PROVINCIA, CP, TELÉFONO, EMAIL).
    """
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO CLIENTE VALUES (NULL,?,?,?,?,?,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def crearServicio(datos):
    """Crea un nuevo servicio, hay que incluir una lista de datos con 4 valores:
    (fecha,decripción del  tratamiento, precio, ID de la factura que tiene ese servicio).
    """
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO SERVICIO VALUES (NULL,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def crearFactura(datos):
    """Crea la factura, hay que incluir una lista de datos con 5 valores:
    (código de la factura, fecha, IVA, descuento, ID del cliente asociado a la factura).
    """

    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    for i in datos:
        miCursor.execute(f'INSERT INTO FACTURA VALUES (NULL,?,?,?,?,?,?)', i)
    miConexion.commit()
    miConexion.close()


def leerRegistro(tabla, campo, valor):
    """Lee un registro concreto, ejemplo de uso:
    leerRegistro("FACTURA", "ID", 8) te da todos los datos de la factura cuyo ID es 8"""
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    registro = miCursor.execute(f'SELECT * FROM {tabla} WHERE {campo} = ?', datos).fetchall()
    print(registro)
    return registro
    miConexion.commit()
    miConexion.close()


def leerTodo(tabla):
    """devuelve todos los campos de la tabla que digamos"""
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    query = miCursor.execute(f'SELECT * FROM {tabla}').fetchall()
    miConexion.commit()
    miConexion.close()
    return query


def actualizarRegistro(tabla, campo, valor, condicion_columna, condicion_valor):
    """actualizar cualquier registro, se le debe indicar:
    tabla: a modificar
    campo: a modificar
    valor: que queremos incluir sustituyendo a lo que había
    condicion_columna: para indicar que campo vamos a sustituir
    condicion_valor: para decir que valor debe ir en la condición.
        Ejemplo: actualizarRegistro("CLIENTE", "DNI","12345678M","ID", 4)
        cambia en la tabla clientes el dni (actualizándolo a 12345678M) en el  cliente con ID=4."""
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor, condicion_valor)
    #print("Se ha llamado a actualizarRegistro")
    # miCursor.execute(f'UPDATE {tabla} SET {campo} = {valor} WHERE {condicion}')
    miCursor.execute(f'UPDATE {tabla} SET {campo} = ? WHERE {condicion_columna} = ?', datos)
    #print(leerTodo("CLIENTE"))
    miConexion.commit()
    miConexion.close()


def borrarRegistro(tabla, campo, valor):
    """Borrar el registro, hay que introducir la tabla, el campo y el valor a eliminar"""
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    clientes = miCursor.execute(f'DELETE FROM {tabla} WHERE {campo} = ?', datos)
    print(clientes.fetchall())
    miConexion.commit()
    miConexion.close()


def todoFacturasClientes(campo_orden, campo_condicion, condicionMayor, condicionMenor):
    """Obtiene todas las facturas con sus clientes y servicios relacionados"""
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    consulta = f'SELECT * FROM FACTURA, CLIENTE, SERVICIO WHERE (FACTURA.CLIENTE_ID = CLIENTE.ID AND SERVICIO.FACTURA_ID = FACTURA.ID AND {campo_condicion} >= "{condicionMayor}" AND {campo_condicion} <= "{condicionMenor}") ORDER BY {campo_orden}'
    print ('y esta es la consulta que le hago a la base de datos \n', consulta)
    query = miCursor.execute(consulta).fetchall()
    miConexion.commit()
    miConexion.close()
    return query






