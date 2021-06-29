### 10. Texto binario
#Implementar una funcion que dado un numero entero positivo, retorne una cadena 
# de texto con su representación binaria.
#Implementar una funcion que haga el proceso inverso; dada una cadena de texto, 
# retorne el numero entero.
def textobinario(numero):
    if (numero>0 and type(numero)==int):
        return str(bin(numero))
def binario_a_texto(texto):
    return int(texto,2)
def prueba():
    entero=input("ingrese valor entero: ")
    print(textobinario(int(entero)))
    texto=input("ingrese un valor binario: ")
    print(binario_a_texto(texto))

if __name__=="__main__":
    prueba()