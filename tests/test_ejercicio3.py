################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import separar_caracteres
from src.ejercicio3 import superposicion_lugar
from src.ejercicio3 import superposicion_cantidad
from src.ejercicio3 import superposicion


"""
Este test pone a prueba a las 4 funciones que principal llama. Las evalua con datos ya sabidos y espera los resultados.
"""


def test_superposicion():
    """
    Comprueba si puede mostrar en que punto dos cadenas no coinciden.
    """
    uno = "nobatman"
    dos = "sibatman y robin"
    comparación = ([0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    fallos = superposicion(uno, dos)
    assert isinstance(fallos, list), "Devuelve el tipo de dato corresto: list."
    assert comparación == fallos, "Devuelve el orden indicado en donde se superponen y en donde no lo hacen."

    
    pass

def test_superposicion_lugar():
    """
    Prueba si la función indica a partir de donde se superponen adecuadamente.
    """
    uno = "El joker es rico"
    dos = "Y batman es rico"
    comparacion = 8 
    fallos = superposicion_lugar(uno, dos)
    assert isinstance(fallos, int), "El numero devuelto es del tipo correcto: int"
    assert comparacion == fallos, "Indica correctamente a partir de que linea se superposicionan."

    pass

def test_superposicion_cantidad():
    """
    Prueba si la funcion cuenta adecuadamente la cantidad de letras superpuestas.
    """
    uno = "un hombre sabio le teme a tres cosas: una noche sin luna, un tormenta en el mar, y la ira de un hombre amable"
    dos = "un hombre sabio le teme a tres cosas: alemania en la final, olvidar descongelar el pollo, y a una moto en la noche"
    resultado = ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    fallos = superposicion_cantidad(uno, dos)
    assert isinstance(fallos, list), "La función devuelve el tipo de dato correcto."
    assert resultado == fallos, "El resultado devuelto por la función es el esperado para los datos ingresados."
    
    pass

def test_separar_caracteres():
    """
    Prueba si lac función consigue separa por caracteres una linea.
    """
    primera = ("Soy batman")
    comparación = (['S', 'o', 'y', ' ', 'b', 'a', 't', 'm', 'a', 'n'])
    orden = separar_caracteres(primera)
    assert isinstance(orden, list), "Consigue separar la linea y devolverla en un list."
    assert comparación == orden, "Consigue separar la palabra como debería hacerlo."
    
    pass

