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

Una buena forma para verificar este ejercicio es codificar y 
decodificar un texto y compararlo con lo que fué ingresado originalmente.

**Tip**: Implementar las funciones utilizando las funciones `ord` y `chr`.
"""

#####
def codificacion_numeracion(texto, desplazamiento):
    cifrado = (" ", ".", ",",":","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    numero_de_cifrado = len(cifrado) -1 #El numero de caracteres del cifrado.
    numero_de_texto = len(texto) -1 #El numero de caracteres del texto.
    desplazamiento = int(desplazamiento)
    
    lista = conversor_caracteres_numeros(cifrado) #La lista del cifrado en numeros.
    lista_de_numeros_de_caracteres_cifrado = lista #Guarda la lista de numeros identica a la del cifrado.
    
    lista = conversor_caracteres_numeros(texto)
    lista_de_numeros_de_textos = lista #Guarda una lista con una cantidad de numeros igual al texto ingresado.
   
    nuevo_orden = [] #Guarda la transformación del texto a el numero de acuerdo a la pocicion de la letra en el cifrado.
    orden_medio = [] #Convertido a numero después de que se le sume el desplamamiento.
    orden_final = [] #Convertido en letra nuevamente.
    contador = 0
    contador_cifrado = 0
    """
    Esta parte de a continuación lo transforma a numero.
    """
    while contador <= numero_de_texto: #Mientras la cantidad de caracteres que tiene el texto no se termine de pasar esto sigue.
        if texto[contador] == cifrado[contador_cifrado]:
            comparacion = lista_de_numeros_de_caracteres_cifrado[contador_cifrado]
            caracter_convertido_numero = comparacion
            nuevo_orden.append(caracter_convertido_numero)
            contador = contador + 1
            contador_cifrado = 0
        else:
            contador_cifrado = contador_cifrado + 1 #Esto desplaza el numero del cifrado al siguiente caracter. 
    """
    La parte que sigue aumenta el numero de la lista de acuerdo para donde se lo quiera desplazar.
    """
    contador_suma = 0 #Otro contador para que pase todo el texto.
    while contador_suma <= numero_de_texto:
        mover = nuevo_orden[contador_suma]
        mover = mover + (desplazamiento)
        orden_medio.append(mover)
        contador_suma = contador_suma + 1
    """
    Esta parte vuelve a transformarlo en texto de acuerdo al cifrado.
    """
    contador_cambio = 0
    contador_cambio_cifrado = 0
    while contador_cambio <= numero_de_texto:
        numero_final = orden_medio[contador_cambio]
        """
        En lo que sigue revisa si el numero final resulta ser mas grande que el numero
        total del cifrado. En caso de serlo, le resta el numero total.
        """
        if numero_final > numero_de_cifrado or numero_final < 0:
            if numero_final > numero_de_cifrado:
                numero_final = numero_final - numero_de_cifrado
                numero_final = numero_final - 1
            elif numero_final < 0:
                numero_final = (numero_final + numero_de_cifrado)
                numero_final = numero_final - 1
                
        comparacion = lista_de_numeros_de_caracteres_cifrado[contador_cambio_cifrado]        
        if numero_final == comparacion:
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
    contador = 1
    while contador < cantidad:
        numero = contador
        lista_de_numeros.append(numero)
        contador = contador + 1
    return lista_de_numeros    
    
    pass
#####


def codificacion_numeracion(texto, desplazamiento):
    numero_letras_texto = len(texto) -1
    #orden_final = []
    contador = 0
    orden_final = ""
    while contador <= numero_letras:
        invocacion = texto[contador]
        numero = ord(invocacion) #Transforma la letra en numero
        numero = numero + desplazamiento #Le suma el numero de desplazamiento.
        numero = chr(numero)
        orden_final = orden_final + numero
        #orden_final.append(numero)
        contador = contador + 1
    print (F"Y asi queda: {orden_final}")
    return orden_final

    pass

def conversor():
    

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
    
if __name__ == "__main__":
    codificacion_numeracion(texto, desplazamiento)