import sqlite3
import os
# setup
nombreBD = "clinica.db"
ivas = [21, 10, 4]



if not(os.path.isfile(nombreBD)):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    miCursor.execute('''CREATE TABLE CLIENTE(
    CLIENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DNI VARCHAR(12) NOT NULL UNIQUE,
    NOMBRE VARCHAR(20) NOT NULL,
    APELLIDOS VARCHAR(50),
    DIRECCION VARCHAR(50),
    MUNICIPIO VARCHAR(50),
    PROVINCIA VARCHAR(50),
    CODIGO_POSTAL VARCHAR(10),
    TELEFONO VARCHAR(15),
    EMAIL VARCHAR(50) NOT NULL 
    )''')
    miCursor.execute('''CREATE TABLE FACTURA(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODIGO_FACTURA VARCHAR(7) NOT NULL UNIQUE,
    FECHA_FACTURA DATE NOT NULL,
    SERVICIO INTEGER,
    IVA_ID INTEGER,
    DESCUENTO INTEGER,
    PRECIO_FINAL REAL
    CLIENTE_ID INTEGER
    )''')
    miCursor.execute('''CREATE TABLE SERVICIO(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FECHA_SERVICIO DATE NOT NULL,
    TRATAMIENTO TEXT,
    PRECIO_FINAL REAL,
    FACTURA_ID INTEGER
    )''')
    miCursor.execute('''CREATE TABLE IVA(
    IVA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIPO INTEGER NOT NULL
    )''')
    for i in ivas:
        miCursor.execute(f'INSERT INTO IVA VALUES (NULL,{i})')
    miConexion.commit()
    miConexion.close()
else:
    print(f'El archivo {nombreBD} ya existe')

# funciones CRUD


def crearCliente(tabla, datos):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    miCursor.execute(f'INSERT INTO {tabla} VALUES (NULL,?,?,?,?,?,?,?,?,?)',datos)
    miConexion.commit()
    miConexion.close()

def leerRegistro(tabla,campo, valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    clientes = miCursor.execute(f'SELECT * FROM {tabla} WHERE {campo} = ?',datos)
    print(clientes.fetchall())
    miConexion.commit()
    miConexion.close()
def actualizarRegistro(tabla,campo,valor,condicion_columna, condicion_valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor, condicion_valor)
    
    #miCursor.execute(f'UPDATE {tabla} SET {campo} = {valor} WHERE {condicion}')
    miCursor.execute(f'UPDATE CLIENTE SET DIRECCION = ? WHERE {condicion_columna} = ?', datos)
    miConexion.commit()
    miConexion.close()
def borrarRegistro(tabla,campo, valor):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    datos = (valor,)
    clientes = miCursor.execute(f'DELETE FROM {tabla} WHERE {campo} = ?',datos)
    print(clientes.fetchall())
    miConexion.commit()
    miConexion.close()

datos=[('123','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfg43434343rgrddd4gr'),
        ('1222ff2223','Antonio','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfg43343rgrddd4gr'),
        ('1222ff22','Jaime','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfd4gr'),
        ('1222f','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putrgrddd4gr'),
        ('1222','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','prgrddd4gr')]
#for i in datos:
#    crearCliente('CLIENTE', i)
#leerRegistro('CLIENTE','NOMBRE','Luis')


#actualizarRegistro('CLIENTE','DIRECCION', 'definitivamente sí', 'NOMBRE', 'Luis')
leerRegistro('CLIENTE','NOMBRE','Luis')
#borrarRegistro('CLIENTE', 'DNI', '123')
leerRegistro('CLIENTE','NOMBRE','Luis')
