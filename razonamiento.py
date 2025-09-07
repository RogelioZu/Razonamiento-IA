import random

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




def condiciones_hacia_atras(a):
 
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
    
    

def nuevo_sub_objetivo(a,bc):

    set_bc = set(bc)
    set_a = set(a)
    if set_a in set_bc:
        
        return None
    else:
        diferencia = set_a.difference(set_bc)
        if len(diferencia) > 1:
            return list(random.choice(diferencia))
        else:
            return list(diferencia)

