################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import codificacion_numeracion

"""
Este test transforma al texto, desplazandolo 20 a la derecha, y luego, lo regresa a
la normalidad volviendolo -20 a la izquierda.
"""


def test_codificacion_numeracion():
    """
    Prueba que el texto puede ser devuelto a la normalidad.
    """
    texto = "En un agujero en el suelo, vivia un hobbit. No era un agujero humedo, sucio, repugnante, con restos de gusanos y olor a fango, ni tampoco un agujero seco, desnudo y arenoso, sin nada en que sentarse o que comer: era un agujero hobbit, y eso significa comodidad."
    texto_uno = texto
    desplazamiento = 25
    orden_final =codificacion_numeracion(texto, desplazamiento)
    encriptado = orden_final
    texto = orden_final
    desplazamiento = -25
    orden_final =codificacion_numeracion(texto, desplazamiento)
    print(f"El texto entrado fue fue {texto_uno}. Despues de coficicarse quedo así: {encriptado}. Y finalmente volvio a quedar así {orden_final}.")
    assert texto_uno == orden_final, "La devolucion codificada es correcta"
    
    pass
