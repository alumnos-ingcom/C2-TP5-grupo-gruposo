### 13. Búsqueda de palabras
#Escribir una función que dado un texto y una palabra, 
#retorne la ubicación de la palabra en el texto o una excepción si la palabra no forma parte del texto.

#Considerar solo la primera vez que aparezca la palabra a buscar.
def busquedadepalabra(texto,palabra):
    ubicacion=texto.find(palabra)
    if (ubicacion ==-1):
        return "la palabra no existe en el texto indicado"
    else:
        return ubicacion

def prueba():
   texto=input("ingrese el texto a analizar: ")
   palabra=input("ingrese la palabra a buscar: ")
   print(busquedadepalabra(texto,palabra))

if __name__ == "__main__":
    prueba()