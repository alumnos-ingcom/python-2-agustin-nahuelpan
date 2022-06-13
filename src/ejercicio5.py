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

def corchetes_balanceados(cadena_armada, simbolos_regreso):
    """
    Revisa si los caracteres indicados estan balanceados.
    """
    resultado = [] #Una lista para devolver los resultados de la operación.
    numero_revision = len(cadena_armada) -1 #Un contador del numero de caracteres en la cadena de texto y poder revirla.
    simbolos_revision = len(simbolos_regreso) -1 #Un contador de la cantidad de simbolos para varios usos.
    contador_numero_de_signo = 0 #Para ver que numero de signo es el actual.
    while simbolos_revision >= 0: #Cuando no quedan simbolos para revisar el programa termina.
        suma=contador_numero_de_signo
        #suma= suma + 1 #Para identificar al numero siguiente que sería el primer signo (pricipalmente para que quede agradable a la vista en la devolución, es decir, así (),y no así: )()
        if contador_numero_de_signo == 0: # None: #simbolos_regreso(suma):
            #simbolos_regreso[suma]
            agregado = simbolos_regreso[suma]
            resultado.append(agregado) #Guarda en la variable de salida el primer valor.        
        contador_simbolo = 1 #Controla el while de abajo.
        contador_revision = 0 #Ve en que numero de la cadena de texto, de izquierda a derecha, esta revisando.
        while contador_simbolo > 0:
            #cadena_armada[contador_revision] #Invica un caracter de la cadena ingresada.
            
            if simbolos_regreso[contador_numero_de_signo] == cadena_armada[contador_revision]: #Revisa si el caracter ingresado se corresponde con un caracter de la cadena.
                contador_simbolo_contrario = contador_revision #Asigna el valor a partir del lugar en donde lo encotntro para empezar a retroceder buscando el caracter que lo cierra.
                if contador_numero_de_signo ==  0: #simbolos_regreso(contador_numero):
                    suma = suma + 1
                    agregado = simbolos_regreso[suma]
                    resultado.append(agregado) #Guarda en la variable de salida el proximo valor
                while contador_simbolo_contrario >= 0: #Empieza a revisar los numeros ya registrados buscando el contrario.
                    comparacion = cadena_armada[contador_simbolo_contrario]
                    comparación_dos = suma 
                    if comparacion == comparación_dos:
                    #if cadena_armada[contador_simbolo_contrario] == simbolos_revision[suma]: #Compara si el numero anterior de la lista es igual al siguiente de los simbollos. Es decir, el que cierra el signo.
                        cadena_armada[contador_simbolo_contrario] = " " #Elimina el numero ya contado de la cadena
                        if contador_revision == numero_revision: #Si el numero de caracteres recorridos de la cadena son todos los caracteres.
                            contador_simbolo = 0
                            contador_numero_de_signo = contador_numero_de_signo + 1
                            simbolos_revision = contador_revision - 2 #Termina con el conteo del primer caracter de los que quiere buscar.
                            contodar_simbolo_contrario = -1
                            if simbolos_revision == 0: #Si los caracteres que quiere buscar se terminan, determina el resultado como uno verdadero.
                                resultado.append("true")
                    contador_simbolo_contrario = contador_simbolo_contrario - 1
                    if contador_simbolo_contrario == -1: #Si no se encuentra un caracter que cierre para cuando se termina de revisar la cadena, entonces asigna un valor negativo.
                        resultado.append(False)
                        contador_simbolo = 0
                        contador_numero_de_signo = contador_numero_de_signo + 1
                        simbolos_revision = simbolos_revision - 2
                    
            contador_revision = contador_revision + 1
    return resultado
    
    pass

def armar_cadena(cadena):
    """
    Pide y arma una cadena con los caracteres pedidos.
#    """
    #cadena = input("Ingrese una linea o cadena de texto para analizar.")
    cantidad = len(cadena) -1
    numero = 0
    cadena_armada = []
    while numero <= cantidad:
        letra = cadena[numero]
        cadena_armada.append(letra)
        numero = numero + 1
    return cadena_armada
    
    pass


#def simbolos():
#    """
#    Pide que ingresen el simbolo o los simbolos que buscar en el programa.
#    """
#    simbolos_regreso = []
#    contador = 1
#    while contador > 1:
#        segundo = input("Ingrese el tipo de simbolo que desea buscar para que abra(ejemplo: "<" ): ")
#        primero = input("Ingrese el tipo de simbolo que desea buscar para que cierre(ejemplo: ">"): :")
#        simbolos_regreso.append(segundo)
#        simbolos_regreso.append(primero)
#        respuesta = int(input("Ingrese 0 si no desea buscar ningun otro simbolo."))
#        if respuesta == 0:
#            contador = 0
#    return simbolos_regreso

    #simbolos = 0
    #while simbolos < 3: #Convierte lo ingresado en un solo simbolo, que sera lo utilizado por otra función.
    #    simbolos_regreso[simbolos]
    #    if simbolos_regreso[simbolos] == "()":
    #        #")" = simbolos_regreso[simbolos]
    #        simbolos_regreso[simbolos] = ")"
    #        simbolos = simbolos + 1
    #    elif simbolos_regreso[simbolos] == "{}":
    #        #"}" = simbolos_Rergreso[simbolos]
    #        simbolos_regreso[simbolos] = "}"
    #        #simbolos = simbolos + 1
    #        simbolos = simbolos + 1
    #    elif simbolos_regreso[simbolos] == "[]":
    #        #"]" = simbolos_regreso[simbolos]
    #        simbolos_regreso[simbolos] = "]"
    #        simbolos = simbolos + 1
    #return simbolos_regreso
    
    pass

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese una linea o cadena de texto para analizar: ")
    cadena_armada = armar_cadena(cadena) #Llama a armar_cadena para armar una.
    
    simbolos_regreso = []
    contador = 1
    while contador > 0:
        segundo = input("Ingrese el tipo de simbolo que desea buscar para que abra: ")
        primero = input("Ingrese el tipo de simbolo que desea buscar para que cierre: ")
        simbolos_regreso.append(segundo)
        simbolos_regreso.append(primero)
        respuesta = int(input("Ingrese 0 si no desea buscar ningun otro simbolo: "))
        if respuesta == 0:
            contador = 0
    #simbolos_regreso = simbolos() #Llama a simbolos para determinar que buscar.
    resultado = corchetes_balanceados(cadena_armada, simbolos_regreso) #Revisa si el texto enviado tiene los simbolos balanceados.
    
    print(f"El resultado de la operación marca con True cuando los simbolos estan cerrrados, y con False cuando no lo están: {resultado}")
    
    #que_devolver = len(resultado) #Para saber cuantos resultados hubieron.
    #if que_devolver == 3:
    #    print (f"El simbolo {armar_cadena[0]} es {resultado[0]}. El simbolo{armar_cadena[1]} es {resultado[1]}. Y el simbolo {armar_cadena[2]} es {resultado[2]}.")
    #if que_devolver == 2:
    #    print (f"El simbolo {armar_cadena[0]} es {resultado[0]}. Y el simbolo{armar_cadena[1]} es {resultado[1]}.")
    #if que_devolver == 1:
    #    print (f"El simbolo {armar_cadena[0]} es {resultado[0]}.")

    pass


if __name__ == "__main__":
    principal()

if __name__ == "__main__":
    armar_cadena(cadena)
    
if __name__ == "__main__":
    corchetes_balenceados()
    
#if __name__ == "__main__":
#    simbolos(regreso)
