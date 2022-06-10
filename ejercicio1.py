import numpy as np
import random as rm

arreglo = np.array([[rm.randrange(0,100) for i in range (0,3)],[rm.randrange(0,100) for i in range (0,3)]])

arreglo2 = np.array([ [rm.randrange(0,100) for i in range (0,3)] for i in range(0,3) ])

#print(arreglo)

print(arreglo2)

print(f"El promedio de todos los elementos es {arreglo2.mean()}")
print(f"La suma de la matriz es {arreglo2.sum()}")
print(f"Obtener la diagonal {arreglo2.diagonal()}")