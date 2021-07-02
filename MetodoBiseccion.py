import numpy as np

f = lambda x: np.sin(7*x)+np.cos(3*x) #función donde buscaremos las raíces

def biseccion(a,b,nmax,tol): #Método príncipal
    fa = f(a) #se buscan los valores de f en los intervalos a y b
    fb = f(b)

    #se compruba que haya por lo menos una raíz disponible en el intervalo
    if(fa*fb>0):
            print ("f(a) y f(b) Tienen el mismo signo en el intervalo [{},{}]".format(a,b))
            print("f({}) = {} y f({}) = {}".format(a,fa,b,fb))
            return

    print("  Iteración      \t     Intervalo\n")
    error = b-a
    for n in range(0,nmax): #Empezamos a buscar el valor de la raíz
        error /= 2
        c = a + error
        fc = f(c)
        print("\t [{}] \t [{} , {}]".format(n,a,c))

        if (np.abs(error) < tol):
            print("\nLa función esta muy cerca del cero en el punto: ", c)
            return
        if (fa * fc > 0):
            fa = fc
            a = c

print("\t\t\t--------------------------------------")
print("\t\t\t|       MÉTODO DE LA BISECCIÓN       |")
print("\t\t\t--------------------------------------\n")
biseccion(-1,0,100,1e-6) #Llamada al método






