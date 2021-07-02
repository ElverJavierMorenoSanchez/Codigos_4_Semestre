import numpy as np

#Variables
matriz = []
arr = np.array([])

#Funcion que permite ingresar los valores de la matriz por teclado
def inputMatriz():
    for i in range(2):
        matriz.append([0] * 2)

    for i in range(2):
        for j in range(2):
            matriz[i][j] = int(input('Introduce el valor de la posicion [{}][{}]: '.format(i, j)))

    return np.array(matriz) #se retorna una matriz con los valores que el usuario digito

#Calcular el determinante
def calDeterminante(arr):
    #se obtiene el valor de la multiplicacion de la diagonales y se restan
    #luego se returna el valor de la operacion
    return (arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0])

#Funcion para calcular la matriz adjuta
def calMAdjunta(arr):
    #A traves de dos ciclos for se intercambian los valores de las diagonales
    for i in range(2):
        for j in range(2):
            if(i == 0 and i==j): #Intercambio en la diagonal principal
                aux = arr[i][j]
                arr[i][j] = arr[i+1][j+1]
                arr[i + 1][j + 1] = aux
            elif(i == 0 and i!=j): #Intercambio en la diagonal secundaria
                aux = arr[i][j]
                arr[i][j] = - arr[i + 1][j - 1]
                arr[i + 1][j - 1] = - aux

    return arr #se retorna la matriz adjunta


#Llamada a las funciones
arr = inputMatriz()
print('\n La matriz introducida es:')
print(arr)

determinante = calDeterminante(arr)
print('\n El determinante de la matriz es: ', determinante)

print('\n La matriz transpuesta es:')
print(arr.T)

arr = calMAdjunta(arr.T)
print('\n La matriz adjunta es:')
print(arr)

arr = arr/determinante
print('\n La matriz inversa es:')
print(arr)
print('\n')

