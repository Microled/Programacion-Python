from tkinter import *             # Módulo para el contenído gráfico Tkinter
from tkinter import ttk           # Módulo para el combobox
from tkinter import scrolledtext  # Módulo para el scrolledtext (tareas)
from datetime import datetime     # Módulo para importar fecha del sistema
from tkinter import filedialog    # Módulo para importar dialogo guardar y abrir archivo
import os                         # Módulo para importar el procese para abrir fichero en windows directamente
   
#############################################
# Variables Globales
#############################################
ficheroTarea=None
nomFichero=None
nomFicheroExt=None

#############################################
# Funciones
#############################################

### Funcion Crear Doc ###
#########################
def funCrearDoc():
    if campoFecha.get()!="":
        global ficheroTarea, nomFichero
        
        nomFichero=comboCliente.get()+" "+campoFecha.get()
  
        # Filedialog.asksaveasfile genera una ruta y fichero si se acepta o un contenido None (keyword) si cancelas
        ficheroTarea=filedialog.asksaveasfile(title="Seleciona el fichero a guardar", mode="w", initialfile=nomFichero, defaultextension=".txt")
            
        if ficheroTarea is not None:            # Si el contenido de ficheroTarea es diferente a None, es decir, tiene un nombre 
                                                # de fichero válido, entonces se habilitan botones y campos para trabajar  
            labelRuta.configure(text=ficheroTarea.name)
            #print(ficheroTarea)                # Impresión de Control
            #print(ficheroTarea.name)           # Impresión de control
    
            # Se habilitan los campos y botones para trabajar
            funHabilitarCampos()
            comboCliente.configure(state="disabled")
            funNombreFichero()
            labelNombreFichero.configure(text=nomFicheroExt)
            funDeshabilitarDoc()


### Función Cargar Documento ###
################################
def funCargarDoc():
    global ficheroTarea
    ficheroTarea=filedialog.askopenfile(title="Selecciona el fichero a cargar", mode="a+")
    funHabilitarCampos()
    labelRuta.configure(text=ficheroTarea.name)
    comboCliente.configure(state="disabled")
    funNombreFichero()
    labelNombreFichero.configure(text=nomFicheroExt)
    funDeshabilitarDoc()
 
### Función Mostrar Doc ###
##########################
def funMostrarDoc():
    os.startfile(ficheroTarea.name)
    
### Función Editar Cliente ###
##############################
def funEditCliente():
    #subprocess.Popen(r'explorer /select,"lista clientes.txt"')
    os.startfile("lista clientes.txt")
    funActualizarClientes()
    
### Función Actualizar Clientes ComboBox ###
#########################################
def funActualizarClientes():
    fichero=open("lista clientes.txt","r")        # Abre el fichero de solo lectura lista clientes
    listaCompleta=(fichero.read().splitlines())   # Divide el fichero en lineas y lo pone en una lista listacompleta
    listaClientes=[]                              # Crea una lista vacia listaClientes
    listaClientes=listaCompleta[5:]               # Pone en la lista listaClientes toda la listaCompleta, menos las línea iniciales
    comboCliente.configure(values=listaClientes)  # Pone el fichero listaClientescomo valores del combobox
    comboCliente.current(0)                       # Marca el quinto elemento (empieza en 0) como predeterminado

### Funcion Validar Tarea ###
#############################
def funValidarTarea():
    global ficheroTarea, nomFichero
    
    #print(txtTarea.get("1.0",END))         # Impresión de Control
    if campoTiempoTarea.get()!="":
        descripTarea=campoUser.get()+"\t"+campoTiempoTarea.get()+" min\n"+txtTarea.get("1.0",END)+"\n"
    else:
        descripTarea=campoUser.get()+"\t"+campoTiempoTarea.get()+"\n"+txtTarea.get("1.0",END)+"\n"
    ficheroTarea.write(descripTarea)
    ficheroTarea.close()
    ficheroTarea=open(ficheroTarea.name, "a+")
    funBorrarCampos()

### Funcion Cerrar Fichero ###
##############################
def funCerrarFichero():
    ficheroTarea.close()
    funDeshabilitarCampos()
    comboCliente.configure(state="normal")
    labelRuta.configure(text="SIN FICHERO")
    labelNombreFichero.configure(text="SIN FICHERO")
    botonCreaDoc.configure(state="normal")
    botonCargarDoc.configure(state="normal")


### Función Salir ###
####################
def funSalir():
    root.destroy()

### Función borrar campos ###
#############################
def funBorrarCampos():
    campoUser.delete(0,END)
    campoUser.insert(0,"Varios")
    txtTarea.delete("0.0",END)
    campoTiempoTarea.delete(0,END)

