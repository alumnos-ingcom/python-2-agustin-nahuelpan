################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import fibonacci

"""
Este test revisa que se este haciendo la cuenta adecuadamente comparandolo con el resultado ya sabido.
"""


def test_fibonacci():
    """
    Compara el resultado de la función con el resultado real de la suma de fibonacci.
    """
    numero = 16
    resultado = 2584
    regreso = fibonacci(numero)
    assert isinstance(regreso, int), "La función regresa el tipo de dato correcto. Int"
    assert resultado == regreso, "El resultado es el adecuado para el numero 16 en la fila de numeros de fibonacci."
    
    pass