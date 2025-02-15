###############
# Katherina Soto - @ktyfer
# UNRN Andina - Introducción a la Ingenieria en Computación
# grupo gruposo
################

# Parentesis balanceado
# Implementar una función que determine si **una** cadena con parentesis está balanceada.

# Es decir, si cada parentesis que abre, tiene su par que cierra.
# El resultado debe ser un valor lógico indicando si esta o no balanceado.

# **Ejemplos**

#   (vacio)      OK
#   []           OK   
#   [][]         OK   
#   [[][]]       OK 
#   ][           NO OK
#   ][][         NO OK
#   []][[]       NO OK
       
# La funcion deberia de ignorar todo lo que no sean parentesis.

# **Extra**: Permitir la modificacion de los caracteres a parentesis,
# llaves, o cualquier otro par de caracteres.

def parentesis_balanceado(cadena):
    
    largo = len(cadena)
    print(f"largo de la cadena: {largo}")
    #Esta es una variable de control provisoria para saber si entra la cadena completa
    #¿la borramos?????

    if ((len(cadena) % 2) == 1) or (len(cadena) == 0):
        respuesta = "NO1" #Marca la condicion de salida aquí o mas abajo
    else:
        respuesta = "YES"
        i = 0
        while i < len(cadena) and respuesta == "YES":
            if cadena[i] in "{[(":
                i += 1
            else:
                if cadena[i - 1] + cadena[i] in "{}" or \
                        cadena[i - 1] + cadena[i] in "[]" or \
                        cadena[i - 1] + cadena[i] in "()":
                    
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                else:
                    respuesta = "NO2" #marca la segunda condicion de salida
                    
    return respuesta
    
    
def prueba():
    cadena1 = [x for x in input("Ingrese parentesis: ") if x in "{}[]()"]
    print(f'salida par de parentesis {parentesis_balanceado(cadena1)}')
    
if __name__ == "__main__":
    prueba() 