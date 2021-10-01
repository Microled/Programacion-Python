from tkinter import *
class aplicacion(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.crear_widgets()

	def crear_widgets(self):
		self.boton1=Button(self,text="Mensaje")
		self.boton1.grid()


ventana = Tk()
ventana.title("Primer Botón")
ventana.geometry("300x200")

app=aplicacion(ventana)

ventana.mainloop()
