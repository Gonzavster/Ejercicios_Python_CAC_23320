# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:23:22 2023

@author: gvallejo
"""

"""
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construya los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que
validar las entradas de datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor
de edad.
"""

class Persona:
    def __init__(self, nombre="", edad=0, dni=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    @property
    def nombre(self): 
        return self._nombre
    
    @property
    def edad(self): 
        return self._edad
    
    @property
    def dni(self): 
        return self._dni
       
    @nombre.setter
    def nombre(self, value):
        special_characters = "!@#$%^&*()-+?_=,<>/"
        numbers = "1234567890"
        error_nombre = "El nombre debe ser una cadena de texto sin numeros o caracteres especiales"
        if not isinstance(value, str):
            raise ValueError(error_nombre, "El valor no es una cadena de texto")
        elif any(c in special_characters for c in value):
            raise ValueError(error_nombre, "Se han ingresado caracteres especiales en el nombre")
        elif any(c in numbers for c in value):
            raise ValueError(error_nombre, "Se han ingresado numeros en el nombre")
        self._nombre = value
        
    @edad.setter
    def edad(self, value):
        error_edad = "La edad debe ser un numero entero positivo, menor a 150"
        if not isinstance(value, int):
            raise ValueError(error_edad, "La edad ingresada no es un numero entero")
        elif value < 0:
            raise ValueError(error_edad, "La edad no puede ser negativa")
        elif value >= 150:
            raise ValueError(error_edad, "La edad no puede ser mayor a 150")
        self._edad = value
        
    @dni.setter
    def dni(self, value):
        error_dni = "El DNI debe ser un numero entero de 7 u 8 dígitos"
        if not isinstance(value, int):
            raise ValueError(error_dni, "El valor ingresado no es un numero entero")
        elif (len(str(value)) < 7 or len(str(value)) > 8) and value != 0:
            raise ValueError(error_dni, "El DNI debe tener 7 u 8 dígitos")
        self._dni= value
       
    def mostrar(self):
        print("Nombre: {}".format(self._nombre))
        print("Edad: {}".format(self._edad))
        print("DNI: {}".format(self._dni))
        return(["Nombre: {}".format(self._nombre), "Edad: {}".format(self._edad), "DNI: {}".format(self._dni)])
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False