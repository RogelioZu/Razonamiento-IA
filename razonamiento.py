import threading

h1 = False
h2 = False
h3 = False
h4 = False
h5 = False
h6 = False
h7 = False 
h8 = False
h9 = False

#Base de conocimiento
bc = []
    
 #Reglas de el razonamiento
 #Reciben como parametro un texto   

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

def reglas(a):
  print(type(a))



if __name__ == '__main__':
   print()

