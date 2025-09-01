from tkinter import *
import HaciaAdelante as A
import HaciaAtras as AS

class Gui:
    def __init__(self):
        self.bc = []
        self.meta = ""
        mainWindow = Tk()
        label = Label(mainWindow, text = "Escriba 2 elementos para la base de conocimiento: ").pack()

        self.entry1 = Entry(mainWindow)
        self.entry2 = Entry(mainWindow)
        self.entry3 = Entry(mainWindow)
        self.entries = [self.entry1, self.entry2, self.entry3]

        for entry in self.entries:
            entry.pack()

        label2 = Label(mainWindow, text="Escriba la meta:").pack()
        self.metaTextField = Entry(mainWindow)
        self.metaTextField.pack()
        procesarBtn = Button(mainWindow, text = "procesar", command=self.procesar).pack()


        mainWindow.mainloop()

    def procesar(self):
        print("procesar presionado")

        for entry in self.entries:
            if entry.get() == "":
                break
            else:
                self.bc.append(entry.get())

        self.meta = self.metaTextField.get()
        print(f"Base de conocimiento {self.bc}")
        print(f"meta: {self.meta}")

Gui()

#adelante = A.HaciaAdelante(meta,bc)
#adelante.proceso()

atras = AS.HaciaAtras(meta,bc)
atras.proceso()