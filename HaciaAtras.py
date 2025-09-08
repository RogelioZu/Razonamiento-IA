
import random

class HaciaAtras:

    def __init__(self,meta,bc):
        self.meta = meta
        self.bc = bc

    def condiciones_hacia_atras(self, a):
        R1 = ["h8","h6","h5"]
        R2 = ["h6","h3"]
        R3 = ["h7","h4"]
        R4 = ["h8"]
        R5 = ["h6"]
        R6 = ["h9","h1"]
        R7 = ["h7"]
        R8 = ["h1","h7"]
        R9 = ["h1","h8"]
 
        coincidencias = []
        #Vemos donde se encuentra  a como conclusion
        if a == 1:
            coincidencias.append(R1)
        if a == 2:
            coincidencias.append(R2)    
        if a == 3:
            coincidencias.append(R3)
        if a == 4:
            coincidencias.append(R4)
        if a == 5:
            coincidencias.append(R5)    
        if a == 6:
            coincidencias.append(R6)
        if a == 7:
            coincidencias.append(R7)
        if a == 8:
            coincidencias.append(R8)    
        if a == 9:
            coincidencias.append(R9)

        #Devuelme las coincidencias
        return coincidencias

    def sub_objetivo(self,a):

        #su primer elemento es su indice
        #Condiciones de las Reglas
        R1 = [1,"h8","h6","h5"]
        R2 = [2,"h6","h3"]
        R3 = [3,"h7","h4"]
        R4 = [4,"h8"]
        R5 = [5,"h6"]
        R6 = [6,"h9","h1"]
        R7 = [7,"h7"]
        R8 = [8,"h1","h7"]
        R9 = [9,"h1","h8"]


        #Conculsiones de la reglas para el razonamiento hacia atras
        CR1 = "h4"
        CR2 = "h9"
        CR3 = "h9"
        CR4 = "h1"
        CR5 = "h5"
        CR6 = "h2"
        CR7 = "h6"
        CR8 = "h9"
        CR9 = "h6"
        
        coincidencias = []
     #Vemos donde se encuentra  a como conclusion
        if a == CR1:
            coincidencias.append(R1)
        if a == CR2:
            coincidencias.append(R2)    
        if a == CR3:
            coincidencias.append(R3)
        if a == CR4:
            coincidencias.append(R4)
        if a == CR5:
            coincidencias.append(R5)    
        if a == CR6:
            coincidencias.append(R6)
        if a == CR7:
            coincidencias.append(R7)
        if a == CR8:
            coincidencias.append(R8)    
        if a == CR9:
            coincidencias.append(R9)

        #Devuelme las coincidencias
        return coincidencias


    def resolucion_de_conflictos(self,reglas,bc):
        if not reglas:
            return None

        set_bc = set(bc)

        # 1. INICIALIZAMOS con la primera regla como la mejor candidata.
        #    Esto garantiza que 'mejor_regla' nunca sea None dentro del bucle.
        mejor_regla = reglas[0]
        condiciones_mejor_regla = mejor_regla[1:]
        max_coincidencias = len(set_bc.intersection(condiciones_mejor_regla))
        
        print(f"Evaluando Regla: {mejor_regla[0]} -> Coincidencias: {max_coincidencias} (Candidata inicial)")

        # 2. Iteramos por el RESTO de las reglas (a partir de la segunda).
        for regla in reglas[1:]:
            indice_actual = regla[0]
            condiciones_actuales = regla[1:]
            
            coincidencias_actuales = len(set_bc.intersection(condiciones_actuales))
            print(f"Evaluando Regla: {indice_actual} -> Coincidencias: {coincidencias_actuales}")

            # Si esta regla tiene más coincidencias, es la nueva mejor.
            if coincidencias_actuales > max_coincidencias:
                max_coincidencias = coincidencias_actuales
                mejor_regla = regla
            
            # Si hay empate en coincidencias, usamos el índice más bajo.
            elif coincidencias_actuales == max_coincidencias:
                if indice_actual < mejor_regla[0]:
                    mejor_regla = regla

        print(f"-> Conflicto resuelto. Gana la Regla: {mejor_regla[0]}")
        return mejor_regla
    

    
    def proceso(self):

        goal_stack = [self.meta]
        pseudo_bc = self.bc.copy()
        iterable = 0
    
        while goal_stack:

            print("\n------------------")
            print(f"Pila actual: {goal_stack}")
            objetivo_actual = goal_stack.pop()
            print(f"Intentando resolver: '{objetivo_actual}'")
            
            if objetivo_actual in pseudo_bc:
                print(f"-> '{objetivo_actual}' ya es un hecho conocido.")
                continue

            reglas_disponibles = self.sub_objetivo(objetivo_actual)
            
            if not reglas_disponibles:
                print(f"-> No hay reglas para resolver '{objetivo_actual}'. No se puede probar por esta vía.")
                print("\nFallo: no se pudo encontrar el objetivo final.")
                return

            hecho_derivado = False
            for regla in reglas_disponibles:
                antecedentes_regla = regla[1:]
                if all(antecedente in pseudo_bc for antecedente in antecedentes_regla):
                    print(f"hecho derivado Todos los antecedentes {antecedentes_regla} de la regla {regla[0]} son verdaderos")
                    pseudo_bc.append(objetivo_actual)
                    hecho_derivado = True
                    break
            
            if hecho_derivado:
                continue
                
            mejor_regla = self.resolucion_de_conflictos(reglas_disponibles, pseudo_bc)
            
            antecedentes = mejor_regla[1:]
            
            print(f"-> Los antecedentes de la regla {mejor_regla[0]} son {antecedentes}")
            iterable += 1
            print(f"Iteracion: {iterable}")
            goal_stack.append(objetivo_actual)
            for antecedente in antecedentes:
                if antecedente not in pseudo_bc and antecedente not in goal_stack:
                    goal_stack.append(antecedente)
            
        if self.meta in pseudo_bc:
            print("\n¡ÉXITO! El objetivo final fue encontrado.")
            self.bc.append(self.meta)
            print(f"Base de conocimiento final: {self.bc}")
        else:
            print("\nFallo: no se pudo encontrar el objetivo final.")