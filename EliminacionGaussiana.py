import numpy as np

def eliminacionGauss(n, a, b, x):

    # ----------------------- Pivoteo --------------------------- #
    for k in range(n - 1):
    # Elegir el valor mas alto en la matriz para hacer de pivote
        max = abs(a[k:, k]).argmax() + k
        if (a[max, k] == 0):
            print("La matriz no tiene soluciones")
        # Hacer los cambios
        if max != k:
            a[[k, max]] = a[[max, k]]
            b[[k, max]] = b[[max, k]]
    # ---------------------- Fin Pivoteo ----------------------- #
    # ------------------------- Gauss -------------------------- #

        for i in range(k + 1, n):
            multi = a[i][k] / a[k][k]
            a[i][k] = multi
            for j in range(k + 1, n):
                a[i][j] -= multi * a[k][j]
            b[i] -= b[k] * multi

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in reversed(range(n)):
        suma = b[i]
        for j in range(i + 1, n):
            suma -= a[i][j] * x[j]
        x[i] = suma / a[i][i]
    # ---------------------- FIn Gauss ------------------------ #

    print("\nLa matriz después de aplicar la eliminación Gaussiana con pivoteo es: \n")
    print("     Matriz A \n",a)
    print("     Matriz b \n",b)
    print("\nLos valores que resuelven la ecuación son:")
    for i in range(n):
        print("T_{} = {}".format(i+1, x[i]))

def procesos():
    a = np.array([[4, -1, -1, 0], [-1, 4, 0, -1], [-1, 0, 4, -1], [0, -1, -1, 4]],dtype=float) #Matriz A o principal
    b = np.array([[30.], [60.], [40.], [70.]]) #Matriz B
    n = len(a)
    x = np.zeros(n) #Valores de x

    print("La matriz ingresada es: \n")
    print("     Matriz A \n", a)
    print("     Matriz b \n", b)

    eliminacionGauss(n, a, b, x)

procesos()