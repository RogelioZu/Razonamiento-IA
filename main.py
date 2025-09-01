from tkinter import *
import HaciaAdelante as A
import HaciaAtras as AS

class Gui:
    def __init__(self):
        mainWindow = Tk()
        label = Label(mainWindow, text = "Escriba 2 elementos para la base de conocimiento: ").pack()

        entry1 = Entry(mainWindow).pack()
        entry2 = Entry(mainWindow).pack()
        entry3 = Entry(mainWindow).pack()
        entries = [entry1, entry2, entry3]

        label2 = Label(mainWindow, text="Escriba la meta:").pack()
        metaTextField = Entry(mainWindow).pack()
        procesarBtn = Button(mainWindow, text = "procesar", command=self.procesar).pack()


        mainWindow.mainloop()

    def procesar(self):
        print("procesar presionado")

Gui()

bc = []


bc.append(input())
bc.append(input())

print("Introduzca la meta: ")
meta = input()

print(f"Base de conocimiento {bc}")
print("meta: " + meta)


#adelante = A.HaciaAdelante(meta,bc)
#adelante.proceso()

atras = AS.HaciaAtras(meta,bc)
atras.proceso()