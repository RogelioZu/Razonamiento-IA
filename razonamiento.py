

#su primer elemento es su indice y su segundo es el numero de condiciones 
R1 = [1,"h8","h6","h5"]
R2 = [2,"h6","h3"]
R3 = [3,"h7","h4"]
R4 = [4,"h8"]
R5 = [5,"h6"]
R6 = [6,"h9","h1"]
R7 = [7,"h7"]
R8 = [8,"h1","h7"]
R9 = [9,"h1","h8"]




 #Reglas de el razonamiento
 #Reciben como parametro un texto h1,h2,h3,...,h9


def nuevo_conocimiento(a):
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
    