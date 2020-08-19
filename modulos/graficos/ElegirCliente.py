from modulos.modulos_importados import *
from modulos.CRUD import *
from tkinter import *


class VentanaClientes(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Tk.__init__(self, padre)
    self.controlador =  controlador
 