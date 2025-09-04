import razonamiento as r
import random

class HaciaAdelante:

    def __init__(self, meta, bc):
        self.meta = meta
        self.bc = bc
        
    def proceso(self):
        extracciones = []
        print(self.bc)
        # print("Con cual elemento de la bc deseas extraer?")
        extraer = random.choice(self.bc)
        print(f"Elemento a extraer primero: {extraer} (elegido al azar)")
        iteracion = 1
        print("Iteracion: 1")

        while True:
            if extraer in r.R1:
                extracciones.append(r.R1)
            if extraer in r.R2:
                extracciones.append(r.R2)
            if extraer in r.R3:
                extracciones.append(r.R3)
            if extraer in r.R4:
                extracciones.append(r.R4)
            if extraer in r.R5:
                extracciones.append(r.R5)
            if extraer in r.R6:
                extracciones.append(r.R6)
            if extraer in r.R7:
                extracciones.append(r.R7)
            if extraer in r.R8:
                extracciones.append(r.R8)
            if extraer in r.R9:
                extracciones.append(r.R9)

            if not extracciones:
                print("No se encontraron reglas que cumplan termina el proceso")
                break

            print(f"Reglas en conflicto {extracciones}")
            mejor_regla = r.resolucion_de_conflictos(extracciones,self.bc)

            if mejor_regla is None:
                print("No se pudo resolver ninguna regla. Proceso terminado.")
                break

            nuevo = r.nuevo_conocimiento_adelante(mejor_regla)
            if nuevo is None:
                print("No se pudo generar nuevo conocimiento. Proceso terminado.")
                break
             # Verificar si el nuevo conocimiento ya existe en la BC
            if nuevo in self.bc:
                print(f"El conocimiento '{nuevo}' ya existe en la BC. Proceso terminado.")
                break

            self.bc.append(nuevo)
            print(f"Base de conocimiento actual: {self.bc}")
            extraer = nuevo
            extracciones = []

              # Verificar si se alcanzó la meta
            if nuevo == self.meta:
                print(f"¡Meta alcanzada! Se encontró: {self.meta}")
                break
            
            iteracion += 1
            print(f"Iteracion: {iteracion}")

        print(f"\nProceso finalizado. Base de conocimiento final: {self.bc}")
            
        

    
    
        
        