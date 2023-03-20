# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:52:08 2023

@author: gvallejo

Ejercicio 5: Sabiendo que ValueError es la excepción que se lanza
cuando no podemos convertir una cadena de texto en su valor numérico,
escriba una función get_int() que lea un valor entero del usuario y
lo devuelva, iterando mientras el valor no sea correcto. Intente
resolver el ejercicio tanto de manera iterativa como recursiva.
"""

def get_int():
    
    """
    Función que lee un valor entero y lo devuelva,
    iterando mientras el valor no sea correcto.
    """
    x = input("Ingrese un numero entero:")
    try:
        num = int(x)
        print("El numero ingresado es", num)
    except ValueError:
        print("Ingresó {}, que no es un numero entero".format(x))
        get_int()