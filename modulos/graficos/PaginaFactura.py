from modulos.modulos_importados import *

def VentanaClientes(self):

    self.ventana= tk.Toplevel()
    self.ventana.title('Elige al cliente')    
    self.ventana.geometry('300x200')
        
        
        

    self.caja_clientes=tk.Listbox(self.ventana, height =10, width=35)
    self.caja_clientes.grid(row=4, column=3, rowspan=9, columnspan = 2)
    self.scroll=tk.Scrollbar(self.ventana)
    self.scroll.grid(row=4, column=5, rowspan=9)
    self.caja_clientes.configure(yscrollcommand=self.scroll.set)
    self.scroll.configure(command=self.caja_clientes.yview)
    self.caja_clientes.bind('<<ListboxSelect>>',self.coger_filas_seleccionadas)
        



class PaginaFactura(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    #título
    self.label = tk.Label(self, text="Factura", font=self.controlador.fuente_titulo)
    self.label.grid(column=0, row=0)

    self.texto_id=StringVar()
    self.etiqueta_id = tk.Label(self, text="ID")
    self.etiqueta_id.grid(row=1, column = 3)
    self.cuadro_id = ttk.Entry(self, textvariable= self.texto_id, justify=tk.RIGHT)
    self.cuadro_id.grid(row=1, column = 4)

    self.texto_codigo=StringVar()
    self.etiqueta_codigo = tk.Label(self, text="Codigo de la factura")
    self.etiqueta_codigo.grid(row=2, column = 3)
    self.cuadro_codigo = ttk.Entry(self, textvariable= self.texto_codigo, justify=tk.RIGHT)
    self.cuadro_codigo.grid(row=2, column = 4)
    
    self.etiqueta_fecha = tk.Label(self, text="Fecha factura")
    self.etiqueta_fecha.grid(row=3, column = 3)
    self.cal = DateEntry(self, width=12, background='darkblue',
                    foreground='white', borderwidth=2, locale='es_ES')
    self.cal.grid(row=3, column=4)
    #ttk.Button(self, text="ok", command = lambda: self.ver_fecha()).grid(row=3, column=2)

    self.texto_cliente=StringVar()
    self.etiqueta_cliente = tk.Label(self, text="Cliente: ")
    self.etiqueta_cliente.grid(row=1, column = 0)
    self.cuadro_cliente = ttk.Entry(self, textvariable= self.texto_codigo, justify=tk.RIGHT)
    self.cuadro_cliente.grid(row=1, column = 1)

    boton = ttk.Button(self, text='Elegir Cliente para la factura', 
                           command=self.abrir_cliente)
    boton.grid(row= 1, column = 2)

    self.texto_servicio=StringVar()
    self.etiqueta_servicio = tk.Label(self, text="Tabla de servicios")
    self.etiqueta_servicio.grid(row=13, column = 0)
    self.cuadro_servicio = ttk.Entry(self, textvariable= self.texto_servicio, justify=tk.RIGHT)
    self.cuadro_servicio.grid(row=13, column = 1)

  
    self.texto_iva=StringVar()
    self.etiqueta_iva = tk.Label(self, text="IVA")
    self.etiqueta_iva.grid(row=14, column = 0)
    self.cuadro_iva = ttk.Entry(self, textvariable= self.texto_servicio, justify=tk.RIGHT)
    self.cuadro_iva.grid(row=14, column = 1)

    self.texto_descuento=StringVar()
    self.etiqueta_descuento = tk.Label(self, text="Descuento")
    self.etiqueta_descuento.grid(row=15, column = 0)
    self.cuadro_descuento= ttk.Entry(self, textvariable= self.texto_servicio, justify=tk.RIGHT)
    self.cuadro_descuento.grid(row=15, column = 1)

    self.texto_total=StringVar()
    self.etiqueta_total = tk.Label(self, text="TOTAL")
    self.etiqueta_total.grid(row=16, column = 0)
    self.cuadro_total= ttk.Entry(self, textvariable= self.texto_servicio, justify=tk.RIGHT)
    self.cuadro_total.grid(row=16, column = 1)



    

    


    




  def coger_filas_seleccionadas(self,event):
    global tupla_seleccionados
    global id_seleccionado    

    

  def ver(self):
    self.caja_clientes.delete(0, END)
    for fila in leerTodo("CLIENTE"):
        self.caja_clientes.insert(END,fila)



  def editar(self):
    #print("CLIENTE", "DNI",self.cuadro_dni.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "DNI",self.cuadro_dni.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "NOMBRE",self.cuadro_nombre.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "APELLIDOS",self.cuadro_apellido.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "DIRECCION",self.cuadro_direccion.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "MUNICIPIO",self.cuadro_municipio.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "PROVINCIA",self.cuadro_provincia.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "CODIGO_POSTAL",self.cuadro_cp.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "TELEFONO",self.cuadro_telefono.get(),"CLIENTE_ID", id_seleccionado)
    actualizarRegistro("CLIENTE", "EMAIL",self.cuadro_email.get(),"CLIENTE_ID", id_seleccionado)
    self.ver()

  def borrar(self):

    self.cuadro_dni.delete(0,END)
    self.cuadro_nombre.delete(0,END)
    self.cuadro_apellido.delete(0,END)
    self.cuadro_direccion.delete(0,END)
    self.cuadro_municipio.delete(0,END)
    self.cuadro_provincia.delete(0,END)
    self.cuadro_cp.delete(0,END)
    self.cuadro_telefono.delete(0,END)
    self.cuadro_email.delete(0,END)

  def eliminar(self):
    borrarRegistro("CLIENTE", "CLIENTE_ID", id_seleccionado)


  def añadir(self):
    datos = [(self.cuadro_dni.get(), self.cuadro_nombre.get(), self.cuadro_apellido.get(), self.cuadro_direccion.get(),
              self.cuadro_municipio.get(), self.cuadro_provincia.get(), self.cuadro_cp.get(), self.cuadro_telefono.get(), self.cuadro_email.get())]
    #print(datos)
    crearCliente(datos)
    self.ver()





  def ver_fecha(self):
        print(self.cal.get_date())

  def abrir_cliente(self):
    ventana_emergente= VentanaClientes(self)