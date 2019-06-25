from tkinter import*
from math import*


ventana=Tk()
ventana.title("Calculadora")
ventana.configure(background="green")
ventana.geometry("392x600")
fondo = PhotoImage(file="descarga.gif")
label1 =Label(ventana, image=fondo).place(x=86, y=0)
buttom_height=3
buttom_width=11


def botonclik(num):
    global operador
    operador=operador+str(num)
    entrada_texto.set(operador)
    
def clear():
    global operador
    operador=("")
    entrada_texto.set("0")
    
def operacion():
    global operador
    try:
        opera=str(eval(operador))
    except:
        clear()
        opera("ERROR")
    entrada_texto.set(opera)
    


entrada_texto=StringVar()
operador=""
clear()

boton0 = Button(ventana, text="0",bg="yellow3", width=buttom_width, height=buttom_height, command=lambda:botonclik(0)).place(x=17, y=190)
boton1 = Button(ventana, text="1",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(1)).place(x=107, y=190)
boton2 = Button(ventana, text="2",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(2)).place(x=197, y=190)
boton3 = Button(ventana, text="3",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(3)).place(x=287, y=190)
boton4 = Button(ventana, text="4",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(4)).place(x=17, y=250)
boton5 = Button(ventana, text="5",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(5)).place(x=107, y=250)
boton6 = Button(ventana, text="6",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(6)).place(x=197, y=250)
boton7 = Button(ventana, text="7",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(7)).place(x=287, y=250)
boton8 = Button(ventana, text="8",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(8)).place(x=17, y=310)
boton9 = Button(ventana, text="9",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(9)).place(x=107, y=310)
boton0 = Button(ventana, text="PI",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("pi")).place(x=197, y=310)
boton0 = Button(ventana, text=".",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(".")).place(x=287, y=310)
boton0 = Button(ventana, text="+",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("+")).place(x=17, y=370)
boton0 = Button(ventana, text="-",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("-")).place(x=107, y=370)
boton0 = Button(ventana, text="*",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("*")).place(x=197, y=370)
boton0 = Button(ventana, text="/",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("/")).place(x=287, y=370)
boton0 = Button(ventana, text="Raiz",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("sqrt")).place(x=17, y=430)
boton0 = Button(ventana, text="C",bg="yellow3",width=buttom_width, height=buttom_height, command=clear).place(x=107, y=430)
boton0 = Button(ventana, text="EXP",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("**")).place(x=197, y=430)
boton0 = Button(ventana, text="=",bg="yellow3",width=buttom_width, height=buttom_height, command=operacion).place(x=287, y=430)
boton0 = Button(ventana, text="(",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("(")).place(x=17, y=490)
boton0 = Button(ventana, text=")",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik(")")).place(x=107, y=490)
boton0 = Button(ventana, text="%",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("%")).place(x=197, y=490)
boton0 = Button(ventana, text="In",bg="yellow3",width=buttom_width, height=buttom_height, command=lambda:botonclik("log")).place(x=287, y=490)

entrada = Entry(ventana, font=("arial",20, "bold"),textvariable=entrada_texto, width=23, bd=5, insertwidth=5, bg="powder blue", justify="right").place(x=15,y=80)

e1 = Label(ventana,text="FRANCISCO CASTILLO ITTJ",font=("arial",8,"bold"), width=54,height=2, bg="white", fg="black").place(x=5,y=560)


ventana.mainloop()
 
        
    