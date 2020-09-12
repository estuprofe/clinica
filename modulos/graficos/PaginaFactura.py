
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import END

from tkcalendar import Calendar, DateEntry
from datetime import datetime
from modulos.import_export import cal2fecha
from modulos.import_export import imprimir
from modulos.CRUD import *









class PaginaFactura(tk.Frame):

    def __init__(self, padre,  controlador, cliente=None):
        """INICIAR LOS GRÁFICOS DE LA PÁGINA DE FACTURAS"""

        tk.Frame.__init__(self, padre)
        self.cliente = cliente
        self.controlador =  controlador

        ######################################
        #CABECERA
        ######################################
        boton_inicio = tk.Button(self, text="INICIO",
                           command=lambda:  controlador.mostrar_marco("PaginaInicial"))
        boton_inicio.grid(row=00, column = 0)

        boton_ver_clientes = tk.Button(self, text="Ver facturas",
                                   command=lambda: self.ver_facturas())
        boton_ver_clientes.grid(row=1, column = 0)

        boton_actualizar = tk.Button(self, text="actualizar facturas",
                       command=lambda: self.editar_facturas())
        boton_actualizar.grid(row=1, column = 1)

        boton_añadir = tk.Button(self, text="Añadir factura",
                           command=lambda: self.añadir_factura())
        boton_añadir.grid(row=2, column = 0)

        boton_eliminar = tk.Button(self, text="Eliminar factura",
                                   command=lambda: self.eliminar_factura())
        boton_eliminar.grid(row=2, column = 1)

        boton_borrar = tk.Button(self, text="Borrar cuadros",
                           command=lambda: self.borrar())
        boton_borrar.grid(row=2, column = 2)
     
        #caja de facturas
        self.caja_facturas=tk.Listbox(self, height =10, width=70)
        self.caja_facturas.grid(row=0, column=4, rowspan=9, columnspan = 5)
        self.scroll_facturas=tk.Scrollbar(self)
        self.scroll_facturas.grid(row=0, column=10, rowspan=9)
        self.caja_facturas.configure(yscrollcommand=self.scroll_facturas.set)
        self.scroll_facturas.configure(command=self.caja_facturas.yview)
        self.caja_facturas.bind('<<ListboxSelect>>',self.caja_factura_seleccionada)

        boton = ttk.Button(self, text="Elegir Cliente para la factura", 
                               command=lambda: controlador.mostrar_marco("PaginaCliente"))
        boton.grid(row= 7, column = 1)

        
                               #ruta, factura, fecha, nombre, direccion, cp, dni, tratamientos, comentario, iva, descuento, total
        boton = ttk.Button(self, text="Imprimir PDF", 
                               command=self.imprimir)
        boton.grid(row= 7, column = 2)

        #título

        self.label = tk.Label(self, text="Factura", font=self.controlador.fuente_titulo)
        self.label.grid(row=10, column=0)

        self.texto_codigo=StringVar()
        self.etiqueta_codigo = tk.Label(self, text="Codigo de la factura")
        self.etiqueta_codigo.grid(row=11, column = 0)
        self.cuadro_codigo = ttk.Entry(self, textvariable= self.texto_codigo, justify=tk.RIGHT)
        self.cuadro_codigo.grid(row=11, column = 1) 
        self.auto_id_factura= controlador.marcos['PaginaInicial'].cuadro_resultado.get()
        self.cuadro_codigo.insert(END,self.auto_id_factura)

        self.texto_id_factura=StringVar()
        self.texto_id_factura.set("Factura no seleccionada")
        self.etiqueta_id_factura = tk.Label(self, text="ID Factura")
        self.etiqueta_id_factura.grid(row=11, column = 2)
        self.cuadro_id_factura = ttk.Label(self, textvariable= self.texto_id_factura, justify=tk.RIGHT)
        self.cuadro_id_factura.grid(row=11, column = 3)    

        self.texto_cliente=StringVar()
        self.texto_cliente.set("Sin cliente seleccionado")
        self.etiqueta_cliente = tk.Label(self, text="Nº Cliente asociado:")
        self.etiqueta_cliente.grid(row=11, column = 4)
        self.etiqueta_cliente_asignado = ttk.Label(self, textvariable=self.texto_cliente, justify=tk.RIGHT)
        self.etiqueta_cliente_asignado.grid(row=11, column = 5) 

        self.texto_nombre=StringVar()
        self.etiqueta_nombre = tk.Label(self, text="Nombre: ")
        self.etiqueta_nombre.grid(row=12, column = 0)
        self.cuadro_nombre = ttk.Entry(self, textvariable= self.texto_nombre, justify=tk.RIGHT)
        self.cuadro_nombre.grid(row=12, column = 1)

        self.texto_dni=StringVar()
        self.etiqueta_dni = tk.Label(self, text="DNI")
        self.etiqueta_dni.grid(row=12, column = 2)
        self.cuadro_dni = ttk.Entry(self, textvariable= self.texto_dni, justify=tk.RIGHT)
        self.cuadro_dni.grid(row=12, column = 3)

        self.texto_direccion=StringVar()
        self.etiqueta_direccion = tk.Label(self, text="Direccion")
        self.etiqueta_direccion.grid(row=13, column = 0)
        self.cuadro_direccion = ttk.Entry(self, textvariable=self.texto_direccion, justify=tk.RIGHT)
        self.cuadro_direccion.grid(row=13, column = 1)
        
        self.texto_cp=StringVar()
        self.etiqueta_cp = tk.Label(self, text="Código postal")
        self.etiqueta_cp.grid(row=13, column = 2)
        self.cuadro_cp = ttk.Entry(self, textvariable=self.texto_cp, justify=tk.RIGHT)
        self.cuadro_cp.grid(row=13, column = 3)

        self.etiqueta_fecha = tk.Label(self, text="Fecha factura")
        self.etiqueta_fecha.grid(row=14, column = 0)
        self.cal = DateEntry(self, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='es_ES')
        self.cal.grid(row=14, column=1)

        
        self.etiqueta_comentarios = tk.Label(self, text="Comentarios")
        self.etiqueta_comentarios.grid(row=15, column = 0)
        self.cuadro_comentarios = tk.Text(self, width=70, height=10, wrap='word')
        self.cuadro_comentarios.grid(row=15, column = 1, columnspan=3, rowspan=5)
        

        ###############################
        #SERVICIOS
        ##############################
        self.label = tk.Label(self, text="Servicios", font=self.controlador.fuente_titulo)
        self.label.grid(row=129, column=0)
        
        #caja de servicios
        self.caja_servicios=tk.Listbox(self, height =10, width=35)
        self.caja_servicios.grid(row=130, column=1, rowspan=9)
        self.scroll_servicios=tk.Scrollbar(self)
        self.scroll_servicios.grid(row=130, column=2, rowspan=9)
        self.caja_servicios.configure(yscrollcommand=self.scroll_servicios.set)
        self.scroll_servicios.configure(command=self.caja_servicios.yview)
        self.caja_servicios.bind('<<ListboxSelect>>',self.caja_servicio_seleccionado)

        boton_añadir_servicio = tk.Button(self, text="Añadir servicio",
                           command=lambda: self.añadir_servicio())
        boton_añadir_servicio.grid(row=130, column = 4)

        boton_eliminar_servicio = tk.Button(self, text="Eliminar servicio",
                           command=lambda: self.eliminar_servicio())
        boton_eliminar_servicio.grid(row=131, column = 4)

        boton_editar_servicio = tk.Button(self, text="Editar servicio",
                           command=lambda: self.editar_servicio())
        boton_editar_servicio.grid(row=132, column = 4)

        self.etiqueta_fecha_servicio = tk.Label(self, text="Fecha servicio")
        self.etiqueta_fecha_servicio.grid(row=133, column = 3)
        self.cal_servicio = DateEntry(self, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='es_ES')
        self.cal_servicio.grid(row=133, column=4)

        self.texto_tratamiento=StringVar()
        self.etiqueta_tratamiento = tk.Label(self, text="Tratamiento: ")
        self.etiqueta_tratamiento.grid(row=134, column = 3)
        self.cuadro_tratamiento = ttk.Entry(self, textvariable= self.texto_tratamiento, justify=tk.RIGHT)
        self.cuadro_tratamiento.grid(row=134, column = 4)
        self.cuadro_tratamiento.delete(0, END)
        self.cuadro_tratamiento.insert(END, "Sesión de Fisioterapia")

        self.texto_precio_tratamiento=StringVar()
        self.etiqueta_precio_tratamiento = tk.Label(self, text="€: ")
        self.etiqueta_precio_tratamiento.grid(row=135, column = 3)
        self.cuadro_precio_tratamiento = ttk.Entry(self, textvariable= self.texto_precio_tratamiento, justify=tk.RIGHT)
        self.cuadro_precio_tratamiento.grid(row=135, column = 4)
        self.cuadro_precio_tratamiento.delete(0, END)
        self.cuadro_precio_tratamiento.insert(END, 28)

        ###############################
        #PIE DE FACTURA
        ##############################
        self.label = tk.Label(self, text="Calculos", font=self.controlador.fuente_titulo)
        self.label.grid(row=140, column=0)
        
        #calculos

             
        self.etiqueta_iva = tk.Label(self, text="IVA")
        self.etiqueta_iva.grid(row=141, column = 0)
        self.combo_iva = ttk.Combobox(self)
        self.combo_iva["values"] = [0, 4, 16, 21] 
        self.combo_iva.set(0)
        self.combo_iva.bind("<<ComboboxSelected>>", self.combo_seleccionado)
        self.combo_iva.grid(row=141, column = 1)

        self.texto_descuento=StringVar()
        self.etiqueta_descuento = tk.Label(self, text="Descuento")
        self.etiqueta_descuento.grid(row=150, column = 0)
        self.cuadro_descuento= ttk.Entry(self, textvariable= self.texto_descuento, justify=tk.RIGHT)
        self.cuadro_descuento.grid(row=150, column = 1)
        self.cuadro_descuento.bind('<Return>', self.combo_seleccionado)
        self.cuadro_descuento.insert(END,"0")

        self.texto_total=StringVar()
        self.etiqueta_total = tk.Label(self, text="TOTAL")
        self.etiqueta_total.grid(row=160, column = 0)
        self.cuadro_total= ttk.Entry(self, textvariable= self.texto_total, justify=tk.RIGHT)

        self.cuadro_total.grid(row=160, column = 1)
        
        
        # iniciar el cuadro con las facturas

        self.ver_facturas()
        
