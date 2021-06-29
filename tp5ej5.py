### 5. Inversión de mayusculas
#Implementar una funcion que dada un texto, deje en minuscula lo que esté en mayuscula y 
#en mayuscula lo que esté en minuscula.

def inversiondekeys(texto):
    texto=texto.swapcase()
    print(texto)


def prueba():
    texto=input("ingrese su texto: ")
    inversiondekeys(texto)

if __name__ == "__main__":
    prueba()