#exportar a pdf  https://ricardogeek.com/como-crear-documentos-pdf-usando-python/
#http://www.pythondiario.com/2015/04/generar-un-pdf-partir-de-un-sencillo.html
import os
import os.path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from datetime import *

variable_de_prueba="MECAGOENTOTUSMUERTOSQUENOSEIMPORTA"

def cuatroDigitar(numero):

    if numero < 10:
        cadena = "000"+str(numero)
    elif numero < 100:
        cadena = "00" + str(numero)
    elif numero < 1000:
        cadena = "0"+ str(numero)
    else:
        cadena = str(numero)
    return cadena

def cal2fecha(fecha):
    fecha=fecha.split("/")
    fecha = datetime(2000+int(fecha[2]),int(fecha[1]),int(fecha[0])).date()
    return fecha


def imprimir(ruta, factura, fecha, nombre, direccion, cp, dni, tratamientos, descuento, total):
    archivo = f"{factura}.pdf"
    ruta = os.path.join(ruta,archivo)

    print(ruta)
    pdf = canvas.Canvas(ruta, pagesize=A4)
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 18)

    pdf.drawString(100,750,"Clínica de Fisioterapia Elisa Isabel García López")
    pdf.setFont('Helvetica', 12)
    pdf.drawString(100,720,"Elisa Isabel García López")
    pdf.drawString(100,690,"DNI: 48482651C")
    pdf.drawString(100,660,"C/ Agustín Virgili, 25.")
    pdf.drawString(100,630,"Corvera, Murcia")

    pdf.line(100,600, 500, 600)

    pdf.drawString(100,570, "CLIENTE:")
    pdf.drawString(100,540, f"{nombre}. DNI: {dni}")

    pdf.drawString(100,510, f"{direccion} {cp}")

    pdf.line(100,500, 500, 500)
    pdf.drawString(100, 470 , f"SERVICIOS:")
    
    pdf.drawString (100, 430, "Fecha Servicio")
    pdf.drawString (200, 430, "|Tratamiento")
    pdf.drawString (400, 430, "|€")#|    Tratamiento              | Precio")

    posicion_texto = 400
    acumulado=0
    for tratamiento in tratamientos:
        print(tratamiento)
        
        pdf.drawString (100, posicion_texto, tratamiento[1])
        pdf.drawString (200, posicion_texto, tratamiento[2])
        pdf.drawString (400, posicion_texto, str(tratamiento[3]))
        acumulado+=tratamiento[3]
        posicion_texto -=30

    pdf.line(100, posicion_texto, 500, posicion_texto)
    posicion_texto -=30
    pdf.drawString(100, posicion_texto, f"Acumulado: {acumulado} €")
    posicion_texto -=30
    pdf.drawString(100, posicion_texto, f"Descuento %: {descuento} €")
    posicion_texto -=30
    pdf.setFont('Helvetica', 18)
    posicion_texto -=30
    pdf.drawString(100, posicion_texto, f"TOTAL: {total} €")

    pdf.save()
    comando = "start AcroRD32 "+"\""+ ruta +"\""+" &"
    os.system(comando)
