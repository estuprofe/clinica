from modulos.CRUD import *

# setup

ivas = [21, 10, 4]

#Creación de la BD y la tabla
if not(os.path.isfile(nombreBD)):
    miConexion = sqlite3.connect(nombreBD)
    miCursor = miConexion.cursor()
    miCursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTE(
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

    miCursor.execute('''CREATE TABLE IF NOT EXISTS FACTURA(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODIGO_FACTURA VARCHAR(7) NOT NULL UNIQUE,
    FECHA_FACTURA DATE NOT NULL,
    SERVICIO_ID INTEGER,
    IVA_ID INTEGER,
    DESCUENTO INTEGER,
    PRECIO_FINAL REAL,
    CLIENTE_ID INTEGER,
    FOREIGN KEY(IVA_ID) REFERENCES IVA(ID),
    FOREIGN KEY(CLIENTE_ID) REFERENCES CLIENTE(ID),
    FOREIGN KEY(SERVICIO_ID) REFERENCES SERVICIO(ID)
    )''')

    miCursor.execute('''CREATE TABLE IF NOT EXISTS SERVICIO(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FECHA_SERVICIO DATE NOT NULL,
    TRATAMIENTO TEXT,
    PRECIO_FINAL REAL,
    FACTURA_ID INTEGER
    )''')

    miCursor.execute('''CREATE TABLE IF NOT EXISTS IVA(
    IVA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIPO INTEGER NOT NULL
    )''')
    for i in ivas:
        miCursor.execute(f'INSERT INTO IVA VALUES (NULL,{i})')
    miConexion.commit()
    miConexion.close()

else:
    print(f'El archivo {nombreBD} ya existe')

if __name__ == "__main__":
    leerTodo('CLIENTE')
    leerTodo('FACTURA')
    leerTodo('SERVICIO')
    leerTodo('IVA')
# funciones CRUD
"""
#PRUEBAS DE INICIO DE BD
    datos=[('123','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfg43434343rgrddd4gr'),
    ('1222ff2223','Antonio','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfg43343rgrddd4gr'),
    ('1222ff22','Jaime','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putomail.comfd4gr'),
    ('1222f','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','putrgrddd4gr'),
    ('1222','Luis','Zurita Herrera', 'micalle','jorelre','ererer','12342','69696868','prgrddd4gr')]

    crearCliente(datos)
    leerRegistro('CLIENTE','NOMBRE','Luis')


    actualizarRegistro('CLIENTE','DIRECCION', 'definitivamente sí', 'NOMBRE', 'Luis')
    leerRegistro('CLIENTE','NOMBRE','Luis')
    borrarRegistro('CLIENTE', 'DNI', '123')
    leerRegistro('CLIENTE','NOMBRE','Luis')
    leerTodo('CLIENTE')
#PROBANDO SERVICIOS, LEER DATOS, CAMBIAR, CREAR FACTURAS...
    servicioDatos = [("2020/07/10","Masaje",50.35,1)]
    crearServicio(servicioDatos)
    leerTodo('SERVICIO')
    actualizarRegistro('SERVICIO','TRATAMIENTO','CAMBIADO EL TRATAMIENTO', 'ID',1)
    leerTodo('SERVICIO')
    facturaDatos=[('F200001','2020/07/15',1,3,20,20.93,1),
                ('F200002','2020/07/16',2,3,15,28.00,2)] 
    crearFactura(facturaDatos)
    leerTodo('FACTURA')"""