import numpy as np

f = lambda x: np.sin(7*x)+np.cos(3*x) #función donde buscaremos las raíces

def secante(a,b, nmax, tol):  #Método príncipal
    print("  Iteración  \t    Valor de x\n")

    for n in range (0,nmax):
        fa = f(a)
        fb = f(b)
        x = (a*fb - b*fa)/(fb - fa)

        if(np.abs(x - b) > tol): #se compruba que ya nos encontremos muy cerca de la raíz
            print("\t [{}] \t [{}]".format(n,x))
            a = b
            b = x
        else:
            print("\nLa función esta muy cerca del cero en el punto: ", x)
            return

print("\t\t\t--------------------------------------")
print("\t\t\t|        MÉTODO DE LA SECANTE        |")
print("\t\t\t--------------------------------------\n")
secante(-1,0,100,1e-6) #Llamada al método

