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
        else:
            print("No se encontro ninguna regla con la condicion ")

        print(extracciones)

    def resolucion_de_conflictos(self,Reglas):
       print()