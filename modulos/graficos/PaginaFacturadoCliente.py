



self.caja_facturas=tk.Listbox(self, height =10, width=35)
    self.caja_facturas.grid(row=2, column=2, rowspan=10, columnspan = 2)
    self.scroll_facturas=tk.Scrollbar(self)
    self.scrolll_facturas.grid(row=2, column=2, rowspan=10)
    self.caja_facturas.configure(yscrollcommand=self.scroll.set)
    self.scroll.configure(command=self.caja_facturas.yview)
    self.caja_clientes.bind('<<ListboxSelect>>',self.coger_facturas_seleccionadas)