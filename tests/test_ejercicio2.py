################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import estadisticas

"""
Este test comprueba que el el proceso funcione bien y devuelva los numeros correctos. Es decir, el maximo, el minimo, y el promedio.
"""


def test_estadistica():
    """
    De antemano se sabe el resultado y se lo compara con lo que devuelve la función. En caso de ser igual, se sabra que la función trabaja bien.
    """
    secuencia = (2, 6, 18, 26, 76, 20, 3, 9, 47, 60)
    comparación = (76, 2, 26.7)
    devolver = estadisticas(secuencia)
    assert isinstance(devolver, tuple), "El tipo de dato devuelto es correcto. La función devuelve una tupla."
    assert devolver == comparación, "La función devuelve la tupla con los numeros correctos en el orden correcto."
    
    pass