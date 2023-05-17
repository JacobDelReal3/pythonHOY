import tkinter as Tk
from tkinter import *

#############################################################
def suma():
    n1 = int(num.get())
    n2 = int(num2.get())
    res.set(n1+n2)
    signo.set("+")
def resta():
    n1 = int(num.get())
    n2 = int(num2.get())
    res.set(n1-n2)
    signo.set("-")
def division():
    n1 = int(num.get())
    n2 = int(num2.get())
    res.set(n1/n2)
    signo.set("/")    
def multiplicacion():
    n1 = int(num.get())
    n2 = int(num2.get())
    res.set(n1*n2)
    signo.set("*")
##########################################################    

root=Tk()
root.geometry("450x340")
root.title("Calculadora gedionda") 

num = StringVar()
num.set("0")

num2 = StringVar()
num2.set("0")

res = StringVar()
res.set("0")

signo = StringVar()
signo.set(" ")

lbl_num = LabelFrame(root, text = "Numeros", width=440, height=100, font=("Arial", 10))
lbl_num.place(x=5, y=25)

lbl_opp = LabelFrame(root, text= "Operadores aritmeticos", width= 440, height= 150, font=("Arial", 10))
lbl_opp.place(x= 5, y= 150)


#BARRAS
barra = Entry(root, textvariable=num)
barra.place(x=40, y=60, width=80, height=40)
barra.config(font=("arial", 20), fg="black")

barra2 = Entry(root, textvariable=num2)
barra2.place(x=185, y=60, width=80, height=40)
barra2.config(font=("arial", 20), fg="black")

barra3 = Entry(root, textvariable=res)
barra3.place(x=330, y=60, width=80, height=40)
barra3.config(font=("arial", 20), fg="black")

# Funciones
funcion = Button(root, text="+",command=suma)
funcion.place(x=40, y=200, width=75, height=50)
funcion.config(font=("arial", 20), fg="chocolate")

funcion = Button(root, text="-",command=resta)
funcion.place(x=120, y=200, width=75, height=50)
funcion.config(font=("arial", 20), fg="chocolate")

funcion = Button(root, text="*",command=multiplicacion)
funcion.place(x=200, y=200, width=75, height=50)
funcion.config(font=("arial", 20), fg="chocolate")

funcion = Button(root, text="/",command=division)
funcion.place(x=280, y=200, width=75, height=50)
funcion.config(font=("arial", 20), fg="chocolate")

lblsigno = Label(root, textvariable=signo)
lblsigno.place(x=120, y=60, width=40, height=50)
lblsigno.config(font=("arial", 20), fg="black")

lblmsg = Label(root, text= "=")
lblmsg.pack()
lblmsg.place(x=285, y= 60)
lblmsg.config(font=("arial", 20), fg="black")

root.mainloop()