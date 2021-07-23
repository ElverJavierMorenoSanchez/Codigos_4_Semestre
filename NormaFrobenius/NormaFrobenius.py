import numpy as np
import math as mt

def metodoFrobenius(n,A):
    print("\t\t\t---------------------------------------")
    print("\t\t\t|           NORMA FROBENIUS           |")
    print("\t\t\t---------------------------------------\n")

    print("La matriz ingresada es: \n\n",A)

    suma = 0
    for i in range(0,n): # Ciclo que recorrera las filas de la matriz
        for j in range(0,n): # Ciclo que recorrera las columnas de la matriz
            suma += A[i][j]**2 # Suma de cada valor de la matriz elevado al cuadrado

    print("\nLa suma de todos los valores de la matriz elevados al cuadrado es: ", suma)
    norma = mt.sqrt(suma) # Se saca la raiz de la suma y se retorna ese valor
    print("\nEl valor de la norma es:", norma)


A = np.array([[3,1,-4,8,5],[2,7,-8,7,4],[7,9,2,1,3],[1,5,9,3,2],[1,5,9,3,1]]) # Creacion de la matriz
n = len(A) # Tamaño de la matriz

metodoFrobenius(n,A) # Llamada a la funcion y obtenecion del resulatado.



