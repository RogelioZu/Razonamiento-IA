from tkinter import *
import io
import sys
import HaciaAdelante as A
import HaciaAtras as AS

class Gui:
    def __init__(self):
        self.bc = []
        self.meta = ""
        mainWindow = Tk()
        mainWindow.title("Razonamiento IA")
        Label(mainWindow, text="Escriba de 2 a 3 elementos para la base de conocimiento: ").pack()

        self.entry1 = Entry(mainWindow)
        self.entry2 = Entry(mainWindow)
        self.entry3 = Entry(mainWindow)
        self.entries = [self.entry1, self.entry2, self.entry3]
        for entry in self.entries:
            entry.pack()

        Label(mainWindow, text="Escriba la meta:").pack()
        self.metaTextField = Entry(mainWindow)
        self.metaTextField.pack()
        Button(mainWindow, text="procesar", command=self.procesar).pack()

        mainWindow.mainloop()

    def procesar(self):
        self.bc = []
        for entry in self.entries:
            if entry.get():
                self.bc.append(entry.get())

        self.meta = self.metaTextField.get()

        #Salida de HaciaAdelante
        adelante_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = adelante_output
        adelante = A.HaciaAdelante(self.meta, self.bc.copy())
        adelante.proceso()
        sys.stdout = sys_stdout
        adelante_text = adelante_output.getvalue()

        # Salida de HaciaAtras
        atras_output = io.StringIO()
        sys.stdout = atras_output
        atras = AS.HaciaAtras(self.meta, self.bc.copy())
        atras.proceso()
        sys.stdout = sys_stdout
        atras_text = atras_output.getvalue()

        # Crear ventana de resultados
        resultsWindow = Toplevel()
        resultsWindow.title("Resultados")

        Label(resultsWindow, text=f"Base de conocimiento: {self.bc}").pack()
        Label(resultsWindow, text=f"Meta: {self.meta}").pack()

        frame = Frame(resultsWindow)
        frame.pack(fill=BOTH, expand=True)

        # Panel para HaciaAdelante
        adelante_panel = Text(frame, wrap=WORD, width=50)
        adelante_panel.insert(END, adelante_text)
        adelante_panel.config(state=DISABLED)
        adelante_panel.pack(side=LEFT, fill=BOTH, expand=True)

        # Panel para HaciaAtras
        atras_panel = Text(frame, wrap=WORD, width=50)
        atras_panel.insert(END, atras_text)
        atras_panel.config(state=DISABLED)
        atras_panel.pack(side=LEFT, fill=BOTH, expand=True)

Gui()