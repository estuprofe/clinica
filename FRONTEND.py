from BACKEND import *
from tkinter import *

class Aplicacion(Frame):
	def prueba(self):
		self.prueba["text"]="Funciona el botón"
		print("funcionando")

	def paginaClientes(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "Salir"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.QUIT

		self.QUIT.pack({"side": "left"})

		self.prueba= Button(self)
		self.prueba["text"] = "Botón de prueba"
		self.prueba["command"] = self.prueba

		self.prueba.pack({"side" : "left"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.paginaClientes()

raiz = Tk()
print("a ver que pasa")
app=Aplicacion(master=raiz)
app.mainloop()
raiz.destroy()