###############################
        #FUNCIONES
        ##############################
        
    def imprimir(self):
        print("impresión pulsado")
        
        print(self.controlador.ruta, self.cuadro_codigo.get(), self.cal.get(),
                               self.cuadro_nombre.get(), self.cuadro_direccion.get(), self.cuadro_cp.get(), self.cuadro_dni.get()
                               ,self.ver_servicios(), self.cuadro_comentarios.get("1.0", END), self.combo_iva.get(), self.cuadro_descuento.get(),self.cuadro_total.get())
        imprimir(self.controlador.ruta, self.cuadro_codigo.get(), self.cal.get(),
                               self.cuadro_nombre.get(), self.cuadro_direccion.get(), self.cuadro_cp.get(), self.cuadro_dni.get()
                               ,self.ver_servicios(), self.cuadro_comentarios.get("1.0", END), self.combo_iva.get(), self.cuadro_descuento.get(),self.cuadro_total.get())

    def combo_seleccionado(self, event):
        iva_seleccionado = self.combo_iva.get()
        actualizarRegistro("FACTURA", "IVA_ID",
            self.combo_iva.get(),"ID", self.texto_id_factura.get())    
        actualizarRegistro("FACTURA", "DESCUENTO", self.cuadro_descuento.get(),"ID", self.texto_id_factura.get() )
        self.ver_facturas()
        self.actualizar_total()
       

    def editar_facturas(self):
        actualizarRegistro("FACTURA", "CODIGO_FACTURA",
            self.cuadro_codigo.get(),"ID", self.texto_id_factura.get())
        actualizarRegistro("FACTURA", "FECHA_FACTURA",
        cal2fecha(self.cal.get()),"ID", self.texto_id_factura.get())
        actualizarRegistro("FACTURA", "IVA_ID",
            self.combo_iva.get(),"ID", self.texto_id_factura.get())
        actualizarRegistro("FACTURA", "DESCUENTO",
            self.cuadro_descuento.get(),"ID", self.texto_id_factura.get())
        actualizarRegistro("FACTURA", "CLIENTE_ID", self.texto_cliente.get(),"ID", self.texto_id_factura.get() )
        actualizarRegistro("FACTURA", "COMENTARIO",
            self.cuadro_comentarios.get("1.0",END),"ID", self.texto_id_factura.get())
        self.ver_facturas() 
        self.actualizar_total()



    def añadir_factura(self):
        datos = [(self.cuadro_codigo.get(), cal2fecha(self.cal.get()), self.combo_iva.get(), self.cuadro_descuento.get(),
              self.ID_cliente_asociado, self.cuadro_comentarios.get("1.0", END))] 
        print(self.cuadro_comentarios.get("1.0", END))
        crearFactura(datos)
        self.borrar()
        self.texto_id_factura.set(leerTodo("FACTURA")[-1][0])
        self.ver_facturas()
        self.controlador.marcos["PaginaInicial"].siguienteNumero()

    def editar_servicio(self):
        #FECHA_SERVICIO ,        TRATAMIENTO, PRECIO_FINAL,        FACTURA_ID 
        actualizarRegistro("SERVICIO", "FECHA_SERVICIO",
            cal2fecha(self.cal_servicio.get()),"ID", tupla_servicios_seleccionados[0])
        actualizarRegistro("SERVICIO", "TRATAMIENTO",
            self.cuadro_tratamiento.get(),"ID", tupla_servicios_seleccionados[0])
        actualizarRegistro("SERVICIO", "PRECIO_FINAL",
            self.cuadro_precio_tratamiento.get(),"ID", tupla_servicios_seleccionados[0])     
        self.ver_servicios() 
        self.actualizar_total()
   

    def añadir_servicio(self):
        if self.texto_id_factura.get() !="Factura no seleccionada":
            datos = [(cal2fecha(self.cal_servicio.get()), self.cuadro_tratamiento.get(), self.cuadro_precio_tratamiento.get(),
              self.texto_id_factura.get())]#fecha, tratamiento, precio y factura a la que pertenece
            crearServicio(datos)
            self.ver_servicios()
            self.actualizar_total()
        else:
            print("No hay factura seleccionada para asociarle el servicio")  
        
    

    def eliminar_factura(self):
        borrarRegistro("FACTURA","ID", self.texto_id_factura.get())
        self.ver_facturas() 


    def eliminar_servicio(self):
        borrarRegistro("SERVICIO","ID", tupla_servicios_seleccionados[0])
        self.ver_servicios()
        self.actualizar_total() 


    def set_cliente(self,cliente):
        self.cliente = cliente
        id_seleccionado=cliente[0]
        self.cuadro_dni.delete(0,END)
        self.cuadro_dni.insert(END,cliente[1])

        self.ID_cliente_asociado = cliente[0]

        self.texto_cliente.set(cliente[0])

        self.cuadro_nombre.delete(0,END)
        self.cuadro_nombre.insert(END,cliente[2])
        self.cuadro_nombre.insert(END," ")
        self.cuadro_nombre.insert(END,cliente[3])

        self.cuadro_direccion.delete(0,END)
        self.cuadro_direccion.insert(END,cliente[4])
        self.cuadro_direccion.insert(END,". ")
        self.cuadro_direccion.insert(END,cliente[5])
        self.cuadro_direccion.insert(END,". ")
        self.cuadro_direccion.insert(END,cliente[6])

        self.cuadro_cp.delete(0,END)
        self.cuadro_cp.insert(END, cliente[7])

        self.ver_facturas()

        
    def caja_factura_seleccionada(self, evento):
        global tupla_facturas_seleccionadas
        global id_factura
        if (self.caja_facturas.curselection()):
            indice = self.caja_facturas.curselection()[0]

            #print("Al pulsar se ve esto: "+ str(self.caja_facturas.curselection()))
            
            tupla_facturas_seleccionadas=self.caja_facturas.get(indice)

            cliente_factura = leerRegistro("CLIENTE", "ID", tupla_facturas_seleccionadas[5])
            id_factura=str(tupla_facturas_seleccionadas[0])
            
            
            self.texto_id_factura.set(id_factura)
            
            
            self.set_cliente(cliente_factura[0])

            lista_fecha=(str(tupla_facturas_seleccionadas[2]).split("-"))
            self.cal.set_date(datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2])))

            self.cuadro_codigo.delete(0,END)
            self.cuadro_codigo.insert(END,tupla_facturas_seleccionadas[1])

            self.cuadro_comentarios.delete("1.0",END)
            self.cuadro_comentarios.insert(END,tupla_facturas_seleccionadas[6])

            self.combo_iva.set(tupla_facturas_seleccionadas[3])

            self.cuadro_descuento.delete(0,END)
            self.cuadro_descuento.insert(END,tupla_facturas_seleccionadas[4])


            self.caja_facturas.itemconfigure(indice, bg="#00aa00", fg="#fff")#darle colorcito verde a lo seleccionado
            self.caja_facturas.see(indice)# esto es para que se centre en el que que has seleccionado
            
            self.ver_servicios()
            self.actualizar_total()


    def caja_servicio_seleccionado(self, evento):
        global tupla_servicios_seleccionados    
        indice_servicio = self.caja_servicios.curselection()[0]
        tupla_servicios_seleccionados=self.caja_servicios.get(indice_servicio)      
        
        lista_fecha=(str(tupla_servicios_seleccionados[1]).split("-"))
        self.cal_servicio.set_date(datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2])))
        
        self.cuadro_tratamiento.delete(0, END)
        self.cuadro_tratamiento.insert(END, tupla_servicios_seleccionados[2])
      
        self.cuadro_precio_tratamiento.delete(0, END)
        self.cuadro_precio_tratamiento.insert(END, tupla_servicios_seleccionados[3])

        self.caja_servicios.itemconfigure(indice_servicio, bg="#00aa00", fg="#fff")#darle colorcito verde a lo seleccionado
        self.caja_servicios.see(indice_servicio)# esto es para que se centre en el que que has seleccionado

        self.ver_servicios()
        self.actualizar_total()


    def borrar(self):
        self.cuadro_dni.delete(0,END)
        self.cuadro_nombre.delete(0,END)
        self.cuadro_direccion.delete(0,END)
        self.cuadro_cp.delete(0,END)
        self.texto_id_factura.set("Factura no seleccionada")
        self.cuadro_comentarios.delete("1.0",END)
        self.cuadro_codigo.delete(0,END)
        self.caja_servicios.delete(0, END)
        self.combo_iva.set(0)
        self.cuadro_descuento.delete(0,END)
        self.cuadro_descuento.insert(END,"0")
        self.cuadro_total.delete(0,END)
        self.controlador.marcos['PaginaInicial'].actualizar() 
        
    def ver_facturas(self):
        self.caja_facturas.delete(0, END)
        for fila in leerTodo("FACTURA"):
            self.caja_facturas.insert(END,fila)         
   

    def ver_servicios(self):
        servicios_factura=[]
        self.caja_servicios.delete(0, END)
        for fila in leerRegistro("SERVICIO","FACTURA_ID",self.texto_id_factura.get()):
            servicios_factura.append(fila)
            self.caja_servicios.insert(END,fila)
        return servicios_factura
            




    def actualizar_total (self):
        total=0

        for fila in leerRegistro("SERVICIO","FACTURA_ID",self.texto_id_factura.get()):
            total += float(fila[3])
        total_calculado = total  * (1 - float(self.cuadro_descuento.get())*0.01) * (1 + float(self.combo_iva.get())*0.01)
        total_calculado = round(total_calculado, 2)
        print ("Total actualizado a ",total_calculado)
        self.cuadro_total.delete(0, END)
        self.cuadro_total.insert(END, total_calculado)

