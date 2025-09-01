import razonamiento as r

class HaciaAdelante:

    def __init__(self, meta, bc):
        self.meta = meta
        self.bc = bc
        
    def proceso(self):
        extracciones = []
        print(self.bc)
        print("Con cual elemento de la bc deseas extraer?")
        extraer = input()
        

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

        print(extracciones)
        nuevo = r.nuevo_conocimiento(self.resolucion_de_conflictos(extracciones))
        self.bc.append(nuevo)
        print(self.bc)

        

    def resolucion_de_conflictos(self,reglas):
       
       #convertimos la base de conocimiento en un conjunto para facilitar esto
       set_bc = set(self.bc)
       #variable para guardar la mejor regla
       mejor_regla = []
       max_coincidencias = -1

       for regla in reglas:
           indice_actual = regla[0]
           condiciones_actuales = regla[1:]
           #calculamos cuantas condiciones tiene la regla
           coincidencias_actuales = len(set_bc.intersection(condiciones_actuales))
           print(f"Regla ID {indice_actual}: {condiciones_actuales} -> Coincidencias: {coincidencias_actuales}")

           if coincidencias_actuales > max_coincidencias and len(condiciones_actuales) - coincidencias_actuales == 0:
               max_coincidencias = coincidencias_actuales
               mejor_regla = [regla]
               return mejor_regla[0][0]
           elif coincidencias_actuales == max_coincidencias:
               if indice_actual < mejor_regla[0][0]:
                   mejor_regla = [regla]
                   return mejor_regla[0][0]
        
    
    
    
        
        