from modulos.modulos_importados import *


#exportar a excel https://es.stackoverflow.com/questions/36060/pasar-los-datos-de-una-lista-a-una-hoja-de-c%C3%A1lculo-mediante-dos-celdas-de-la-ho
class PaginaResumen(tk.Frame):
    def __init__(self, padre,  controlador):

        #####################################
        #CARGA INICIAL DEL OBJETO PÁGINA#
        #####################################
        tk.Frame.__init__(self, padre)
        ##setup para archivos excel
        self.controlador =  controlador
        self.ruta=controlador.ruta
        self.archivo="trimestral.xlsx"
        self.salida = os.path.join(self.ruta,self.archivo)
        #####################################
        #GRÁFICOS#
        #####################################
        label = tk.Label(self, text="Resumen de Facturas", font=controlador.fuente_titulo)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ir al principio",
                           command=lambda:  controlador.mostrar_marco("PaginaInicial"))
        button2 = tk.Button(self, text="Facturado durante el trimestre",
                           command= self.trimestral)
        button.pack()
        button2.pack()
        datos_cliente_inicial=[('','Clientes contado','','','','','','','')]
        try:
            crearCliente(datos_cliente_inicial)
        except:
            print('Cliente ya creado')
        try:
            self.controlador.marcos['PaginaInicial'].actualizar()#hasta que no están todas las páginas creadas no puedo asignar la numeración automática, esta es la última página en inicializarse, por eso lo pongo aquí
        except:
            print('Sin id_factura')

        #####################################
        #FUNCIONES#
        #####################################
    def trimestral(self):
        #facturas = leerTodo("FACTURA")
        #clientes = leerTodo("CLIENTE")
        fecha_inicial=cal2fecha(self.controlador.marcos['PaginaInicial'].cal_inicio.get())
        print(fecha_inicial)
        fecha_final=cal2fecha(self.controlador.marcos['PaginaInicial'].cal_fin.get())
        print(fecha_final)
        consulta = todoFacturasClientes("CODIGO_FACTURA", "FECHA_FACTURA", fecha_inicial, fecha_final)
        
        print ("Esta es la consulta que recibe antes de pasar a excel: \n",consulta)
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
        hoja.cell(column=columna_ptr, row=fila_ptr, value="IVA %")
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value="Descuento % ")
        columna_ptr +=1
        hoja.cell(column=columna_ptr, row=fila_ptr, value="Total facturado €(Impuestos y descuentos incluidos")
        columna_ptr =1
        fila_ptr +=1
        #3ª fila
        factura_leida = "ninguna"
        
        acumulado = 0
        for info in consulta:
            if factura_leida == info[1]:

                
                acumulado +=info[-2]

                print ("se tiene en cuenta ", acumulado)
                hoja.cell(column=columna_ptr+6, row=fila_ptr-1, value=acumulado)
                hoja.cell(column=columna_ptr+9, row=fila_ptr-1, value=round((acumulado*(1+info[3]/100))*(1-info[4]/100),2))
                continue
            else:
                acumulado = 0
                

            
            factura_leida = info[1]
            hoja.cell(column=columna_ptr, row=fila_ptr, value=factura_leida)#codigo
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[2])#fecha
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[9]+' '+info[10]) #nombre
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[8])#DNI
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[-4])#fecha último servicio
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[-3])#tratamiento
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[-2])#Precio del tratamiento
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[3])#IVA
            columna_ptr +=1
            hoja.cell(column=columna_ptr, row=fila_ptr, value=info[4])#Descuento
            columna_ptr +=1
            acumulado += info[-2]*(1+info[3]/100)*(1-info[4]/100)
            acumulado = round(acumulado, 2)
            hoja.cell(column=columna_ptr, row=fila_ptr, value=acumulado)
            columna_ptr =1
            fila_ptr +=1
            
            print(info)

        #Grabar el archivo
        excel.save(filename=self.salida)
        comando = "start excel.exe "+"\""+ self.salida +"\""+" &"
        os.system(comando)





















