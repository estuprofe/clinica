from modulos.modulos_importados import *

class PaginaFactura(tk.Frame):

  def __init__(self, padre,  controlador):
    tk.Frame.__init__(self, padre)
    self.controlador =  controlador
    label = tk.Label(self, text="Facturas", font=controlador.fuente_titulo)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(self, text="Ir al principio",
                       command=lambda:  controlador.mostrar_marco("PaginaInicial"))
    button.pack()
