from tkinter import ttk
import tkinter as tk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        
        self.combo = ttk.Combobox(self)
        self.combo.place(x=50, y=50)
        self.combo["values"] =  ["0", "4", "16", "21"]
        self.combo.bind("<<ComboboxSelected>>", self.selecction_changed)

        self.etiqueta_iva = tk.Label(self, text="IVA")
        self.etiqueta_iva.grid(row=140, column = 0)
        self.combo_iva = ttk.Combobox(self)
        self.combo_iva["values"] = ["Juri", "Puri", "16", "21"] #TODO- hacer que lo coja de la base de datos
        self.combo_iva.bind("<<ComboboxSelected>>", self.selecction_changed)
        self.combo_iva.grid(row=140, column = 1)
        
        main_window.configure(width=300, height=200)
        self.place(width=300, height=200)

    def selecction_changed(self, event):
        print("Nuevo elemento seleccionado:", self.combo_iva.get())
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()