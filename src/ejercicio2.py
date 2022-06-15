################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio de 
una secuencia con números, retornando los valores como una `tuple`.

Sin utilizar lazos `for` o las funciones integradas del lenguaje 
que procesan secuencias."""

# Reemplazar por las funciones del ejercicio

def estadisticas(secuencia):
    cantidad_numero_total = 0
    suma_total = 0
    maximo = 0
    minimo = 10000000000000000000000000
    orden = len(secuencia)-1 #El numero de los numeros en orden.
    while orden > -1:
        secuencia[orden]
        if secuencia[orden] > maximo:
            maximo = secuencia[orden]
        if secuencia[orden] < minimo:
            minimo = secuencia[orden]
        cantidad_numero_total = cantidad_numero_total + 1 #Para conseguir el promedio después.
        suma_total = suma_total + secuencia[orden] #Para dividir después.
        orden = orden - 1 
    promedio = suma_total / cantidad_numero_total
    devolver = (maximo, minimo, promedio)
    return devolver

    pass

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    secuencia = []
    mantenedor = 1 #Para mantener el bucle while.
    while mantenedor > 0:
        numero = int(input("Ingrese un numero a la lista: "))
        secuencia.append(numero)
        final = int(input("Ingrese un 0 si quiere terminar con la lista de numeros: "))
        if final == 0:
            mantenedor = 0
    print (f"{secuencia}")
    devolver = estadisticas(secuencia)
    print (f"La máxima, la mímima y el promedio de la seguencia de numeros ingresada es {devolver}")
    
    pass


if __name__ == "__main__":
    principal()