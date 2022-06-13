################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una encriptación de 
sustitución simple. Esto significa que cada caracter se sustituye 
por otro caracter de acuerdo con un sistema especifico. 

La codificación debe ser tal que la palabra codificada contenga 
unicamente caracteres del tipo AZaz y 0 a 9, de manera que al 
codificar las ultimas letras del abecedario se vuelva a las primeras letras.

**Por ejemplo**, el método conocido y muy utilizado ROT13 rota 
el alfabeto con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

* Implementar una funcion que codifique un texto rotandolo 
una cantidad de posiciones ajustable.

* Implementar la funcion que decodifique el texto rotado una 
cantidad de posiciones ajustable.

Una buena forma para verificar este ejercicio es codificar y 
decodificar un texto y compararlo con lo que fué ingresado originalmente.

**Tip**: Implementar las funciones utilizando las funciones `ord` y `chr`.
"""

def codificacion_numeracion(texto, desplazamiento):
    cifrado = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    numero_de_cifrado = len(cifrado) -1 #El numero de caracteres del cifrado.
    numero_de_texto = len(texto) -1 #El numero de caracteres del texto.
    
    lista = conversor_caracteres_numeros(cifrado) #La lista del cifrado en numeros.
    lista_de_numeros_de_caracteres = lista #Guarda la lista de numeros identica a la del cifrado.
    
    lista = conversor_caracteres_numeros(texto)
    lista_de_numeors_de_textos = lista #Guarda una lista con una cantidad de numeros igual al texto ingresado.
   
    nuevo_orden = []
    orden_final = []
    contador = 0
    contador_cifrado = 0
    while contador <= numero_de_texto:
        if texto[contador] == cifrado[contador_cifrado]:
            comparacion = lista_de_numeros[contador_cifrado]
            caracter_convertido_numero = comparacion
            nuevo_orden.append(caracter_convertido_numero)
            contador = contador + 1
            contador_cifrado = 0
        else:
            contador_cifrado = contador_cifrado + 1    
    contador_suma = 0
    while contador_suma >= numero_de_texto:
        nuevo_orden[contador_suma] = nuevo_orden[contador_suma] +(desplazamiento)
        contador_suma = contador_suma + 1
    contador_cambio = 0
    contador_cambio_cifrado = 0
    while contador_cambio >= numero_de_texto:
        numero_final = nuevo_orden[contador_cambio]
        if numero_final > numero_de_cifrado:
            numero_final = (numero_final - numero_de_cifrado) - 1
        elif numero_final < numero_de_cifrado:
            numero_final = (numero_final + numero_de_cifrado) + 1
        
        if numero_final == lista_de_numeros[contador_cambio_cifrado]:
            orden = cifrado[contador_cambio_cifrado]
            orden_final.append(orden)
            contador_cambio = contador_cambio + 1
        else:
            contador_cambio_cifrado = contador_cambio_cifrado + 1
            
    return orden_final
    
    pass

def conversor_caracteres_numeros(lista):
    cantidad = len(lista) -1
    lista_de_numeros = []
    contador = 0
    while contador > cantidad:
        numero = lista[contador]
        lista_de_numeros.append(numero)
        contador = contador + 1
    return lista_de_numeros    
    
    pass

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = input("Ingrese un texto para convertir: ")
    desplazamiento = int(input("Ingrese cuantas casillas lo quiere correr(numero positivo = derecha; numero negativo = izquierda): "))
    orden_final = codificacion_numeracion(texto, desplazamiento)
    print (f"El orden del texto: {texto} queda así {orden_final}")
    
    pass


if __name__ == "__main__":
    principal()
    conversor_caracteres_numeros(cifrado)
    codificacion_numeracion(texto, desplazamiento)

