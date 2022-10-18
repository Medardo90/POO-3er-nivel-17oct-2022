# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:25:44 2022

@author: lab
"""

class Dog:
    pass
    def __init__(self):
        self.raza = "Paztor aleman"
        
perros = [Dog(),Dog()]
print(perros[0].raza)


# """2"""
 
class Dog:
    pass
    def __init__(self, raza):
        self.raza = raza
        
        
perros = [Dog("pastor aleman"),Dog("pitbull")]
print(perros[1].raza)
print(perros[0].raza)

#puedo crear un objeto aparte para crear una espacio de menoria oar autlizalrlo mas adelante 
#vector de objetos

class Dog:
    pass
    def __init__(self, raza):
        self.raza = raza
        
        
perros1 = Dog("pastor aleman")
perros2 = Dog("pitbul")

dogs =[perro1, perro2]
print(dogs[1].raza)

dogs[1].raza="mestizo"
print(dogs[1].raza)


class Dog:
    pass
    def __init__(self, raza):
        self.raza = raza
        
        
       











