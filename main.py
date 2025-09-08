from tkinter import *
import io
import sys
import threading
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
        self.process_button = Button(mainWindow, text="Procesar", command=self.procesar)
        self.process_button.pack()

        mainWindow.mainloop()

    

    def _ejecutar_adelante(self, meta, bc, result_container):
        """Función objetivo para el hilo de HaciaAdelante."""
        adelante_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = adelante_output
        try:
            adelante = A.HaciaAdelante(meta, bc)
            adelante.proceso()
        finally:
            sys.stdout = sys_stdout  # Asegura que la salida estándar se restaure
        result_container['adelante'] = adelante_output.getvalue()

    def _ejecutar_atras(self, meta, bc, result_container):
        """Función objetivo para el hilo de HaciaAtras."""
        atras_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = atras_output
        try:
            atras = AS.HaciaAtras(meta, bc)
            atras.proceso()
        finally:
            sys.stdout = sys_stdout # Asegura que la salida estándar se restaure
        result_container['atras'] = atras_output.getvalue()

    def procesar(self):
        """
        Ejecuta los procesos HaciaAdelante y HaciaAtras en hilos paralelos
        y muestra los resultados en una nueva ventana.
        """
        self.bc = [entry.get() for entry in self.entries if entry.get()]
        self.meta = self.metaTextField.get()
        
     
        self.process_button.config(state=DISABLED)

        # Diccionario para almacenar los resultados de los hilos
        results = {}

        # Crear los hilos
        thread_adelante = threading.Thread(target=self._ejecutar_adelante, args=(self.meta, self.bc.copy(), results))
        thread_atras = threading.Thread(target=self._ejecutar_atras, args=(self.meta, self.bc.copy(), results))

        # Iniciar los hilos
        thread_adelante.start()
        thread_atras.start()

        # Esperar a que ambos hilos terminen
        thread_adelante.join()
        thread_atras.join()
        
        # Habilita el botón nuevamente
        self.process_button.config(state=NORMAL)

        # Obtener los resultados capturados
        adelante_text = results.get('adelante', 'Error al ejecutar Hacia Adelante.')
        atras_text = results.get('atras', 'Error al ejecutar Hacia Atrás.')

        # Crear ventana de resultados (esto se hace después de que los hilos terminen)
        self._crear_ventana_resultados(adelante_text, atras_text)

    def _crear_ventana_resultados(self, adelante_text, atras_text):
        resultsWindow = Toplevel()
        resultsWindow.title("Resultados")

        Label(resultsWindow, text=f"Base de conocimiento: {self.bc}").pack()
        Label(resultsWindow, text=f"Meta: {self.meta}").pack()

        frame = Frame(resultsWindow)
        frame.pack(fill=BOTH, expand=True)

        # Panel para HaciaAdelante
        adelante_frame = Frame(frame)
        adelante_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        Label(adelante_frame, text="Resultado Hacia Adelante", font=("Arial", 12, "bold")).pack()
        adelante_scroll = Scrollbar(adelante_frame)
        adelante_scroll.pack(side=RIGHT, fill=Y)

        adelante_panel = Text(adelante_frame, wrap=WORD, width=50, yscrollcommand=adelante_scroll.set)
        adelante_panel.insert(END, adelante_text)
        adelante_panel.config(state=DISABLED)
        adelante_panel.pack(side=LEFT, fill=BOTH, expand=True)
        adelante_scroll.config(command=adelante_panel.yview)

        # Panel para HaciaAtras
        atras_frame = Frame(frame)
        atras_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        Label(atras_frame, text="Resultado Hacia Atrás", font=("Arial", 12, "bold")).pack()
        atras_scroll = Scrollbar(atras_frame)
        atras_scroll.pack(side=RIGHT, fill=Y)

        atras_panel = Text(atras_frame, wrap=WORD, width=50, yscrollcommand=atras_scroll.set)
        atras_panel.insert(END, atras_text)
        atras_panel.config(state=DISABLED)
        atras_panel.pack(side=LEFT, fill=BOTH, expand=True)
        atras_scroll.config(command=atras_panel.yview)


Gui()