import razonamiento as r
import random

class HaciaAtras:

    def __init__(self,meta,bc):
        self.meta = meta
        self.bc = bc


    def proceso(self):
        
        extraer = self.meta
        extracciones = r.sub_objetivo(extraer)
        print(extracciones)
        print(f"Los antecendentes de {extraer} son {extracciones[0][1:]}")
        #sub_objetivo = random.choice(extracciones[0][1:])
        sub_objetivo = extracciones[0][1]
        print(f"Sub objetivo elegido al azar: {sub_objetivo}")
        iteracion = 1
        print("Iteracion: 1")
        while True:    
            
            reglas_sub_objetivo = r.sub_objetivo(sub_objetivo)
            print(f"Reglas en conflicto para el sub objetivo {reglas_sub_objetivo}")
            mejor_regla = r.resolucion_de_conflictos(reglas_sub_objetivo, self.bc)

            if mejor_regla is None:
                print("No se pudo resolver ninguna regla. Proceso terminado.")
                break

            print(f"Mejor regla para el sub objetivo {mejor_regla}")

            extraer = r.condiciones_hacia_atras(mejor_regla)
            
            print(extraer[0][1:])
        
            
            sub_objetivo = r.nuevo_sub_objetivo(extraer[0][1:], self.bc)
            print(f"Nuevo sub objetivo {sub_objetivo}")

            break