### Función Habilitar Campos ###
################################
def funHabilitarCampos():
    comboCliente.configure(state="normal")
    campoUser.configure(state="normal")
    campoUser.delete(0,END)
    campoUser.insert(0,"Varios")
    campoTiempoTarea.configure(state="normal")
    txtTarea.configure(state="normal")
    botonMostrarDoc.configure(state="normal")
    botonValidarTarea.configure(state="normal")
    botonCerrarFichero.configure(state="normal")

### Función Deshabilitar Campos ###
###################################
def funDeshabilitarCampos():
    campoUser.configure(state="disabled")
    campoTiempoTarea.configure(state="disabled")
    txtTarea.configure(state="disabled")
    botonMostrarDoc.configure(state="disabled")
    botonValidarTarea.configure(state="disabled")
    botonCerrarFichero.configure(state="disabled")

### Funcion Deshabilitar Crear y cargar Documentos #
####################################################

def funDeshabilitarDoc():
    botonCargarDoc.configure(state="disabled")
    botonCreaDoc.configure(state="disabled")

    
### Función Extraer nombre Fichero ###
######################################

def funNombreFichero():
    global ficheroTarea, nomFicheroExt
    nomFicheroExt=ficheroTarea.name.split("/")[-1]  # Extraemos nombre fichero de la ruta completa del fichero
                                                    # Pasamos la ruta a una lista separada por "/" y cojemos el último elemento
    


#############################################
# Creación Interface gráfica
#############################################

root=Tk()
# Ventana principal
root.geometry("600x450")
root.title("INSERCIÓN DE TAREAS EN CLIENTES")


# Widgets ventana principal
# Ventana principal con 6 columnas

# Primera Fila
# Fecha, Número y boton crear Doc
labelFecha=Label(root, text="Fecha:")
labelFecha.place(x=5, y=5)

campoFecha=Entry(root, justify=CENTER)
campoFecha.place(x=60, y=5)

labelNumeroFecha=Label(root, text="Nº:")
labelNumeroFecha.place(x=230, y=5)

campoNumeroFecha=Entry(root, width=5)
campoNumeroFecha.place(x=260, y=5)

labelNombreFichero=Label(root, text="SIN FICHERO")
labelNombreFichero.place(x=360,y=5)

botonCreaDoc=Button(root, text="Crear Doc", command=funCrearDoc, width=10, height=2)
botonCreaDoc.place(x=500, y=5)

# Segunda Fila
# Cliente
labelCliente=Label(root, text="Cliente:")
labelCliente.place(x=5, y=35)

comboCliente=ttk.Combobox(root, width=35)
comboCliente.place(x=60, y=35)

botonEditCliente=Button(text="Editar Clientes", command=funEditCliente)
botonEditCliente.place(x=320, y=35)

# Tercera Fila
# User y Cargar Doc
labelUser=Label(root, text="User:")
labelUser.place(x=5,y=65)

campoUser=Entry(root, width=60,state="disabled") #disabled deshabilita el widget
campoUser.place(x=60, y=65)

botonCargarDoc=Button(root, text="Cargar Doc", command=funCargarDoc, width=10, height=1)
botonCargarDoc.place(x=500, y=65)

# Cuarta Fila
# label tarea, Nº tarea, Mostrar Doc
labelTarea=Label(root,text="Descripción Tarea:")
labelTarea.place(x=5, y=95)

labelTiempoTarea=Label(root, text="Tiempo Tarea:")
labelTiempoTarea.place(x=230, y=95)

campoTiempoTarea=Entry(root, width=11,state="disabled")
campoTiempoTarea.place(x=325, y=95)

botonMostrarDoc=Button(root, text="Mostrar Doc", command=funMostrarDoc, width=10, state="disabled")
botonMostrarDoc.place(x=500, y=95)

# Quinta Fila
# Campo Texto
txtTarea=scrolledtext.ScrolledText(root, width=73, heigh=16,state="disabled")
txtTarea.place(x=5, y=125)

# Sexta Fila
# Botones Validar Tarea, Cerra Fichero y Salir

botonValidarTarea= Button(root, text="Validar Tarea",command=funValidarTarea, state="disabled")
botonValidarTarea.place(x=20, y=395)

botonCerrarFichero= Button(root, text="Cerrar Fichero",state="disabled", command=funCerrarFichero)
botonCerrarFichero.place(x=250, y=395)

botonSalir= Button(root, text="Salir", command=funSalir)
botonSalir.place(x=500, y=395)


# Septima Fila
# Nombre y ruta
labelRuta=Label(root, text="SIN FICHERO")
labelRuta.place(x=5, y=425)


#############################################
# Estado Inicial pantalla gráfica           #
#############################################
#Fecha
fechaSistema=datetime.today().strftime("%d-%m-%Y")
campoFecha.insert(0,fechaSistema)


############################################
# Actualizar lista clientes                #
############################################
#Combo Clientes
funActualizarClientes()


root.mainloop()