import razonamiento as r
import random

class HaciaAtras:

    def __init__(self,meta,bc):
        self.meta = meta
        self.bc = bc


    def proceso(self):
        contador = 0
        extracciones = []
        extraer = self.meta
        while True:
            #Vemos donde se encuentra la meta como conclusion
            extracciones = r.sub_objetivo(extraer)
            
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
            print(f"Sub-objetivo: {sub_objetivo} (Elegido al azar)")
            
            extraer = sub_objetivo
            extracciones = []
            contador += 1

            if contador > 1:
                if not extracciones:
                    print("No se encontraron reglas que cumplan termina el proceso")
                    break
                print(f"Reglas en conflicto {extracciones}")
                mejor_regla = r.resolucion_de_conflictos(extracciones,self.bc)
                

                if mejor_regla is None:
                    print("No se pudo resolver ninguna regla. Proceso terminado.")
                    break

                print(mejor_regla)