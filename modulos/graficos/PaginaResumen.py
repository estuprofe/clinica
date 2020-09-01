from modulos.modulos_importados import *
from openpyxl import Workbook
from datetime import datetime

#exportar a excel https://es.stackoverflow.com/questions/36060/pasar-los-datos-de-una-lista-a-una-hoja-de-c%C3%A1lculo-mediante-dos-celdas-de-la-ho


class PaginaResumen(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    self.ruta=controlador.ruta
    self.archivo="trimestral.xlsx"
    self.salida = os.path.join(self.ruta,self.archivo)

    label = tk.Label(self, text="Resumen de Facturas", font=controlador.fuente_titulo)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button2 = tk.Button(self, text="Facturado durante el trimestre",
                       command= self.trimestral)
    button.pack()
    button2.pack()

  def trimestral(self):
    facturas = leerTodo("FACTURA")
    clientes = leerTodo("CLIENTE")
    consulta = todoFacturasClientes()

    print (consulta)

   
    excel = Workbook()

    hoja= excel.active
    hoja.title = "Facturado"

    
    

    fila_ptr = 1 #los utilizo a modo de punteros
    columna_ptr = 1
    #1ª fila
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Declaración trimestral")
    fila_ptr +=1
    #2ª fila
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Factura")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Fecha")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Cliente")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="DNI")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Fecha Factura")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Servicios realizados")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="€")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="IVA")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Descuento")
    columna_ptr +=1
    hoja.cell(column=columna_ptr, row=fila_ptr, value="Total facturado €")
    columna_ptr =1
    fila_ptr +=1
    #3ª fila
    factura_leida = "ninguna"
    
    acumulado = 0
    for info in consulta:
        if factura_leida == info[1]:


            acumulado +=info[-2]*(1+info[3]/100)*(1-info[4])

            print ("se tiene en cuenta ", acumulado)
            hoja.cell(column=columna_ptr, row=fila_ptr, value=acumulado)
            continue
        else:
            acumulado = 0


        factura_leida = info[1]
        hoja.cell(column=columna_ptr, row=fila_ptr, value=factura_leida)
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[2])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[8]+' '+info[9])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[7])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[2])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[-3])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[-2])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[3])
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value=info[4])
        columna_ptr +=1
        acumulado += info[-2]*(1+info[3]/100)*(1-info[4])
        hoja.cell(column=columna_ptr, row=fila_ptr, value=acumulado)
        columna_ptr =1
        fila_ptr +=1
        print(info)

    #Grabar el archivo
    excel.save(filename=self.salida)
    comando = "start excel.exe "+"\""+ self.salida +"\""+" &"
    os.system(comando)


















