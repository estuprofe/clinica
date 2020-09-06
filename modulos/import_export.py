#exportar a pdf  https://ricardogeek.com/como-crear-documentos-pdf-usando-python/
#http://www.pythondiario.com/2015/04/generar-un-pdf-partir-de-un-sencillo.html
import os
import os.path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from datetime import *

variable_de_prueba="MECAGOENTOTUSMUERTOSQUENOSEIMPORTA"
parrafada_datos = "EN CUMPLIMIENTO DEL RUE 2016/679 - 27 abril le informamos que El Responsable: ELISA ISABEL GARCIA LOPEZ©                          CENTRO DE FISIOTERAPIA;  Delegado de Protección de datos:protecciondedatos@totaldata.es; Finalidad del tratamiento de datos: Gestión de servicios dentro de la actividad CENTRO DE FISIOTERAPIA;¿Que nos legitima a tratar sus datos?: Ejecución de un contrato y consentimiento explícito del interesado; Destinatarios: No se cederán datos a terceros, salvo obligación legal. Publicación de su imagen en web y/o redes sociales: (Me opongo __); Envío información comercial sobre productos y servicios relacionados con los servicios solicitados y fidelizarle como cliente: (Me opongo ); Derechos Usted tiene derecho a obtener confirmación sobre si estamos tratando sus datos personales por tanto tiene derecho a acceder a sus datos personales, rectificar los datos inexactos o solicitar su supresión cuando los datos ya no sean necesarios. Ejercicio de derechos ELISA ISABEL GARCIA LOPEZ © CENTRO DE FISIOTERAPIA o al Correo electrónico  DPO: protecciondedatos@totaldata.es indicando el nombre de la empresa; Información adicional en la dirección indicada o en la web"

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
    margen = 70

    print(ruta)
    pdf = canvas.Canvas(ruta, pagesize=A4)
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 18)

    pdf.drawString(margen,posicion_texto,"Clínica de Fisioterapia Elisa Isabel García López")
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica', 12)
    pdf.drawString(margen,posicion_texto,"Elisa Isabel García López")
    posicion_texto -=salto_de_linea
    pdf.drawString(margen ,posicion_texto,"DNI: 48482651C")
    posicion_texto -=salto_de_linea
    pdf.drawString(margen ,posicion_texto,"C/ Agustín Virgili, 25.")
    posicion_texto -=salto_de_linea
    pdf.drawString(margen ,posicion_texto,"Corvera, Murcia")
    posicion_texto -=salto_de_linea

    pdf.line(margen ,posicion_texto, 500,posicion_texto)
    posicion_texto -=salto_de_linea

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(margen ,posicion_texto, "CLIENTE:")
    pdf.setFont('Helvetica', 12)
    posicion_texto -=salto_de_linea
    pdf.drawString(margen ,posicion_texto, f"{nombre}. DNI: {dni}")
    posicion_texto -=salto_de_linea

    pdf.drawString(margen ,posicion_texto, f"{direccion} {cp}")
    posicion_texto -=salto_de_linea

    pdf.line(margen ,posicion_texto, 500,posicion_texto)
    posicion_texto -=salto_de_linea
    
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(margen , posicion_texto , f"SERVICIOS:") 
    pdf.setFont('Helvetica', 12) 
    posicion_texto -=salto_de_linea  
    pdf.drawString (margen , posicion_texto, "Fecha Servicio")
    pdf.drawString (margen*3, posicion_texto, "|Tratamiento")
    pdf.drawString (margen*5, posicion_texto, "|€")#|    Tratamiento              | Precio")
    posicion_texto -=salto_de_linea

    
    acumulado=0
    for tratamiento in tratamientos:
        print(tratamiento)
        
        pdf.drawString (margen, posicion_texto, tratamiento[1])
        pdf.drawString (margen*3, posicion_texto, "|"+tratamiento[2])
        pdf.drawString (margen*5, posicion_texto, "|"+str(tratamiento[3]))
        acumulado+=tratamiento[3]
        posicion_texto -= salto_de_linea

    pdf.line(margen , posicion_texto, 500, posicion_texto)
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(margen , posicion_texto, f"Comentarios:")
    pdf.setFont('Helvetica', 12) 
    posicion_texto -=salto_de_linea
    lineas = comentario.split("\n")
    for linea in lineas:
        pdf.drawString(margen , posicion_texto, linea)
        posicion_texto -=salto_de_linea
    pdf.line(margen , posicion_texto, 500, posicion_texto)
    posicion_texto -=salto_de_linea
    pdf.drawString(margen , posicion_texto, f"Acumulado: {acumulado} €")
    posicion_texto -=salto_de_linea
    eurosIva = round(acumulado*(float(iva)/100),2)
    pdf.drawString(margen , posicion_texto, f"Iva: {iva}% = {eurosIva} €")
    posicion_texto -=salto_de_linea
    eurosDescuento = round(acumulado * (float(descuento)/100),2)
    pdf.drawString(margen , posicion_texto, f"Descuento: {descuento}% = {eurosDescuento} €")
    posicion_texto -=salto_de_linea
    pdf.setFont('Helvetica', 18)
    posicion_texto -=salto_de_linea
    pdf.drawString(margen , posicion_texto, f"TOTAL: {total} €")
    pdf.setFont('Helvetica', 7)
    posicion_texto -=salto_de_linea
    print (len(parrafada_datos))
    linea_texto = ""
    pos_inicial= 0
    caracteres = 0
    salto_de_linea=8
    for letra in parrafada_datos:
        caracteres +=1
        if caracteres % 130 == 0 or caracteres == len(parrafada_datos):
            linea=parrafada_datos[pos_inicial:caracteres].encode("utf-8")
            print(linea)
            pdf.drawString(margen , posicion_texto, linea)
            pos_inicial=caracteres
            posicion_texto -=salto_de_linea

    pdf.save()
    comando = "start AcroRD32 "+"\""+ ruta +"\""+" &"
    os.system(comando)
