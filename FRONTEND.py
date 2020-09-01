#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Construido siguiendo el blog https://python-para-impacientes.blogspot.com/
#módulos utilizados
from modulos.modulos_importados import *





# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
#setup
nombreClinica="Elisa Isabel García López"
letraFactura="A"
añoFactura="20"

ruta_programa = os.path.abspath(os.path.dirname(__file__))
print(ruta_programa)
carpeta = "facturas"
ruta_facturas = os.path.join(ruta_programa,carpeta)
print (ruta_facturas)




class Aplicacion(tk.Tk):

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    self.letraFactura=letraFactura
    self.añoFactura=añoFactura
    self.ruta=ruta_facturas
    
    self.fuente_titulo = tkfont.Font(
        family='Helvetica', size=18, weight="bold", slant="italic")
    self.geometry('800x600')
      
    self.title(f'Programa de facturación. Clinica {nombreClinica}')
    # the container is where we'll stack a bunch of frames
    # on top of each other, then the one we want visible
    # will be raised above the others
    contenedor = tk.Frame(self)
    contenedor.pack(side="top", fill="both", expand=True)
    contenedor.grid_rowconfigure(0, weight=1)
    contenedor.grid_columnconfigure(0, weight=1)

    self.marcos = {}
    for M in (PaginaInicial, PaginaCliente, PaginaFactura, PaginaResumen):
      nombre_pagina = M.__name__
      marco = M(padre=contenedor, controlador=self)
      self.marcos[nombre_pagina] = marco

      # put all of the pages in the same location;
      # the one on the top of the stacking order
      # will be the one that is visible.
      marco.grid(row=0, column=0, sticky="nsew")

    self.mostrar_marco("PaginaInicial")

  def mostrar_marco(self, nombre_pagina):
    '''Show a frame for the given page name'''
    marco = self.marcos[nombre_pagina]
    marco.tkraise()










if __name__ == "__main__":
  app = Aplicacion()
  app.mainloop()
