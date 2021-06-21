### 12. Comparación de listas
#Escribir una función que que determine retornando True si un par de listas contienen
#los mismos elementos que pueden estar estén ubicados en diferentes posiciones.
def mismos_valores(lista_1,lista_2):   
    if (len(lista_1)==len(lista_2)):
        for i in range(len(lista_1)):
            aux=lista_1[i]
            if aux in lista_2:
                pass
            else:
                return False
        return True
    else:
        print("las listas no tienen la misma cantidad de elementos")
        return False
        

def prueba():
    primer_lista=["hola","como","estas"]
    segunda_lista=["como","hola","estas"]
    tercer_lista=["como","hola","amigo"]
    cuarta_lista=["hola"]
    quinta_lista=["hola","como","estas","amigo"]
    print(mismos_valores(primer_lista,segunda_lista),"\n")
    print(mismos_valores(primer_lista,tercer_lista),"\n")
    print(mismos_valores(segunda_lista,quinta_lista),"\n")
    print(mismos_valores(tercer_lista,cuarta_lista),"\n")

if __name__ == "__main__":
    prueba()