import numpy as np

def tridiag(n,d,a,c,b):
    x = np.zeros(n)
    for i in range(1,n-1):
        mult = a[i-1]/d[i-1]
        d[i] -= mult*c[i-1]
        b[i] -= mult*b[i-1]

    print("Valores de x que resuelven el sistema de ecuaciones:\n",d)
    x[n - 1] = b[n - 1] / d[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - c[i] * x[i + 1]) / d[i]
    return x

def procedimiento():
    n=100
    a=np.ones(n) #Creacion diagonal principal con puros ceros
    d=0.5*np.ones(n) #Creacion de la Super diagonal
    c=0.5*np.ones(n) #Creacion de la Subdiagonal

    #Creacion de los terminos independientes
    b=2*np.ones(n)
    b[0]=1.5
    b[n-1]=1.5

    #Imprimir los resultados
    print("Superdiagonal:\n",d,"\n")
    print("Diagonal Principal:\n",a,"\n")
    print("Subdiagonal:\n",c,"\n")
    print("Terminos Independientes:\n",b,"\n")

    tridiag(n,a,c,d,b)

procedimiento()

