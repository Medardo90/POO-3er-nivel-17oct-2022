# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:39:36 2022

@author: lab
"""
"crear un  objeto = es instanciar a la clase, llamar a la clase"
#parentesisi = metodo no poner en variabñles
#significa creaar nuestro propio dtipo de dato

class Dog():
    pass
    def __init__(self):
        self.color="negro"
        
# perro.makeSound()

# vaca=Cow()
# vaca.makeSound()

# lobo = Wolf()
# lobo.makeSound()
        
a=5
print(type(a))
lista_int=[2,3,4]
perro_firulais= Dog()
print("perro Firulais:", perro_firulais.color)

perro_pelusa= Dog()
print("perro pelusa :", perro_pelusa.color)
# print(type(perro))




lista_dogs =[Dog(), Dog()]
# perr= Dog
# print([lista_dogs])