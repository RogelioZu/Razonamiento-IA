import tkinter as tk
from tkinter import scrolledtext, messagebox

class TextPanel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Panel de Texto Dividido")
        self.window.geometry("800x600")
        self.window.configure(bg='#f0f0f0')
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame superior para el botón
        top_frame = tk.Frame(self.window, bg='#f0f0f0', height=60)
        top_frame.pack(fill=tk.X, padx=10, pady=10)
        top_frame.pack_propagate(False)  # Mantener altura fija
        
        # Botón Procesar
        process_btn = tk.Button(
            top_frame,
            text="PROCESAR",
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            bd=0,
            relief='flat',
            padx=20,
            pady=10,
            command=self.process_text
        )
        process_btn.pack(pady=15)
        
        # Frame principal para los paneles de texto
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Configurar el grid para dividir en dos columnas iguales
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
        # Panel izquierdo
        left_frame = tk.Frame(main_frame, bg='#f0f0f0')
        left_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 5))
        
        # Etiqueta para panel izquierdo
        left_label = tk.Label(
            left_frame,
            text="Panel Izquierdo",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        left_label.pack(pady=(0, 5))
        
        # Área de texto izquierda con scroll
        self.left_text = scrolledtext.ScrolledText(
            left_frame,
            font=('Consolas', 11),
            bg='white',
            fg='#333333',
            bd=1,
            relief='solid',
            wrap=tk.WORD
        )
        self.left_text.pack(fill=tk.BOTH, expand=True)
        
        # Panel derecho
        right_frame = tk.Frame(main_frame, bg='#f0f0f0')
        right_frame.grid(row=0, column=1, sticky='nsew', padx=(5, 0))
        
        # Etiqueta para panel derecho
        right_label = tk.Label(
            right_frame,
            text="Panel Derecho",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        right_label.pack(pady=(0, 5))
        
        # Área de texto derecha con scroll
        self.right_text = scrolledtext.ScrolledText(
            right_frame,
            font=('Consolas', 11),
            bg='white',
            fg='#333333',
            bd=1,
            relief='solid',
            wrap=tk.WORD
        )
        self.right_text.pack(fill=tk.BOTH, expand=True)
        
        # Agregar texto de ejemplo
        self.left_text.insert('1.0', "Escribe aquí tu texto...\n\nPuedes escribir lo que quieras en este panel.")
        self.right_text.insert('1.0', "Este es el panel derecho...\n\nTambién puedes escribir aquí.")
    
    def process_text(self):
        # Obtener el texto de ambos paneles
        left_content = self.left_text.get('1.0', tk.END).strip()
        right_content = self.right_text.get('1.0', tk.END).strip()
        
        # Ejemplo de procesamiento: mostrar información sobre el texto
        left_words = len(left_content.split()) if left_content else 0
        right_words = len(right_content.split()) if right_content else 0
        left_chars = len(left_content)
        right_chars = len(right_content)
        
        message = f"""PROCESAMIENTO COMPLETADO
        
Panel Izquierdo:
- Palabras: {left_words}
- Caracteres: {left_chars}

Panel Derecho:
- Palabras: {right_words}
- Caracteres: {right_chars}

Total de palabras: {left_words + right_words}
Total de caracteres: {left_chars + right_chars}"""
        
        messagebox.showinfo("Resultado del Procesamiento", message)
    
    def run(self):
        self.window.mainloop()

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = TextPanel()
    app.run()