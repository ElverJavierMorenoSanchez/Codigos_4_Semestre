#importar librerias
import math as mt

#Metodo para calcular la aproximacion de Tylor
def funcionTylor(trun, x):
    suma = 0
    n=0

    while(n<=trun):
        # implementacion de la formula de Tylor
        suma += (((-1)**n)*(x**((2*n)+1)))*(1/calFactorial((2*n)+1))
        print(n,". ", suma)
        n += 1
    return suma

#Metodo para el calculo del factorial
def calFactorial(x):
    if(x>=2):
        return x * calFactorial(x - 1)
    return 1

#Llamada a las funciones
x = mt.radians(float(input("Introduzca el valor de x en grados: ")))
n = int(input("Introduzca el valor de n: "))

print("")
funcionTylor(n,x)