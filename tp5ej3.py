### 3. ¡Tribonacci!
#La secuencia de Tribonacci es el mismo concepto que la de Fibonacci común,
#pero acá en lugar de sumar dos terminos; se suman de a tres.
#[Tribonacci - OEIS](http://oeis.org/A000213) 
def tribonacci(num):
    if num < 4:
        return 1
    else:
        return tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)

def prueba():
    valor=int(input("ingrese el valor n : "))
    if (type(valor)==int and valor>2):
        print(tribonacci(valor))
    else:
        print("valor erroneo")


if __name__ == "__main__":
    prueba()