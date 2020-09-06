from modulos.modulos_importados import *
    


class PaginaInicial(tk.Frame):

  def __init__(self, padre, controlador):
    tk.Frame.__init__(self, padre)
    self.controlador = controlador
    self.label = tk.Label(self, text=f"Programa de facturación. Clinica {controlador.nombreClinica}",
                     font=controlador.fuente_titulo)
    self.label.pack(side="top", fill="x", pady=10)

    self.button1 = tk.Button(self, text="Clientes",
                        command=lambda: controlador.mostrar_marco("PaginaCliente"))
    self.button2 = tk.Button(self, text="Facturas",
                        command = lambda: controlador.mostrar_marco("PaginaFactura"))

    self.button3 = tk.Button(self, text="Resumen",
                        command=lambda: controlador.mostrar_marco("PaginaResumen"))

    self.label_configuracion = tk.Label(self, text="Configuración del código automático de las facturas", font=controlador.fuente_titulo)

    self.texto_letra=StringVar()
    self.etiqueta_letra = tk.Label(self, text="Letra") 
    self.cuadro_letra = ttk.Entry(self, textvariable= self.texto_letra, justify=tk.RIGHT)
    self.cuadro_letra.delete(0,END)
    self.cuadro_letra.insert(END, "A")

    self.texto_año=StringVar()
    self.etiqueta_año = tk.Label(self, text="Año") 
    self.cuadro_año = ttk.Entry(self, textvariable= self.texto_año, justify=tk.RIGHT)
    self.cuadro_año.delete(0,END)
    self.cuadro_año.insert(END, "20")

    print("Pasa por aquí")

    self.texto_numero=StringVar()
    self.etiqueta_numero = tk.Label(self, text="Numero") 
    self.cuadro_numero = ttk.Entry(self, textvariable= self.texto_numero, justify=tk.RIGHT)
    self.cuadro_numero.delete(0,END)
    try:
        self.cuadro_numero.insert(END, cuatroDigitar(leerTodo("FACTURA")[-1][0]+1))
    except IndexError:
        self.cuadro_numero.insert(END, cuatroDigitar(1))



    #print (cuatroDigitar(leerTodo("FACTURA")[-1][0]+1))

    self.texto_resultado=StringVar()   
    self.etiqueta_resultado = tk.Label(self, text="resultado") 
    self.cuadro_resultado = ttk.Entry(self, textvariable= self.texto_resultado, justify=tk.RIGHT)
    self.button4 = tk.Button(self, text="Actualizar Numeración",
                        command= self.actualizar)

    self.etiqueta_fecha_inicio = tk.Label(self, text="Fecha inicial para el EXCEL")
    self.cal_inicio = DateEntry(self, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='es_ES')
    self.cal_inicio.set_date(datetime(2020,7,1))

    self.etiqueta_fecha_final = tk.Label(self, text="Fecha final para el EXCEL")
    self.cal_fin = DateEntry(self, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='es_ES')
    self.cal_fin.set_date(datetime(2020,9,30))
    

   
    self.button1.pack()
    self.button2.pack()
    self.button3.pack()
    self.label_configuracion.pack()
    self.etiqueta_letra.pack()
    self.cuadro_letra.pack()
    self.etiqueta_año.pack()
    self.cuadro_año.pack()
    self.etiqueta_numero.pack()
    self.cuadro_numero.pack()
    self.etiqueta_resultado.pack()
    self.cuadro_resultado.pack()
    self.button4.pack()
    self.etiqueta_fecha_inicio.pack()
    self.cal_inicio.pack()
    self.etiqueta_fecha_final.pack()
    self.cal_fin.pack()

  def actualizar(self):
    self.cuadro_resultado.delete(0,END)
    self.cuadro_resultado.insert(END, self.cuadro_letra.get())
    self.cuadro_resultado.insert(END, self.cuadro_año.get())
    self.cuadro_resultado.insert(END, cuatroDigitar(int(self.cuadro_numero.get())))
    self.controlador.marcos['PaginaFactura'].cuadro_codigo.delete(0,END)
    self.controlador.marcos['PaginaFactura'].cuadro_codigo.insert(END,self.cuadro_resultado.get())
    self.controlador.marcos['PaginaFactura'].set_cliente(leerTodo("CLIENTE")[0])