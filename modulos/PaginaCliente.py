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

    self.texto_dni=StringVar()
    self.etiqueta_dni = tk.Label(self, text="DNI")
    self.etiqueta_dni.grid(row=1, column = 0)
    self.cuadro_dni = ttk.Entry(self, textvariable= self.texto_dni, justify=tk.RIGHT)
    self.cuadro_dni.grid(row=1, column = 1)

    self.texto_nombre=StringVar()
    self.etiqueta_nombre = tk.Label(self,  text="Nombre")
    self.etiqueta_nombre.grid(row=2, column = 0)
    self.cuadro_nombre = ttk.Entry(self, textvariable= self.texto_nombre, justify=tk.RIGHT)
    self.cuadro_nombre.grid(row=2, column = 1)

    self.texto_apellido=StringVar()
    self.etiqueta_apellido = tk.Label(self, text="Apellidos")
    self.etiqueta_apellido.grid(row=3, column = 0)
    self.cuadro_apellido = ttk.Entry(self, textvariable=self.texto_apellido, justify=tk.RIGHT)
    self.cuadro_apellido.grid(row=3, column = 1)

    self.texto_direccion=StringVar()
    self.etiqueta_direccion = tk.Label(self, text="Direccion")
    self.etiqueta_direccion.grid(row=4, column = 0)
    self.cuadro_direccion = ttk.Entry(self, textvariable=self.texto_direccion, justify=tk.RIGHT)
    self.cuadro_direccion.grid(row=4, column = 1)

    self.texto_municipio=StringVar()
    self.etiqueta_municipio = tk.Label(self, text="Municipio")
    self.etiqueta_municipio.grid(row=5, column = 0)
    self.cuadro_municipio = ttk.Entry(self, textvariable=self.texto_municipio, justify=tk.RIGHT)
    self.cuadro_municipio.grid(row=5, column = 1)

    self.texto_provincia=StringVar()
    self.etiqueta_provincia = tk.Label(self, text="Provincia")
    self.etiqueta_provincia.grid(row=6, column = 0)
    self.cuadro_provincia = ttk.Entry(self, textvariable=self.texto_provincia, justify=tk.RIGHT)
    self.cuadro_provincia.grid(row=6, column = 1)

    self.texto_cp=StringVar()
    self.etiqueta_cp = tk.Label(self, text="Código postal")
    self.etiqueta_cp.grid(row=7, column = 0)
    self.cuadro_cp = ttk.Entry(self, textvariable=self.texto_cp, justify=tk.RIGHT)
    self.cuadro_cp.grid(row=7, column = 1)

    self.texto_telefono=StringVar()
    self.etiqueta_telefono = tk.Label(self, text="Telefono")
    self.etiqueta_telefono.grid(row=8, column = 0)
    self.cuadro_telefono = ttk.Entry(self, textvariable =self.texto_telefono, justify=tk.RIGHT)
    self.cuadro_telefono.grid(row=8, column = 1)

    self.texto_email=StringVar()
    self.etiqueta_email = tk.Label(self, text="Email")
    self.etiqueta_email.grid(row=9, column = 0)
    self.cuadro_email = ttk.Entry(self, textvariable = self.texto_email, justify=tk.RIGHT)
    self.cuadro_email.grid(row=9, column = 1)

    self.caja_clientes=tk.Listbox(self, height =10, width=35)
    self.caja_clientes.grid(row=10, column=0, rowspan=10, columnspan = 2)
    self.scroll=tk.Scrollbar(self)
    self.scroll.grid(row=10, column=2, rowspan=10)
    self.caja_clientes.configure(yscrollcommand=self.scroll.set)
    self.scroll.configure(command=self.caja_clientes.yview)
    self.caja_clientes.bind('<<ListboxSelect>>',self.coger_filas_seleccionadas)

    
    



    #pie
  

    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button.grid(row=20, column = 0)
    button = tk.Button(self, text="Todos los clientes",
                       command=lambda: self.ver())
    button.grid(row=19, column = 0)
      
  def coger_filas_seleccionadas(self,event):
    global tupla_seleccionados
    indice=self.caja_clientes.curselection()[0]
    tupla_seleccionados=self.caja_clientes.get(indice)
    self.cuadro_dni.delete(0,END)
    self.cuadro_dni.insert(END,tupla_seleccionados[1])

    self.cuadro_nombre.delete(0,END)
    self.cuadro_nombre.insert(END,tupla_seleccionados[2])

  def ver(self):
    self.caja_clientes.delete(0, END)
    for fila in leerTodo("CLIENTE"):
        self.caja_clientes.insert(END,fila)

