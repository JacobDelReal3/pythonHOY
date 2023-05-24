from tkinter import *
ventana = Tk()
ventana.title("Calculadora pedos tristes")
ventana.configure(background= "DodgerBlue2")
#Entrada
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row= 0, column = 0, columnspan = 5, padx = 5, pady = 5)

i = 0

#Funciones
def click_boton(valor):
	global i 
	e_texto.insert(i, valor)
	i += 1

#Botones
boton1 = Button(ventana, text = "1", width = 5, bg= "deepskyblue2", height = 2,command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, bg= "deepskyblue2", height = 2,command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, bg= "deepskyblue2",height = 2,command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 16,bg= "deepskyblue2",height = 2,command = lambda: click_boton(0))

a    = Button(ventana, text = "<--",bg= "turquoise3", width = 5, height = 2,command = lambda: click_boton("a"))
MC   = Button(ventana, text = "MC" ,bg= "turquoise3", width = 5, height = 2,command = lambda: borrar())
c    = Button(ventana, text = "C"  ,bg= "turquoise3", width = 5, height = 2,command = lambda: click_boton("c"))
d    = Button(ventana, text = "±"  ,bg= "turquoise3", width = 5, height = 2,command = lambda: click_boton("d"))
e    = Button(ventana, text = "√"  ,bg= "turquoise3", width = 5, height = 2,command = lambda: raiz())

def raiz():
	ecuacion1 = e_texto.get()
	resultado1 = eval(ecuacion1)
	resultado2 = resultado1** (0.5)
	e_texto.delete(0, END)
	e_texto.insert(0,resultado2)
	i = 0

MR = Button(ventana, text = "MR" ,bg= "turquoise3", width = 5, height = 2,command = lambda: MR1())
Mmas = Button(ventana, text = "M+" ,bg= "turquoise3", width = 5, height = 2,command = lambda: MMAS())


g    = Button(ventana, text = "%"  ,bg= "turquoise2", width = 5, height = 2,command = lambda: porciento())

def porciento():
	ecuacion1 = e_texto.get()
	resultado1 = eval(ecuacion1)
	resultado2 = resultado1*0.01
	e_texto.delete(0, END)
	e_texto.insert(0,resultado2)
	i = 0

h    = Button(ventana, text = "1/x", width = 5,bg= "turquoise3", height = 2,command = lambda: unoentrex())

def unoentrex():
	ecuacion1 = e_texto.get()
	resultado1 = eval(ecuacion1)
	resultado2 = 1/resultado1
	e_texto.delete(0, END)
	e_texto.insert(0,resultado2)
	i = 0

sqr  = Button(ventana, text = "sqr", width = 5,bg= "turquoise3", height = 2,command = lambda: click_boton("sqr"))


MS = Button(ventana, text = "MS" , width = 5,bg= "turquoise3", height = 2,command = lambda: click_boton(")"))
decimal     = Button(ventana, text = "." ,bg= "turquoise3", width = 5, height = 2,command = lambda: click_boton("."))
borrar1     = Button(ventana, text = "CE",bg= "turquoise3", width = 5, height = 2,command = lambda: borrar())

def borrar():
	e_texto.delete(0, END)
	i = 0 

suma  = Button(ventana, text = "+", bg= "turquoise1", width = 5, height = 2,command = lambda: click_boton("+"))
resta = Button(ventana, text = "-", bg= "turquoise1",width = 5, height = 2,command = lambda: click_boton("-"))
multi = Button(ventana, text = "*", bg= "turquoise1",width = 5, height = 2,command = lambda: click_boton("*"))
divi  = Button(ventana, text = "÷", bg= "turquoise1",width = 5, height = 2,command = lambda: click_boton("/"))
igual = Button(ventana, text = "=", bg= "turquoise1",width = 5, height = 6,command = lambda: operacion())

def operacion():
	ecuacion = e_texto.get()
	resultado = eval(ecuacion)
	e_texto.delete(0 , END)
	e_texto.insert(0, resultado)
	i = 0

# acomodar botones
MC.grid(         row=1, column=0, padx=5, pady=5)
MR.grid(row=1, column=1, padx=5, pady=5) 
MS.grid(row=1, column=2, padx=5, pady=5) 
Mmas.grid(       row=1, column=3, padx=5, pady=5)
sqr.grid(        row=1, column=4, padx=5, pady=5)

a.grid(row=2, column=0, padx=5, pady=5)
borrar1.grid(row=2, column=1, padx=5, pady=5) 
c.grid(row=2, column=2, padx=5, pady=5)
d.grid(row=2, column=3, padx=5, pady=5)
e.grid(row=2, column=4, padx=5, pady=5)


boton7.grid(row=3, column=0, padx=5, pady=5)
boton8.grid(row=3, column=1, padx=5, pady=5)
boton9.grid(row=3, column=2, padx=5, pady=5)
divi.grid(row=3, column=3, padx=5, pady=5)
g.grid(row=3, column=4, padx=5, pady=5)


boton4.grid(row=4, column=0, padx=5, pady=5)
boton5.grid(row=4, column=1, padx=5, pady=5)
boton6.grid(row=4, column=2, padx=5, pady=5)
multi.grid( row=4, column=3, padx=5, pady=5)
h.grid(row=4, column=4, padx=5, pady=5)

boton1.grid(row=5, column=0, padx=5, pady=5)
boton2.grid(row=5, column=1, padx=5, pady=5)
boton3.grid(row=5, column=2, padx=5, pady=5)
resta.grid( row=5, column=3, padx=5, pady=5)
igual.grid( row=5, column=4, padx=5, rowspan=5, pady=5)

boton0.grid( row=6, column=0, columnspan=2, padx=5, pady=5)
decimal.grid(row=6, column=2, padx=5, pady=5)
suma.grid(   row=6, column=3, padx=5, pady=5)




ventana.mainloop()