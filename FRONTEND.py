#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Construido siguiendo el blog https://python-para-impacientes.blogspot.com/
#módulos utilizados



from BACKEND import *
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
#setup
nombreClinica='Elisa Isabel García López'


class Aplicacion(tk.Tk):

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    self.fuente_titulo = tkfont.Font(
        family='Helvetica', size=18, weight="bold", slant="italic")
    self.geometry('800x600')
      
    self.title(f'Programa de facturación. Clinica {nombreClinica} ')
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


class PaginaInicial(tk.Frame):

  def __init__(self, padre, controlador):
    tk.Frame.__init__(self, padre)
    self.controlador = controlador
    label = tk.Label(self, text=f"Programa de facturación. Clinica {nombreClinica}",
                     font=controlador.fuente_titulo)
    label.pack(side="top", fill="x", pady=10)

    button1 = tk.Button(self, text="Clientes",
                        command=lambda: controlador.mostrar_marco("PaginaCliente"))
    button2 = tk.Button(self, text="Facturas",
                        command=lambda: controlador.mostrar_marco("PaginaFactura"))
    button3 = tk.Button(self, text="Resumen",
                        command=lambda: controlador.mostrar_marco("PaginaResumen"))
    button1.pack()
    button2.pack()
    button3.pack()

class PaginaCliente(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    #título
    label = tk.Label(self, text="Clientes", font=controlador.fuente_titulo)
    label.grid(column=0, row=0)
    #cuerpo



    #pie
    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button.grid(column=0, row=1)


class PaginaFactura(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    label = tk.Label(self, text="Facturas", font=controlador.fuente_titulo)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button.pack()

class PaginaResumen(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    label = tk.Label(self, text="Resumen de Facturas", font=controlador.fuente_titulo)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button.pack()


if __name__ == "__main__":
  app = Aplicacion()
  app.mainloop()
