#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Construido siguiendo:
#videotutoriale de píldorasinformáticas: https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS
#blog https://python-para-impacientes.blogspot.com/
#     exportar a excel https://es.stackoverflow.com/questions/36060/pasar-los-datos-de-una-lista-a-una-hoja-de-c%C3%A1lculo-mediante-dos-celdas-de-la-ho
#      ayudas sql query varias tablas a la vez https://www.campusmvp.es/recursos/post/Fundamentos-de-SQL-Consultas-SELECT-multi-tabla-JOIN.aspx
#módulos utilizados
import tkinter as tk
import os
from modulos.BACKEND import creacion_db
from tkinter import font as tkfont
from modulos.graficos.PaginaCliente import PaginaCliente
from modulos.graficos.PaginaFactura import PaginaFactura
from modulos.graficos.PaginaInicial import PaginaInicial
from modulos.graficos.PaginaResumen import PaginaResumen
from modulos.import_export import cuatroDigitar


class Aplicacion(tk.Tk):
  """Clase principal que llevará la aplicación, se encarga de cargar las páginas,
  crea las páginas a visualizar y decide cual mostrar.
  - Incluye variables comunes a todas las ventanas.
    Métodos incluidos:
    mostra_marco (self, nombre_pagina): Muestra "nombre_pagina" como página principal.
    """

  def __init__(self, *args, **kwargs):
    creacion_db()
    tk.Tk.__init__(self, *args, **kwargs)#inicio
    #setup para exportar las facturas y los excels
    #lo que ponga aquí lo podré llevar al resto de las páginas mediante controlador.loquesea
    ruta_programa = os.path.abspath(os.path.dirname(__file__))
    carpeta = "facturas"
    self.añoFactura="20"
    self.ruta=os.path.join(ruta_programa,carpeta)
    self.nombreClinica='Elisa Isabel García López'
    self.fuente_titulo = tkfont.Font(
        family='Helvetica', size=18, weight="bold", slant="italic")
    self.geometry('1200x800') 
    self.title(f'Programa de facturación. Clinica {self.nombreClinica}')
    # the container is where we'll stack a bunch of frames
    # on top of each other, then the one we want visible
    # will be raised above the others
    contenedor = tk.Frame(self)
    contenedor.pack(side="top", fill="both", expand=True)
    contenedor.grid_rowconfigure(0, weight=1)
    contenedor.grid_columnconfigure(0, weight=1)

    self.marcos = {}
    for M in ( PaginaInicial, PaginaCliente, PaginaFactura, PaginaResumen):
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
