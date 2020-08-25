from modulos.modulos_importados import *
from modulos.CRUD import *




class PaginaCliente(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    
    self.controlador =  controlador
    #título
    self.label = tk.Label(self, text="Clientes", font=self.controlador.fuente_titulo)
    self.label.grid(column=0, row=0)
    
    #cuerpo

    self.texto_id=StringVar()
    self.etiqueta_id = tk.Label(self, text="ID")
    self.etiqueta_id.grid(row=1, column = 0)
    self.cuadro_id = ttk.Entry(self, textvariable= self.texto_id, justify=tk.RIGHT)
    self.cuadro_id.grid(row=1, column = 1)

    self.texto_dni=StringVar()
    self.etiqueta_dni = tk.Label(self, text="DNI")
    self.etiqueta_dni.grid(row=2, column = 0)
    self.cuadro_dni = ttk.Entry(self, textvariable= self.texto_dni, justify=tk.RIGHT)
    self.cuadro_dni.grid(row=2, column = 1)

    self.texto_nombre=StringVar()
    self.etiqueta_nombre = tk.Label(self,  text="Nombre")
    self.etiqueta_nombre.grid(row=3, column = 0)
    self.cuadro_nombre = ttk.Entry(self, textvariable= self.texto_nombre, justify=tk.RIGHT)
    self.cuadro_nombre.grid(row=3, column = 1)

    self.texto_apellido=StringVar()
    self.etiqueta_apellido = tk.Label(self, text="Apellidos")
    self.etiqueta_apellido.grid(row=4, column = 0)
    self.cuadro_apellido = ttk.Entry(self, textvariable=self.texto_apellido, justify=tk.RIGHT)
    self.cuadro_apellido.grid(row=4, column = 1)

    self.texto_direccion=StringVar()
    self.etiqueta_direccion = tk.Label(self, text="Direccion")
    self.etiqueta_direccion.grid(row=5, column = 0)
    self.cuadro_direccion = ttk.Entry(self, textvariable=self.texto_direccion, justify=tk.RIGHT)
    self.cuadro_direccion.grid(row=5, column = 1)

    self.texto_municipio=StringVar()
    self.etiqueta_municipio = tk.Label(self, text="Municipio")
    self.etiqueta_municipio.grid(row=6, column = 0)
    self.cuadro_municipio = ttk.Entry(self, textvariable=self.texto_municipio, justify=tk.RIGHT)
    self.cuadro_municipio.grid(row=6, column = 1)

    self.texto_provincia=StringVar()
    self.etiqueta_provincia = tk.Label(self, text="Provincia")
    self.etiqueta_provincia.grid(row=7, column = 0)
    self.cuadro_provincia = ttk.Entry(self, textvariable=self.texto_provincia, justify=tk.RIGHT)
    self.cuadro_provincia.grid(row=7, column = 1)

    self.texto_cp=StringVar()
    self.etiqueta_cp = tk.Label(self, text="Código postal")
    self.etiqueta_cp.grid(row=8, column = 0)
    self.cuadro_cp = ttk.Entry(self, textvariable=self.texto_cp, justify=tk.RIGHT)
    self.cuadro_cp.grid(row=8, column = 1)

    self.texto_telefono=StringVar()
    self.etiqueta_telefono = tk.Label(self, text="Telefono")
    self.etiqueta_telefono.grid(row=9, column = 0)
    self.cuadro_telefono = ttk.Entry(self, textvariable =self.texto_telefono, justify=tk.RIGHT)
    self.cuadro_telefono.grid(row=9, column = 1)

    self.texto_email=StringVar()
    self.etiqueta_email = tk.Label(self, text="Email")
    self.etiqueta_email.grid(row=10, column = 0)
    self.cuadro_email = ttk.Entry(self, textvariable = self.texto_email, justify=tk.RIGHT)
    self.cuadro_email.grid(row=10, column = 1)

    self.caja_clientes=tk.Listbox(self, height =10, width=35)
    self.caja_clientes.grid(row=4, column=3, rowspan=9, columnspan = 2)
    self.scroll=tk.Scrollbar(self)
    self.scroll.grid(row=4, column=5, rowspan=9)
    self.caja_clientes.configure(yscrollcommand=self.scroll.set)
    self.scroll.configure(command=self.caja_clientes.yview)
    self.caja_clientes.bind('<<ListboxSelect>>',self.escribir_campos)
    self.ver()



    #Botones
    boton_inicio = tk.Button(self, text="INICIO",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    boton_inicio.grid(row=0, column = 1)

    boton_inicio = tk.Button(self, text="FACTURA",
                       command=lambda:  controlador.mostrar_marco("PaginaFactura"))
    boton_inicio.grid(row=0, column = 2)
  

   

    boton_actualizar = tk.Button(self, text="actualizar clientes",
                       command=lambda: self.editar())
    boton_actualizar.grid(row=21, column = 1)

    boton_borrar = tk.Button(self, text="Borrar cuadros",
                       command=lambda: self.borrar())

    boton_borrar.grid(row=22, column = 0)



    boton_ver_clientes = tk.Button(self, text="Ver clientes",
                               command=lambda: self.ver())
    boton_ver_clientes.grid(row=21, column = 0)

     
           

    boton_eliminar = tk.Button(self, text="Eliminar cliente",
                               command=lambda: self.eliminar())
    boton_eliminar.grid(row=22, column = 1)


    boton_añadir = tk.Button(self, text="Añadir cliente",
                       command=lambda: self.añadir())
    boton_añadir.grid(row=24, column = 0, columnspan=3)
        
    # iniciar el cuadro con los clientes
    




  def escribir_campos(self, event):
    
    
    global tupla_seleccionados
    global id_seleccionado
    indice = self.caja_clientes.curselection()[0]
    print (self.caja_clientes.curselection())

    tupla_seleccionados=self.caja_clientes.get(indice)
    self.controlador.marcos['PaginaFactura'].set_cliente(tupla_seleccionados)


    id_seleccionado=tupla_seleccionados[0]

    self.cuadro_id.delete(0,END)
    self.cuadro_id.insert(END,tupla_seleccionados[0])

    self.cuadro_dni.delete(0,END)
    self.cuadro_dni.insert(END,tupla_seleccionados[1])

    self.cuadro_nombre.delete(0,END)
    self.cuadro_nombre.insert(END,tupla_seleccionados[2])

    self.cuadro_apellido.delete(0,END)
    self.cuadro_apellido.insert(END,tupla_seleccionados[3])

    self.cuadro_direccion.delete(0,END)
    self.cuadro_direccion.insert(END,tupla_seleccionados[4])

    self.cuadro_municipio.delete(0,END)
    self.cuadro_municipio.insert(END,tupla_seleccionados[5])

    self.cuadro_provincia.delete(0,END)
    self.cuadro_provincia.insert(END,tupla_seleccionados[6])

    self.cuadro_cp.delete(0,END)
    self.cuadro_cp.insert(END,tupla_seleccionados[7])

    self.cuadro_telefono.delete(0,END)
    self.cuadro_telefono.insert(END,tupla_seleccionados[8])

    self.cuadro_email.delete(0,END)
    self.cuadro_email.insert(END,tupla_seleccionados[9])

      
  def boton_elegir_pulsado(self,event):#Reinicia los cuadros con la información extraída de clientes
    

    seleccionado_ventana = VentanaClientes()
    
  def ver(self):
    self.caja_clientes.delete(0, END)
    for fila in leerTodo("CLIENTE"):
            self.caja_clientes.insert(END,fila)

        

  def eliminar(self):
    borrarRegistro("CLIENTE", "CLIENTE_ID", id_seleccionado)
    self.ver()  



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




  def añadir(self):
    datos = [(self.cuadro_dni.get(), self.cuadro_nombre.get(), self.cuadro_apellido.get(), self.cuadro_direccion.get(),
              self.cuadro_municipio.get(), self.cuadro_provincia.get(), self.cuadro_cp.get(), self.cuadro_telefono.get(), self.cuadro_email.get())]
    #print(datos)
    crearCliente(datos)
    self.ver()
