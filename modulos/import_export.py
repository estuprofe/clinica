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


def imprimir(ruta, factura, fecha, nombre, direccion, cp, dni, tratamientos, comentario, iva, descuento, total):
    archivo = f"{factura}.pdf"
    ruta = os.path.join(ruta,archivo)
    salto_de_linea=18
    posicion_texto = 750

    print(ruta)
    pdf = canvas.Canvas(ruta, pagesize=A4)
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 18)

    pdf.drawString(100,posicion_texto,"Clínica de Fisioterapia Elisa Isabel García López")
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica', 12)
    pdf.drawString(100,posicion_texto,"Elisa Isabel García López")
    posicion_texto -=salto_de_linea
    pdf.drawString(100,posicion_texto,"DNI: 48482651C")
    posicion_texto -=salto_de_linea
    pdf.drawString(100,posicion_texto,"C/ Agustín Virgili, 25.")
    posicion_texto -=salto_de_linea
    pdf.drawString(100,posicion_texto,"Corvera, Murcia")
    posicion_texto -=salto_de_linea

    pdf.line(100,posicion_texto, 500,posicion_texto)
    posicion_texto -=salto_de_linea

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(100,posicion_texto, "CLIENTE:")
    pdf.setFont('Helvetica', 12)
    posicion_texto -=salto_de_linea
    pdf.drawString(100,posicion_texto, f"{nombre}. DNI: {dni}")
    posicion_texto -=salto_de_linea

    pdf.drawString(100,posicion_texto, f"{direccion} {cp}")
    posicion_texto -=salto_de_linea

    pdf.line(100,posicion_texto, 500,posicion_texto)
    posicion_texto -=salto_de_linea
    
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(100, posicion_texto , f"SERVICIOS:") 
    pdf.setFont('Helvetica', 12) 
    posicion_texto -=salto_de_linea  
    pdf.drawString (100, posicion_texto, "Fecha Servicio")
    pdf.drawString (200, posicion_texto, "|Tratamiento")
    pdf.drawString (400, posicion_texto, "|€")#|    Tratamiento              | Precio")
    posicion_texto -=salto_de_linea

    
    acumulado=0
    for tratamiento in tratamientos:
        print(tratamiento)
        
        pdf.drawString (100, posicion_texto, tratamiento[1])
        pdf.drawString (200, posicion_texto, tratamiento[2])
        pdf.drawString (400, posicion_texto, str(tratamiento[3]))
        acumulado+=tratamiento[3]
        posicion_texto -= salto_de_linea

    pdf.line(100, posicion_texto, 500, posicion_texto)
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(100, posicion_texto, f"Comentarios:")
    pdf.setFont('Helvetica', 12) 
    posicion_texto -=salto_de_linea
    lineas = comentario.split("\n")
    for linea in lineas:
        pdf.drawString(100, posicion_texto, linea)
        posicion_texto -=salto_de_linea
    pdf.line(100, posicion_texto, 500, posicion_texto)
    posicion_texto -=salto_de_linea
    pdf.drawString(100, posicion_texto, f"Acumulado: {acumulado} €")
    posicion_texto -=salto_de_linea
    pdf.drawString(100, posicion_texto, f"Iva: {iva} €")
    posicion_texto -=salto_de_linea
    pdf.drawString(100, posicion_texto, f"Descuento %: {descuento} €")
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica', 18)
    posicion_texto -=salto_de_linea
    pdf.drawString(100, posicion_texto, f"TOTAL: {total} €")
    pdf.setFont('Helvetica', 10)
    posicion_texto -=salto_de_linea
    pdf.drawString(100, posicion_texto, f"Parrafada de protección de datos")

    pdf.save()
    comando = "start AcroRD32 "+"\""+ ruta +"\""+" &"
    os.system(comando)
