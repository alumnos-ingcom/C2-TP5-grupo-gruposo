### 14. Números capicúa
#Escribir una función que determine si un numero entero positivo es capicúa.
def capicua(numero):
    numero_a_lista=list(str(numero))
    contador=0
    longitud=len(numero_a_lista)
    for i in range(len(numero_a_lista)//2):
        if(numero_a_lista[i]==numero_a_lista[longitud-1]):
            pass
        else:
            print("no es capicua")
            break
        longitud=longitud-1
        contador=contador+1
    if contador==(len(numero_a_lista)//2):
        print("es capicua")


def prueba():
    valor=input("ingrese el numero a analizar: ")
    capicua(valor)
if __name__ == "__main__":
    prueba()