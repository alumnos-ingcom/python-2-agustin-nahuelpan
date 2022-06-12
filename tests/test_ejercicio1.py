################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import principal

"""
Este test prueba que la función devuelve True con resultados numeros pares, tanto negativos como positivos, y false con impares, tanto negativos como positivos.
"""


def test_principal_positivo_par():
    """
    Prueba si la función sirve con numeros pares positivos.
    """
    numero = 8
    regreso = principal(numero) 
    assert isinstance(regreso, bool), "El tipo de devolución es correcta. Una expresión booleana."
    assert regreso == True, "La devolución correponde con el valor bolleano correcto. True."
    
    pass

def test_principal_positivo_impar():
    """
    Prueba si la función sirve con numeros pares positivos.
    """
    numero = 11
    regreso = principal(numero)
    assert isinstance(regreso, bool), "El tipo de devolución es correcta. Una expresión booleana."
    assert regreso == False, "La devolución correponde con el valor bolleano correcto. False."

    pass

def test_principal_negativo_par():
    """
    Prueba si la función sirve con numeros pares positivos.
    """
    numero = -20
    regreso = principal(numero)
    assert isinstance(regreso, bool), "El tipo de devolución es correcta. Una expresión booleana."
    assert regreso == True, "La devolución correponde con el valor bolleano correcto. True."
    
    pass

def test_principal_negativo_impar():
    """
    Prueba si la función sirve con numeros pares positivos.
    """
    numero = -17
    regreso = principal(numero)
    assert isinstance(regreso, bool), "El tipo de devolución es correcta. Una expresión booleana."
    assert regreso == False, "La devolución correponde con el valor bolleano correcto. True."
    
    pass