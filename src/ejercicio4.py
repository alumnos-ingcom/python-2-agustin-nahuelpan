################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es 
la suma de los dos anteriores. En la misma, los dos primeros términos 
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la 
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2."""
# Reemplazar por las funciones del ejercicio

def fibonacci(numero):
    primer_numero = 1
    segundo_numero = 1
    while numero > 0:
        regreso = primer_numero + segundo_numero
        segundo_numero = primer_numero
        primer_numero = regreso
        numero = numero - 1
    return regreso
    
    pass

def principal(numero):
    regreso = fibonacci(numero)
    print (f"Después de sumar {numero} veces, el numero de finobachi es {regreso}")
    
    pass


if __name__ == "__main__":
    principal(numero)

if __name__ == "__main__":
    fibonacci(numero)