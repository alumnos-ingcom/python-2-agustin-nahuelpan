################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes 
está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. 
El resultado debe ser un valor lógico indicando si esta o no balanceado.

**Ejemplos**
```
   (vacio)      True
   []           True
   [][]         True
   [[][]]       True
   ][           False
   ][][         False
   []][[]       False
```
La funcion deberia de ignorar todo lo que no sean corchetes.

#### Extra #1
Hacer que la funcion reciba _que_ par de simbolos buscar si esta 
balanceado. (como para pasar parentesis, llaves o cualquier otro)

#### Extra #2
Hacer que la función verifique el balanceo simultaneo de parentesis, 
llaves y corchetes.
"""

def corchetes_balanceados(cadena_armada, segundo, primero):
    """
    La funcion revisa si los corchetes estan desbalanceados.
    """
    numero_caracteres = len(cadena_armada) -1
    contador = 0
    primera_suma = 0
    segunda_suma = 0
    while contador <= numero_caracteres: #Reviso que tenga la misma cantidad de caracteres.
        comparacion = cadena_armada[contador]
        if comparacion == primero:
            primera_suma = primera_suma + 1
        if comparacion == segundo:
            segunda_suma = segunda_suma + 1
        contador = contador + 1
    if primera_suma != segunda_suma: #Si no los tiene ya se que es falsa.
        resultado = False
    elif primera_suma == 0 and segunda_suma == 0:
        resultado = True
    else: #Si los tiene necesito más pruebas. Dios mio.
        contador_dos = 0 #Vuelvo a revisar la lista.
        while contador_dos <= numero_caracteres:
            comparacion = cadena_armada[contador_dos] 
            if comparacion == segundo: #Revisa si el corchete de cierre aparece.
                cadena_armada[contador_dos] = " " 
                contador_tres = contador_dos #- 1 #un contador en el mismo punto que empieza a revisar.
                while contador_tres <= contador_dos:
                    comparacion_dos = cadena_armada[contador_tres]
                    if comparacion_dos == primero: #Revisa si aparece el caracter que la abre.
                        cadena_armada[contador_tres] = " " #Elimina ese numero.
                        contador_tres = 10000000#contador_dos + 2 #Un numero que se que debe ser más grande.
                    elif contador_tres < 0:
                        contador_tres = contador_dos + 1
                        contador_dos = numero_caracteres + 1
                        resultado = False
                    contador_tres = contador_tres + 1
            elif contador_dos == numero_caracteres:
                resultado = True
            contador_dos = contador_dos + 1
    return resultado
    
    pass


def armar_cadena(cadena):
    """
    Pide y arma una cadena con los caracteres pedidos.
    """
    cantidad = len(cadena) -1
    numero = 0
    cadena_armada = []
    while numero <= cantidad:
        letra = cadena[numero]
        cadena_armada.append(letra)
        numero = numero + 1
    return cadena_armada
    
    pass

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese una linea o cadena de texto para analizar: ")
    cadena_armada = armar_cadena(cadena) #Llama a armar_cadena para armar una.
    contador = 1
    while contador > 0:
        segundo = input("Ingrese el tipo de simbolo que desea buscar para que abra: ")
        primero = input("Ingrese el tipo de simbolo que desea buscar para que cierre: ")
        print("El sigueinte mensaje indicara con un True si estan cerrados o un False si no lo esta.")
        resultado = corchetes_balanceados(cadena_armada, segundo, primero) #Revisa si el texto enviado tiene los simbolos balanceados.
        print (f"{resultado}")
        respuesta = int(input("Ingrese 0 si no desea buscar ningun otro simbolo: "))
        if respuesta == 0:
            contador = 0

    pass


if __name__ == "__main__":
    principal()

if __name__ == "__main__":
    armar_cadena()
    
if __name__ == "__main__":
    corchetes_balanceados()