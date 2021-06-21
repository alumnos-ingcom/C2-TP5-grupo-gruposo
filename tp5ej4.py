#4. Números perfectos
#“Un numero entero es llamado perfecto cuando este numero es igual a la suma de sus divisores exactos”

#Escribir una función que determine si un numero entero positivo es un número perfecto.

def numerosperfectos(numero):
    resultado=0
    for i in range(1,numero):
        if (numero%i==0):
            resultado=resultado+i
    if(resultado==numero):
        print("El numero es un entero Perfecto")
    else:
        print("el numero no es perfecto")
def prueba():
    numero=input("ingrese un numero entero: ")
    numerosperfectos(int(numero))

if __name__ == "__main__":
    prueba()