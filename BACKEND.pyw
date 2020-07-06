import sqlite3
miConexion = sqlite3.connect("clinica")

miCursor = miConexion.cursor()

miCursor.execute(
    "CREATE TABLE CLIENTE (ID INTEGER,NOMBRE VARCHAR(50),APELLIDOS VARCHAR(50))")




miConexion.close()
