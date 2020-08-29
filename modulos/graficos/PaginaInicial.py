from modulos.modulos_importados import *
    
nombreClinica='Elisa Isabel García López'

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
                        command = lambda: controlador.mostrar_marco("PaginaFactura"))

    button3 = tk.Button(self, text="Resumen",
                        command=lambda: controlador.mostrar_marco("PaginaResumen"))
    button1.pack()
    button2.pack()
    button3.pack()