"""
Nombre: Ventana.py
Objetivo: muestra como trabajar con ventanas gui en python y tkinter
Autor: Luis David Delgado Díaz
Fecha: 29 de julio de 2020
"""

# importar las librerias de tkinter
from tkinter import *
from tkinter import ttk

#funcion para enviar datos al servidor echo
def sendToServer():
	
	print("Enviado ...")

#funcion main
def main():
	#creamos la ventana como contenedora
	win = Tk()
	# Modicicamos parametros de la ventana win
	win .geometry("400x400")
	win.title("mi primer ventana en Python Tkinter")
	#creamos etiqueta
	label = ttk.Label(win, text"Texto a Enviar al Servidor").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)
	#creamos un boton para enviar el contenido dela propiedad
	ttk.button(win, text="enviar mensaje", command=sendToServer).pack(side=BOTTOM)
	#creamos un boton en la ventana y lo colocamos
	ttk.Button(win, text="salir", command=quit).pack(side=BOTTOM)
	#Ciclo para dibujar y esperar eventos
	win.mainloop()


#para funcion main
if__name__ == "__main__":
	main()


