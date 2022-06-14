################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import armar_cadena
from src.ejercicio5 import corchetes_balanceados

"""
El test prueba que la función puede devolver los caracteres pedidos.
"""


def test_corchetes_balanceados():
    """
    Prueba si devuelve que multiples caracteres estan o no en el mismo texto.
    """
    cadena = ("I{} }(am) [batman][]a")
    cadena_armada = armar_cadena(cadena)
    segundo = ")"
    primero =  "("
    resultado_uno = True
    resultado = corchetes_balenceados(cadena_armada)
    resultado_uno_balanceo = resultado
    segundo = "}"
    primero = "{"
    resultado_uno = False
    resultado = corchetes_balenceados(cadena_armada)
    resultado_dos_balanceo = resultado
    segundo = "]"
    primero = "["
    resultado_uno = True
    resultado = corchetes_balenceados(cadena_armada)
    resultado_tres_balanceo = resultado
    assert resultado_uno == resultado_uno_balanceo, "El resultado es el correcto: True."
    assert resultado_dos == resultado_dos_balanceo, "El resultado es el correcto: False."
    assert resultado_tres == resultado_tres_balanceo, "El resultado es el correcto: True."
    
    pass