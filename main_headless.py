import HaciaAdelante as A
import HaciaAtras as AS


print("Escriba 2 elemntos para la base de conocimiento: ")
bc = []


bc.append(input())
bc.append(input())

print("Introduzca la meta: ")
meta = input()

print(f"Base de conocimiento {bc}")
print(f"meta: {meta}")



adelante = A.HaciaAdelante(meta,bc)
adelante.proceso()




#atras = AS.HaciaAtras(meta,bc)
#atras.proceso()