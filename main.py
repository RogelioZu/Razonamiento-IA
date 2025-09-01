import HaciaAdelante as A

print("Escriba 3 elemntos para la base de conocimiento: ")
bc = []


bc.append(input())
bc.append(input())


print("Introduzca la meta: ")
meta = input()

print(bc)
print("meta: " + meta)


adelante = A.HaciaAdelante(meta,bc)
adelante.proceso()

