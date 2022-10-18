# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:08:04 2022

@author: lab
"""

"""polimorfismo"""
""" tener un metodo con el mismo nombre pero se tiene difentes nombres"""
"simplicidad en llamr en los metosdos"

class Animal():
    def makeSound(self):
        print("Grrr....")
        
class Cat(Animal):
    def makeSound(self):
        print("MEOWW")
    
class Dog(Animal):
    def makeSound(self):
        print("woof")
        
class Cow(Animal):
    def makeSound(self):
        print("muuuuu ")
        
class Wolf(Animal):
    def makeSound(self):
        print("Auuuuu")
 

perro= Dog()   #creo una variable """   #instanciar es = a llamar ,
print(type(perro))
# perro.makeSound()

# vaca=Cow()
# vaca.makeSound()

# lobo = Wolf()
# lobo.makeSound()
        