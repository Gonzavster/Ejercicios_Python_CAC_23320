# -*- coding: utf-8 -*-
"""
@author: gvallejo

Casos de test y funciones de testing para cada ejercicio
"""
from ejercicio1 import mcd
from ejercicio2 import mcm
from ejercicio3 import word_counter
from ejercicio4 import most_frequent
from ejercicio5 import get_int
from ejercicio6 import Persona


#Casos de test para Eejercicios 1 y 2 con formato [numero, numero, mcd, mcm]
casos_e1_e2 = {"caso1" : [50, 72, 2, 1800], "caso2" : [18, 22, 2, 198],\
               "caso3" : [18, 24, 6, 72], "caso4" : [2345, 5432, 7, 1819720]}

#Casos de test para Eejercicio3
casos_e3 = {"caso1": "uno dos tres cuatro dos tres cuatro tres cuatro cuatro"}
salidas_esperadas_e3 = {"caso1" : {"uno" : 1, "dos" : 2, "tres" : 3, "cuatro": 4}}

#Casos de test para Eejercicio4
#Se utilizan casos_e3
salidas_esperadas_e4 = {"caso1" : ("cuatro", 4)}

#Casos de test para Ejercicio6
casos_e6 = {"caso1" : ["", 0, 0],\
            "caso2" : ["Juan Perez", 17, 33333333],\
            "caso3" : ["John Doe", 18, 22222222],\
            "caso5" : [1234, "Juan$1", "Juan1"],\
            "caso6" : ['veinticinco', -3, 151],\
            "caso7" : ["1234", 123456, 123456789]}
    
salidas_esperadas_e6 = {"caso5" : ["El nombre debe ser una cadena de texto sin numeros o caracteres especiales",\
                        "El valor no es una cadena de texto",\
                        "Se han ingresado caracteres especiales en el nombre",\
                        "Se han ingresado numeros en el nombre",],
                        "caso6": ["La edad debe ser un numero entero positivo, menor a 150",\
                        "La edad ingresada no es un numero entero",
                        "La edad no puede ser negativa",
                        "La edad no puede ser mayor a 150"],\
                        "caso7" : ["El DNI debe ser un numero entero de 7 u 8 dígitos",\
                        "El valor ingresado no es un numero entero",
                        "El DNI debe tener 7 u 8 dígitos",
                        "El DNI debe tener 7 u 8 dígitos"]}

def test_ej1():
    print("EJERCICIO 1 - Testing")
    for caso in casos_e1_e2:
        if mcd(casos_e1_e2[caso][0], casos_e1_e2[caso][1]) == casos_e1_e2[caso][2]:
            print(caso, "PASSED")
        else:
            print(caso, "FAILED")
    print()

def test_ej2():
    print("EJERCICIO 2 - Testing")
    for caso in casos_e1_e2:
        if mcm(casos_e1_e2[caso][0], casos_e1_e2[caso][1]) == casos_e1_e2[caso][3]:
            print(caso, "PASSED")
        else:
            print(caso, "FAILED")
    print()

def test_ej3():
    print("EJERCICIO 3 - Testing")
    for caso in casos_e3:
        test_e3 = word_counter(casos_e3[caso])
        if isinstance(test_e3, dict):
            print("Datatype PASSED")
        else:
            print("Datatype FAILED")          
        if test_e3 == salidas_esperadas_e3[caso]:
            print(caso, "PASSED")
        else:
            print(caso, "FAILED")
    print()

def test_ej4():
    print("EJERCICIO 4 - Testing")
    for caso in casos_e3:
        test_e4 = most_frequent(word_counter(casos_e3[caso]))
        if isinstance(test_e4, tuple):
            print("Datatype PASSED")
        else:
            print("Datatype FAILED")   
        if test_e4 == salidas_esperadas_e4[caso]:
            print(caso, "PASSED")
        else:
            print(caso, "FAILED")
    print()

def test_ej5():
    print("EJERCICIO 5 - Testing")
    print("Testing Manual. Los valores a ingresar son:")
    print("1- 'uno'")
    print("2- 5.6")
    print("3- 7")
    get_int()

def test_ej6():
    print("EJERCICIO 6 - Testing")
    #Chequeo de creación de persona sin datos iniciales.
    #Adicionalmente testea getters
    john_doe = Persona()
    if john_doe.nombre == casos_e6["caso1"][0] and\
        john_doe.edad == casos_e6["caso1"][1] and\
        john_doe.dni == casos_e6["caso1"][2]:
        print("caso1", "PASSED")
    else:
        print("caso1", "FAILED")

    #Chequeo de creación de persona con datos iniciales
    #Adicionalmente testea getters
    juan_perez = Persona("Juan Perez", 17, 33333333)
    if juan_perez.nombre == casos_e6["caso2"][0] and\
        juan_perez.edad == casos_e6["caso2"][1] and\
        juan_perez.dni == casos_e6["caso2"][2]:
        print("caso2", "PASSED")
    else:
        print("caso2", "FAILED")
        
    #Chequeo de setters
    john_doe.nombre = "John Doe"
    john_doe.edad = 18
    john_doe.dni = 22222222
    if john_doe.nombre == casos_e6["caso3"][0] and\
        john_doe.edad == casos_e6["caso3"][1] and\
        john_doe.dni == casos_e6["caso3"][2]:
        print("caso3", "PASSED")
    else:
        print("caso3", "FAILED")

    #Chequeo de método es_mayor_de_edad()
    if juan_perez.es_mayor_de_edad() == False and\
        john_doe.es_mayor_de_edad() == True:
        print("caso4", "PASSED")
    else:
        print("caso4", "FAILED")

    #Verificación de validaciones atributo nombre"
    test_e6 = []
    for nombre in casos_e6["caso5"]:
        try:
            john_doe.nombre = nombre
        except ValueError as e:
            test_e6.append(str(e))
    for i in range(len(test_e6)):
        if test_e6[i] == "('" + salidas_esperadas_e6["caso5"][0] +"', '" + salidas_esperadas_e6["caso5"][i+1] + "')":
            print("caso5.{} PASSED".format(i+1))
        else:
            print("caso5.{} FAILED".format(i+1))
            
    #Verificación de validaciones atributo edad"
    test_e6 = []
    for edad in casos_e6["caso6"]:
        try:
            john_doe.edad = edad
        except ValueError as e:
            test_e6.append(str(e))
    for i in range(len(test_e6)):
        if test_e6[i] == "('" + salidas_esperadas_e6["caso6"][0] +"', '" + salidas_esperadas_e6["caso6"][i+1] + "')":
            print("caso6.{} PASSED".format(i+1))
        else:
            print("caso6.{} FAILED".format(i+1))

    #Verificación de validaciones atributo dni"
    test_e6 = []
    for dni in casos_e6["caso7"]:
        try:
            john_doe.dni= dni
        except ValueError as e:
            test_e6.append(str(e))
    for i in range(len(test_e6)):
        if test_e6[i] == "('" + salidas_esperadas_e6["caso7"][0] +"', '" + salidas_esperadas_e6["caso7"][i+1] + "')":
            print("caso7.{} PASSED".format(i+1))
        else:
            print("caso7.{} FAILED".format(i+1))