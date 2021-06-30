###############
# Katherina Soto - @ktyfer
# UNRN Andina - Introducción a la Ingenieria en Computación
#grupo gruposo
################

#Parentesis balanceado



def parentesis_balanceado(cadena):
    
    if len(cadena) % 2 != 0 or len(cadena) == 0:
        respuesta = "NO"
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
                    respuesta = "NO"
    
    
def prueba():
    cadena = [x for x in input('Ingrese parentesis: ') if x in "{}[]()"]
    
    cad = parentesis_balanceado(cadena)
    
    print(f'salida par de parentesis {parentesis_balanceado(cadena)}')
    


if __name__ == "__main__":
    prueba() 