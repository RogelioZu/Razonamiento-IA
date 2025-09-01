from tkinter import *
import HaciaAdelante as A
import HaciaAtras as AS

window = Tk()
label = Label(window, text = "Escriba 2 elementos para la base de conocimiento: ")
textField1 = Text(height=1, width=20)
textField2 = Text(height=1, width=20)
textField3 = Text(height=1, width=20)
button = Button(window, text = "procesar")
label.pack()
textField1.pack()
textField2.pack()
textField3.pack()
button.pack()

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