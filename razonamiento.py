

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


def regla_1(a,b,c):
   h8 = True if a == "h8" else False
   h6 = True if b == "h6" else False
   h5 = True if c == "h5" else False
   h4 = True if h8 and h6 and h5 else False
   return h4

def regla_2(a,b):
   h6 = True if a == "h6" else False
   h3 = True if b == "h3" else False
   h9 = True if h6 and h3 else False
   return h9

def regla_3(a,b):
   h7 = True if a == "h7" else False
   h4 = True if b == "h4" else False
   h9 = True if h7 and h4 else False
   return h9
   
def regla_4(a):
   h8 = True if a == "h8" else False
   h1 = True if h8 else False
   return h1

def regla_5(a):
    h6 = True if a == "h6" else False
    h5 = True if h6 else False
    return h5

def regla_6(a,b):
   h9 = True if a == "h9" else False
   h1 = True if b == "h1" else False
   h2 = True if h9 and h1 else False
   return h2

def regla_7(a):
   h7 = True if a == "h7" else False
   h6 = True if h7 else False
   return h6

def regla_8(a,b):
   h1 = True if a == "h1" else False
   h7 = True if b == "h7" else False
   h9 = True if a and b else False
   return h9

def regla_9(a,b):
   h1 = True if a == "h1" else False
   h8 = True if b == "h8" else False
   h6 = True if a and b else False
   return h6


