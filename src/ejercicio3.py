################
# Nombre - @agustin-nahuelpam
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
```python
['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
```
y 
```python
['H', 'o', 'l', 'a']
```
Tienen una superposición de cuatro elementos.

#### Extra #1
Indicar en lugar de la cantidad de caracteres superpuestos, la posicion 
de inicio de la superposición."""

def superposicion(uno, dos):
    lista_uno = len(uno) -1
    lista_dos = len(dos) -1
    fallos = []
    contador = 0
    if lista_uno > lista_dos:
        limite_contador = lista_dos #El maximo de superposición debería ser la lista más chica. Por que más alla de ella no podrian superponerse.
        numeros_adicionales = lista_uno #Para agregar después cuales espacios de la lista más grande no se superponen.
    elif lista_uno < lista_dos:
        limite_contador = lista_uno
        numeros_adicionales = lista_dos
    elif lista_uno == lista_dos:
        limite_contador = lista_uno
        numeros_adicionales = lista_dos
    while contador <= limite_contador:
        primero = uno[contador]
        segundo = dos[contador]
        if primero == segundo:
            fallos.append(1)
        else:
            fallos.append(0)
        contador = contador + 1
    while contador <= numeros_adicionales:
        fallos.append(0)
        contador = contador + 1
    return fallos
    
    pass

def superposicion_lugar(uno, dos):
    lista_uno = len(uno) -1
    lista_dos = len(dos) -1
    contador = 0
    if lista_uno > lista_dos:
        limite_contador = lista_dos #El maximo de superposición debería ser la lista más chica. Por que más alla de ella no podrian superponerse.
    elif lista_uno < lista_dos:
        limite_contador = lista_uno
    else:
        limite_contador = lista_uno
    while contador <= limite_contador:
        primero = uno[contador]
        segundo = dos[contador]
        if primero == segundo:
            fallos = contador
            contador = limite_contador
        contador = contador + 1
    return fallos

    pass

def superposicion_cantidad(uno, dos):
    lista_uno = len(uno) -1
    lista_dos = len(dos) -1
    fallos = []
    contador = 0
    fallos.append(0)
    if lista_uno > lista_dos:
        limite_contador = lista_dos #El maximo de superposición debería ser la lista más chica. Por que más alla de ella no podrian superponerse.
    elif lista_uno < lista_dos:
        limite_contador = lista_uno
    else:
        limite_contador = lista_uno
    while contador <= limite_contador:
        primero = uno[contador]
        segundo = dos[contador]
        if primero == segundo:
            inicio = fallos[0]
            if inicio == 0:
                fallos[0] = 1
            elif inicio == 1:
                fallos.append(1)
            contador = contador +1
        else:
            contador = contador + 1
    return fallos

    pass

def separar_caracteres(primera):
    """
    Función que separa los caracteres de una frase o linea.
    """
    cantidad = len(primera) -1
    numero = 0
    orden = []
    while numero <= cantidad:
        letra = primera[numero]
        orden.append(letra)
        numero = numero + 1
    return orden
    
    pass

def principal():
    """
    Pide al usuario que ingrese las frases a comparar.
    """
    primera = input("Ingrese una frase: ")
    orden = separar_caracteres(primera)
    uno = orden #La primera cadena queda en uno.
    primera = input("Ingrese una frase: ")
    orden = separar_caracteres(primera)
    dos = orden # La segunda queda en dos.
    eleccion = int(input("Presione 1, si desea saber cuantos caracteres superpuestos hay. Presiones 2, si desea saber a partir de que punto se superponen los caracteres. Presione 3, si desea ver una lista que indica el lugar excato de superpocision tomando como base la lista más larga: "))
    if eleccion == 1:
        fallos = superposicion_cantidad(uno, dos)
        print (f"La cantidad de numeros superpuestos esta indicado con un 1 por cada uno de ellos: {fallos}")
    elif eleccion == 2:
        fallos = superposicion_lugar(uno, dos)
        print (f"El lugar en donde inicio la superpocición de los caracteres es a partir del numero de caracter numero {fallos}")
    elif eleccion == 3:
        fallos = superposicion(uno, dos)
        print (f"Tomando la linea más extensa, los caracteres  seran indicados con un 1 cuando estan superpuestos, y con un 0 cuando no lo esten: {fallos}")
    
    pass


if __name__ == "__main__":
    principal()

if __name__ == "__main__":
    superposicion(uno, dos)
    
if __name__ == "__main__":
    separar_caracteres(primera)
    
if __name__ == "__main__":
    superposicion_cantidad(uno, dos)

if __name__ == "__main__":
    superposicion_lugar(uno, dos)