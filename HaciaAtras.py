import razonamiento as r
import random

class HaciaAtras:

    def __init__(self,meta,bc):
        self.meta = meta
        self.bc = bc


    def proceso(self):
        extracciones = []

        #Vemos donde se encuentra la meta como conclusion
        if self.meta == r.CR1:
            extracciones.append(r.R1)
        if self.meta == r.CR2:
            extracciones.append(r.R2)    
        if self.meta == r.CR3:
            extracciones.append(r.R3)
        if self.meta == r.CR4:
            extracciones.append(r.R4)
        if self.meta == r.CR5:
            extracciones.append(r.R5)    
        if self.meta == r.CR6:
            extracciones.append(r.R6)
        if self.meta == r.CR7:
            extracciones.append(r.R7)
        if self.meta == r.CR8:
            extracciones.append(r.R8)    
        if self.meta == r.CR9:
            extracciones.append(r.R9)

        i = 0
        print(extracciones)
        for e in extracciones:
            print(f"El objetivo se encuentra como conclusion en la regla: {extracciones[i][0]}")
            i += 1
        if len(extracciones) > 1:
            extraer = random.choice(extracciones)
        else:
            extraer = extracciones[0]

        print(f"Regla a analizar: {extraer}")

        sub_objetivo = random.choice(extraer[1:])
        print(f"Sub objetivo: {sub_objetivo} (Elegido al azar)")
