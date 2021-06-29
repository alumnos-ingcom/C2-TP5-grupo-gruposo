################
# Katherina Soto - @ktyfer
# UNRN Andina - Introducción a la Ingenieria en Computación
#grupo gruposo
################


# cifrado de cesar

#introducimmos texto a cifrar

def texto_chr(texto):
    
    if texto == texto.upper():
        
        abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    
    else:
        abc = 'abcdefghijklmnñopqrstuvwxyz'
    


def cifrado_ord(cifrado):
    cifrado = ''
    
    for c in cifrado:
        
        if c in abc:
            cifrad += abc [(abc.index(c)+k)%(len(abc))]
        
        else:
            cifrad += c
         


def prueba():
    abc = input("Tu texto: ")
    
    texto = texto_chr(abc)
    
    
    cifrado = int(input('Valor de desplazamiento: '))
    
    desplazamiento = cifrado_ord(texto)
    
    
    print(f'Texto ingresado: {texto_chr(texto)}) \nTexto cifrado: {cifrado_ord(texto, cifrado)})')

if __name__ == "__main__":
    prueba()

    