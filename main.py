from tkinter import *
import HaciaAdelante as A
import HaciaAtras as AS

window = Tk()
label = Label(window, text = "Escriba 2 elementos para la base de conocimiento: ").pack()
textField1 = Text(height=1, width=20).pack()
textField2 = Text(height=1, width=20).pack()
textField3 = Text(height=1, width=20).pack()
label2 = Label(window, text="Escriba la meta:").pack()
metaTextField = Text(height=1, width=20).pack()
procesarBtn = Button(window, text = "procesar").pack()

window.mainloop()

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