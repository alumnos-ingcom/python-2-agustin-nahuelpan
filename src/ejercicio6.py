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
def codificacion_numeracion(texto, desplazamiento):
    numero_letras = len(texto) -1
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