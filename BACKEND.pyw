import sqlite3
import os
#setup
nombreBD="clinica.db"
ivas = [21,10,4]




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
    EMAIL VARCHAR(50) NOT NULL UNIQUE
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







