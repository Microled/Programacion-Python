# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:43:14 2018

@author: Luis
"""

#!/usr/bin/python
from tkinter import *
import socket
def escaneo():
	ipurl=ipx.get()
	rangoini=primerango.get()
	scanner = socket.socket()
	try:
		scanner.connect( (ipurl, rangoini))
		xd=Label(root, text="Puerto %s : Abierto " % rangoini)
		web=Label(root, text="IP: %s  " % ipurl)
		web.grid(row=5, column=1)
		xd.grid(row=4, column=1)
	except:
		xds=Label(root, text="Puerto %s  : Cerrado" % rangoini)
		webx=Label(root, text="IP: %s  " % ipurl)
		webx.grid(row=5, column=1)
		xds.grid(row=4, column=1)
		scanner.close()
 
root = Tk()
root.title("Escaner")
ipx=StringVar()
primerango=IntVar()
labelinicio=Label(root, text="Puerto:")
labelip=Label(root, text="IP:")
buttonscan=Button(root, text="Verificar", command=escaneo)
rangoinicio=Entry(root, textvariable=primerango)
ip=Entry(root, textvariable=ipx)
labelinicio.grid(row=0)
rangoinicio.grid(row=0, column=1)
labelip.grid(row=2)
ip.grid(row=2, column=1)
buttonscan.grid(row=3, column=1)
root.mainloop()
 