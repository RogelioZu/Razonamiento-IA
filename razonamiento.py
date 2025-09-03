

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


def resolucion_de_conflictos(reglas,bc):
       
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
           elif coincidencias_actuales > max_coincidencias and coincidencias_actuales > 0:
                max_coincidencias = coincidencias_actuales
                mejor_regla = [regla]
                return mejor_regla[0][0]
               
    
    

def nuevo_conocimiento_adelante(a):
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
    


def sub_objetivo(a):
        
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




def nuevo_sub_objetivo(sub, bc):
    
    set_bc = set(bc)

    if sub in set_bc:
        return sub
    else:
        return set_bc.difference(sub)
