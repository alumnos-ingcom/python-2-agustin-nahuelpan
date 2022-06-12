################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
Escribir una función que retorne `True` cuando un número entero es par 
y `False` cuando no lo sea, sin utilizar módulo. (`%`)"""
# Reemplazar por las funciones del ejercicio

def pares_e_impares(numero):        
    if numero > 0:
        while numero > 0: #En el bucle while se mantiene hasta llegar a 0, porque el programa ya guarda la variable que va a devolver antes de que esto ocurra.
            numero = numero -1
            if numero == 0: #Si al restar un 1 llega a cero, ya se que es impar. Y cómo el bucle se repite hasta llegar a cero, cada vez que llegue a 0 en este punto indica que es impar.
                regreso = 1 == 2
            numero = numero -1
            if numero == 0: #Si es necesario restarle 2 para llegar a 0, eso quiere decir que es par. Y cómo el bucle se repite, siempre que llegue a 0 en este punto sera par.
                regreso = 1 == 1
    else:
        while numero < 0: #En caso de que sea negativo cumple la misma funcioón que el otro while.
            numero = numero +1
            if numero == 0: #Si al sumar un 1 llega a cero, ya se que es impar. Y cómo el bucle se repite hasta llegar a cero, cada vez que llegue a 0 en este punto indica que es impar.
                regreso = 1 == 2
            numero = numero +1
            if numero == 0: #Si es necesario sumarle 2 para llegar a 0, eso quiere decir que es par. Y cómo el bucle se repite, siempre que llegue a 0 en este punto sera par.
                regreso = 1 == 1
    return regreso


def principal(numero):
    regreso = pares_e_impares(numero)
    return regreso     
    pass


if __name__ == "__main__":
    principal(numero)

if __name__ == "__main__":
    pares_e_impares(numero)      
    