from modulos.modulos_importados import *

from datetime import *

    



class PaginaFactura(tk.Frame):

    def __init__(self, padre,  controlador, cliente=None):

        tk.Frame.__init__(self, padre)
        self.cliente = cliente
        self.controlador =  controlador
        #caja de facturas
        self.caja_facturas=tk.Listbox(self, height =10, width=35)
        self.caja_facturas.grid(row=0, column=3, rowspan=9, columnspan = 4)
        self.scroll_facturas=tk.Scrollbar(self)
        self.scroll_facturas.grid(row=0, column=6, rowspan=9)
        self.caja_facturas.configure(yscrollcommand=self.scroll_facturas.set)
        self.scroll_facturas.configure(command=self.caja_facturas.yview)
        self.caja_facturas.bind('<<ListboxSelect>>',self.caja_factura_seleccionada)
        #título
        self.label = tk.Label(self, text="Factura", font=self.controlador.fuente_titulo)
        self.label.grid(column=0, row=10)

        self.texto_id_factura=StringVar()
        self.etiqueta_id_factura = tk.Label(self, text="ID Factura")
        self.etiqueta_id_factura.grid(row=11, column = 0)
        self.cuadro_id_factura = ttk.Entry(self, textvariable= self.texto_id_factura, justify=tk.RIGHT)
        self.cuadro_id_factura.grid(row=11, column = 1)
        

        

        self.texto_codigo=StringVar()
        self.etiqueta_codigo = tk.Label(self, text="Codigo de la factura")
        self.etiqueta_codigo.grid(row=20, column = 3)
        self.cuadro_codigo = ttk.Entry(self, textvariable= self.texto_codigo, justify=tk.RIGHT)
        self.cuadro_codigo.grid(row=20, column = 4)
        self.auto_id_factura= self.controlador.letraFactura+self.controlador.añoFactura+cuatroDigitar(leerTodo("FACTURA")[-1][0]+1)
        self.cuadro_codigo.insert(END,self.auto_id_factura)
        
        self.etiqueta_fecha = tk.Label(self, text="Fecha factura")
        self.etiqueta_fecha.grid(row=30, column = 3)
        self.cal = DateEntry(self, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='es_ES')
        self.cal.grid(row=30, column=4)
        #ttk.Button(self, text="ok", command = lambda: self.ver_fecha()).grid(row=3, column=2)

        self.texto_cliente=StringVar()
        self.etiqueta_cliente = tk.Label(self, text="ID Cliente: ")
        self.etiqueta_cliente.grid(row=11, column = 2)
        self.cuadro_cliente = ttk.Entry(self, textvariable= self.texto_cliente, justify=tk.RIGHT)
        self.cuadro_cliente.grid(row=11, column = 3)

        self.texto_nombre=StringVar()
        self.etiqueta_nombre = tk.Label(self, text="Nombre: ")
        self.etiqueta_nombre.grid(row=12, column = 0)
        self.cuadro_nombre = ttk.Entry(self, textvariable= self.texto_nombre, justify=tk.RIGHT)
        self.cuadro_nombre.grid(row=12, column = 1)


        self.texto_dni=StringVar()
        self.etiqueta_dni = tk.Label(self, text="DNI")
        self.etiqueta_dni.grid(row=20, column = 0)
        self.cuadro_dni = ttk.Entry(self, textvariable= self.texto_dni, justify=tk.RIGHT)
        self.cuadro_dni.grid(row=20, column = 1)

        self.texto_direccion=StringVar()
        self.etiqueta_direccion = tk.Label(self, text="Direccion")
        self.etiqueta_direccion.grid(row=50, column = 0)
        self.cuadro_direccion = ttk.Entry(self, textvariable=self.texto_direccion, justify=tk.RIGHT)
        self.cuadro_direccion.grid(row=50, column = 1)
            

        

        #caja de facturas
        self.caja_servicios=tk.Listbox(self, height =10, width=35)
        self.caja_servicios.grid(row=130, column=0, rowspan=9, columnspan = 4)
        self.scroll_servicios=tk.Scrollbar(self)
        self.scroll_servicios.grid(row=130, column=3, rowspan=9)
        self.caja_servicios.configure(yscrollcommand=self.scroll_servicios.set)
        self.scroll_servicios.configure(command=self.caja_servicios.yview)
        self.caja_servicios.bind('<<ListboxSelect>>',self.caja_servicio_seleccionado)
      
        
        
        self.etiqueta_iva = tk.Label(self, text="IVA")
        self.etiqueta_iva.grid(row=140, column = 0)
        self.combo_iva = ttk.Combobox(self)
        self.combo_iva["values"] = [0, 4, 16, 21] #TODO- hacer que lo coja de la base de datos
        self.combo_iva.set(0)
        self.combo_iva.bind("<<ComboboxSelected>>", self.combo_seleccionado)
        self.combo_iva.grid(row=140, column = 1)

        self.texto_descuento=StringVar()
        self.etiqueta_descuento = tk.Label(self, text="Descuento")
        self.etiqueta_descuento.grid(row=150, column = 0)
        self.cuadro_descuento= ttk.Entry(self, textvariable= self.texto_descuento, justify=tk.RIGHT)
        self.cuadro_descuento.grid(row=150, column = 1)
        self.cuadro_descuento.insert(END,"0")

        self.texto_total=StringVar()
        self.etiqueta_total = tk.Label(self, text="TOTAL")
        self.etiqueta_total.grid(row=160, column = 0)
        self.cuadro_total= ttk.Entry(self, textvariable= self.texto_total, justify=tk.RIGHT)
        self.cuadro_total.grid(row=160, column = 1)

       
        self.texto_cp=StringVar()
        self.etiqueta_cp = tk.Label(self, text="Código postal")
        self.etiqueta_cp.grid(row=80, column = 0)
        self.cuadro_cp = ttk.Entry(self, textvariable=self.texto_cp, justify=tk.RIGHT)
        self.cuadro_cp.grid(row=80, column = 1)

        self.etiqueta_fecha_servicio = tk.Label(self, text="Fecha servicio")
        self.etiqueta_fecha.grid(row=133, column = 3)
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
        self.cuadro_precio_tratamiento.insert(END, 32)

        


        boton = ttk.Button(self, text='Elegir Cliente para la factura', 
                               command=lambda: controlador.mostrar_marco("PaginaCliente"))
        boton.grid(row= 10, column = 20)
        
        boton_inicio = tk.Button(self, text="INICIO",
                           command=lambda:  controlador.mostrar_marco("PaginaInicial"))
        boton_inicio.grid(row=00, column = 30)

        boton_combo = tk.Button(self, text="Prueba Combo",
                           command= self.combo_seleccionado)
        boton_combo.grid(row=90, column = 30)

        boton_actualizar = tk.Button(self, text="actualizar facturas",
                       command=lambda: self.editar_facturas())
        boton_actualizar.grid(row=1, column = 1)

        boton_borrar = tk.Button(self, text="Borrar cuadros",
                           command=lambda: self.borrar())

        boton_borrar.grid(row=2, column = 2)



        boton_ver_clientes = tk.Button(self, text="Ver facturas",
                                   command=lambda: self.ver_facturas())
        boton_ver_clientes.grid(row=1, column = 0)

         
               

        boton_eliminar = tk.Button(self, text="Eliminar factura",
                                   command=lambda: self.eliminar_factura())
        boton_eliminar.grid(row=2, column = 1)


        boton_añadir = tk.Button(self, text="Añadir factura",
                           command=lambda: self.añadir_factura())
        boton_añadir.grid(row=2, column = 0)

        boton_añadir_servicio = tk.Button(self, text="Añadir servicio",
                           command=lambda: self.añadir_servicio())
        boton_añadir_servicio.grid(row=130, column = 4)

        boton_eliminar_servicio = tk.Button(self, text="Eliminar servicio",
                           command=lambda: self.eliminar_servicio())
        boton_eliminar_servicio.grid(row=131, column = 4)

        boton_editar_servicio = tk.Button(self, text="Editar servicio",
                           command=lambda: self.eliminar_servicio())
        boton_editar_servicio.grid(row=132, column = 4)


        
        # iniciar el cuadro con las facturas
        
    def combo_seleccionado(self, event):
        iva_seleccionado = self.combo_iva.get()
        actualizarRegistro("FACTURA", "IVA_ID",
         self.combo_iva.get(),"ID", self.cuadro_id_factura.get())
        
        self.ver_facturas()
        self.actualizar_total()

        
            
    def editar_facturas(self):
        actualizarRegistro("FACTURA", "CODIGO_FACTURA",
         self.cuadro_codigo.get(),"ID", self.cuadro_id_factura.get())

        actualizarRegistro("FACTURA", "FECHA_FACTURA",
        cal2fecha(self.cal.get()),"ID", self.cuadro_id_factura.get())
        

        actualizarRegistro("FACTURA", "IVA_ID",
         self.combo_iva.get(),"ID", self.cuadro_id_factura.get())

        actualizarRegistro("FACTURA", "DESCUENTO",
         self.cuadro_descuento.get(),"ID", self.cuadro_id_factura.get())

        self.ver_facturas() 
        self.actualizar_total()


        
    def añadir_factura(self):
        datos = [(self.cuadro_codigo.get(), cal2fecha(self.cal.get()), self.combo_iva.get(), self.cuadro_descuento.get(),
              self.cuadro_cliente.get())] 
    #print(datos)
        crearFactura(datos)
        print(leerTodo("FACTURA")[-1])
        self.cuadro_id_factura.delete(0,END)
        self.cuadro_id_factura.insert(END, leerTodo("FACTURA")[-1][0])

        self.ver_facturas()

    def añadir_servicio(self):
        datos = [(cal2fecha(self.cal_servicio.get()), self.cuadro_tratamiento.get(), self.cuadro_precio_tratamiento.get(),
              self.cuadro_id_factura.get())]#fecha, tratamiento, precio y factura a la que pertenece
    #print(datos)
        crearServicio(datos)

        self.ver_servicios()
        self.actualizar_total()
    
    def eliminar_factura(self):
        borrarRegistro("FACTURA","ID", self.cuadro_id_factura.get())
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

        self.cuadro_cliente.delete(0,END)
        self.cuadro_cliente.insert(END,cliente[0])

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



        actualizarRegistro("FACTURA", "CLIENTE_ID", cliente[0], "ID", id_factura)
        self.ver_facturas()

        

    def caja_factura_seleccionada(self, evento):

        global tupla_facturas_seleccionadas
        global id_factura

        indice = self.caja_facturas.curselection()[0]
        

        print("Al pulsar se ve esto: "+ str(self.caja_facturas.curselection()))

        tupla_facturas_seleccionadas=self.caja_facturas.get(indice)
        cliente_factura = leerRegistro("CLIENTE", "ID", tupla_facturas_seleccionadas[5])
        


        id_factura=tupla_facturas_seleccionadas[0]

        self.cuadro_id_factura.delete(0,END)
        self.cuadro_id_factura.insert(END,tupla_facturas_seleccionadas[0])

        self.cuadro_cliente.delete(0,END)
        self.set_cliente(cliente_factura[0])

        lista_fecha=(str(tupla_facturas_seleccionadas[2]).split("-"))
        self.cal.set_date(datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2])))

        self.cuadro_codigo.delete(0,END)
        self.cuadro_codigo.insert(END,tupla_facturas_seleccionadas[1])

        self.combo_iva.set(tupla_facturas_seleccionadas[3])

        self.cuadro_descuento.delete(0,END)
        self.cuadro_descuento.insert(END,tupla_facturas_seleccionadas[4])

        self.ver_servicios()
        self.actualizar_total()

    def caja_servicio_seleccionado(self, evento):

        global tupla_servicios_seleccionados
        
        indice = self.caja_servicios.curselection()[0]
        


        tupla_servicios_seleccionados=self.caja_servicios.get(indice)
        
        
        lista_fecha=(str(tupla_servicios_seleccionados[1]).split("-"))
        self.cal_servicio.set_date(datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2])))
        
        self.cuadro_tratamiento.delete(0, END)
        self.cuadro_tratamiento.insert(END, tupla_servicios_seleccionados[2])
        self.cuadro_precio_tratamiento.delete(0, END)
        self.cuadro_precio_tratamiento.insert(END, tupla_servicios_seleccionados[3])

        self.ver_servicios()
        self.actualizar_total()



    def borrar(self):
        self.cuadro_dni.delete(0,END)
        self.cuadro_cliente.delete(0,END)
        self.cuadro_nombre.delete(0,END)
        self.cuadro_direccion.delete(0,END)
        self.cuadro_cp.delete(0,END)
        self.cuadro_id_factura.delete(0,END)
        self.cuadro_cliente.delete(0,END)
        self.cuadro_codigo.delete(0,END)
        self.combo_iva.set(0)
        self.cuadro_descuento.delete(0,END)




        
    def ver_facturas(self):
        self.caja_facturas.delete(0, END)
        for fila in leerTodo("FACTURA"):
            self.caja_facturas.insert(END,fila)         
            
    def ver_servicios(self):
        self.caja_servicios.delete(0, END)
        for fila in leerRegistro("SERVICIO","FACTURA_ID",self.cuadro_id_factura.get()):
            self.caja_servicios.insert(END,fila) 

    def actualizar_total (self):
        total=0
        for fila in leerRegistro("SERVICIO","FACTURA_ID",self.cuadro_id_factura.get()):
            total += int(fila[3])

        total_calculado = total  * (1 - int(self.cuadro_descuento.get())*0.01) * (1 + int(self.combo_iva.get())*0.01)
        print (total_calculado)
        self.cuadro_total.delete(0, END)
        self.cuadro_total.insert(END, total_calculado)

