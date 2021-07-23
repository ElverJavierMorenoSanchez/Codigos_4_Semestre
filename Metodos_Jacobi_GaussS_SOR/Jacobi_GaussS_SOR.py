import numpy as np
import math as mt

def metodJacobi(n,A,b, x,kmax,E,P):
    print("\t\t\t--------------------------------------")
    print("\t\t\t|          MÉTODO DE JACOBI          |")
    print("\t\t\t--------------------------------------\n")

    for k in range(1,kmax+1): # Bucle que ira iterando segun el valor total de iteraciones seleccionado.
        y = np.copy(x) # Hacemos una copia de la matriz x

        for i in range(1,n+1):
            suma = b[i-1] # Obtenemos el valor de la matriz correspondiente a la iteracion
            diag = A[i-1][i-1] # Obtenemos el valor de la diagonal

            if(mt.fabs(diag) < P): # Comprobar si el elemento de la diagonal es pequeño
                print("El elemento de la diagonal es muy pequeño")

            # Realizamos las operaciones e iteraciones segun las formulas
            for j in range(1,n+1):
                if(j!=i):
                    suma -= A[i-1][j-1]*y[j-1]
            x[i-1]= (suma/diag) # Almacenamos el valor obtenido en la iteracion correspondiente


        print("     ", k, "  ", x)
        norm = np.linalg.norm(x - y) # Calculamos la norma para utilizarlo en el criterio de parada
        if (norm < E): # Criterio de parada
            print("\nCon una precision del {} se realizaron {} iteraciones.".format(E, k))
            print("\nLos valores que resuelven el sistema son: \n")
            for i in range(n):
                print("x_{} = {}".format(i+1, x[i]))
            break

def metodGaussSeidel(n,A,b, x,kmax,E,P):
    print("\t\t\t--------------------------------------")
    print("\t\t\t|      MÉTODO DE GAUSS - SEIDEL      |")
    print("\t\t\t--------------------------------------\n")
    for k in range(1,kmax+1): # Bucle que ira iterando segun el valor total de iteraciones seleccionado.
        y = np.copy(x) # Hacemos una copia de la matriz x

        for i in range(1,n+1):
            suma = b[i - 1]  # Obtenemos el valor de la matriz correspondiente a la iteracion
            diag = A[i - 1][i - 1]  # Obtenemos el valor de la diagonal

            if (mt.fabs(diag) < P): # Comprobar si el elemento de la diagonal es pequeño
                print("El elemento de la diagonal es muy pequeño")

            # Realizamos las operaciones e iteraciones segun las formulas
            for j in range(1,i):
                suma -= A[i-1][j-1]*x[j-1]
            for j in range(i+1,n+1):
                suma -= A[i - 1][j - 1] * x[j - 1]

            x[i-1]= (suma/diag) # Almacenamos el valor obtenido en la iteracion correspondiente

        print("     ", k, "  ", x)
        norm = np.linalg.norm(x - y) # Calculamos la norma para utilizarlo en el criterio de parada
        if (norm < E): # Criterio de parada
            print("\nCon una precision del {} se realizaron {} iteraciones.".format(E, k))
            print("\nLos valores que resuelven el sistema son: \n")
            for i in range(n):
                print("x_{} = {}".format(i+1, x[i]))
            break

def metodSOR(n,A,b, x,W,kmax,E,P):
    print("\t\t\t--------------------------------------")
    print("\t\t\t|             MÉTODO SOR             |")
    print("\t\t\t--------------------------------------\n")
    for k in range(1,kmax+1): # Bucle que ira iterando segun el valor total de iteraciones seleccionado.
        y = np.copy(x) # Hacemos una copia de la matriz x

        for i in range(1,n+1):
            suma = b[i - 1]  # Obtenemos el valor de la matriz correspondiente a la iteracion
            diag = A[i - 1][i - 1]  # Obtenemos el valor de la diagonal

            if (mt.fabs(diag) < P): # Comprobar si el elemento de la diagonal es pequeño
                print("El elemento de la diagonal es muy pequeño")

            # Realizamos las operaciones e iteraciones segun las formulas
            for j in range(1,i):
                suma -= A[i-1][j-1]*x[j-1]
            for j in range(i+1,n+1):
                suma -= A[i - 1][j - 1] * x[j - 1]
            x[i-1] = ((1-W)*y[i-1]) + (W*(suma/diag)) # Almacenamos el valor obtenido en la iteracion correspondiente

        print("     ",k, "  ",x)
        norm = np.linalg.norm(x - y) # Calculamos la norma para utilizarlo en el criterio de parada
        if (norm < E): # Criterio de parada
            print("\nCon una precision del {} se realizaron {} iteraciones.".format(E, k))
            print("\nLos valores que resuelven el sistema son: \n")
            for i in range(n):
                print("x_{} = {}".format(i+1, x[i]))
            break

def ejecuarAlgoritmos():
    A = np.array([[7,1,-1,2],[1,8,0,-2],[-1,0,4,-1],[2,-2,-1,6]],dtype=float) # Matriz A
    b = np.array([3,-5,4,-3],dtype=float) # Matriz b

    n = len(A) # Tamaño de la matriz
    x = np.zeros(n) # Creacion de la matriz que tendra los resultados

    kmax = 100 # Numero total de iteraciones
    E = 1e-4 # Valor para el criterio de parada, en este caso con cuatro decimales
    P = 1e-10 # Valor para saber si hay un valor muy pequeño en la matriz
    W = 1.1  # Parametro para acelerar la convergencia

    metodJacobi(n,A,b,x,kmax,E,P)
    #metodGaussSeidel(n,A,b,x,kmax,E,P)
    #metodSOR(n,A,b,x,W,kmax,E,P)

ejecuarAlgoritmos()


