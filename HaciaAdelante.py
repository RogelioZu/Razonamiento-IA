import random

class HaciaAdelante:

    def __init__(self, meta, bc):
        self.meta = meta
        self.bc = bc


    def nuevo_conocimiento_adelante(self,a):
        if a == 1:
            return "h4"
        elif a == 2:
            return "h9"
        elif a == 3:
            return "h9"
        elif a == 4:
            return "h1"
        elif a == 5:
            return "h5"
        elif a == 6:
            return "h2"
        elif a == 7:
            return "h6"
        elif a == 8:
            return "h9"
        elif a == 9:
            return "h6"

    def resolucion_de_conflictos(self,reglas,bc):
       
       #convertimos la base de conocimiento en un conjunto para facilitar esto
       set_bc = set(bc)
       #variable para guardar la mejor regla
       mejor_regla = []
       max_coincidencias = -1

       for regla in reglas:
           indice_actual = regla[0]
           condiciones_actuales = regla[1:]
           #calculamos cuantas condiciones tiene la regla
           coincidencias_actuales = len(set_bc.intersection(condiciones_actuales))
           print(f"Regla: {indice_actual} : {condiciones_actuales} -> Coincidencias: {coincidencias_actuales}")

           if coincidencias_actuales > max_coincidencias and len(condiciones_actuales) - coincidencias_actuales == 0:
               max_coincidencias = coincidencias_actuales
               mejor_regla = [regla]
               print(f"Gana conflicto regla: {indice_actual}")
               return mejor_regla[0][0]
           elif coincidencias_actuales == max_coincidencias:
               if indice_actual < mejor_regla[0][0]:
                   mejor_regla = [regla]
                   print(f"Gana conflicto regla: {indice_actual}")
                   return mejor_regla[0][0]

        
    def proceso(self):
        print("\n------------------")
        R1 = [1,"h8","h6","h5"]
        R2 = [2,"h6","h3"]
        R3 = [3,"h7","h4"]
        R4 = [4,"h8"]
        R5 = [5,"h6"]
        R6 = [6,"h9","h1"]
        R7 = [7,"h7"]
        R8 = [8,"h1","h7"]
        R9 = [9,"h1","h8"]
        extracciones = []
        print(f"Base de conocimiento inicial {self.bc}")
        # print("Con cual elemento de la bc deseas extraer?")
        extraer = random.choice(self.bc)
        print(f"Intentando resolver: {extraer} (elegido al azar)")
        iteracion = 1
        print("Iteracion: 1")

        while True:
            print("\n------------------")

            if extraer in R1:
                extracciones.append(R1)
            if extraer in R2:
                extracciones.append(R2)
            if extraer in R3:
                extracciones.append(R3)
            if extraer in R4:
                extracciones.append(R4)
            if extraer in R5:
                extracciones.append(R5)
            if extraer in R6:
                extracciones.append(R6)
            if extraer in R7:
                extracciones.append(R7)
            if extraer in R8:
                extracciones.append(R8)
            if extraer in R9:
                extracciones.append(R9)

           
            if not extracciones:
                print("No se encontraron reglas que cumplan termina el proceso")
                break

            print(f"Reglas en conflicto {extracciones}")
            mejor_regla = self.resolucion_de_conflictos(extracciones,self.bc)

            if mejor_regla is None:
                print("No se pudo resolver ninguna regla. Proceso terminado.")
                break

            nuevo = self.nuevo_conocimiento_adelante(mejor_regla)
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
            
        

    
    
        
        