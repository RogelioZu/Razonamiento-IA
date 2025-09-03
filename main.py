from tkinter import *
import HaciaAdelante as A
import HaciaAtras as AS

class Gui:
    def __init__(self):
        self.bc = []
        self.meta = ""
        mainWindow = Tk()
        mainWindow.title("Razonamiento IA")
        label = Label(mainWindow, text = "Escriba de 2 a 3 elementos para la base de conocimiento: ").pack()

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

        resultsWindow = Toplevel()
        bcLabel = Label(resultsWindow, text=f"Base de conocimiento: {self.bc}").pack()
        metaLabel = Label(resultsWindow, text=f"meta: {self.meta}").pack()

Gui()

#adelante = A.HaciaAdelante(meta,bc)
#adelante.proceso()

atras = AS.HaciaAtras(self.meta,self.bc)
atras.proceso()