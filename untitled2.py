# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:53:32 2022

@author: lab
"""
class Dog:
    pass
    def __init__(self, raza,color):
        self.raza = raza
        self.color = color 
        
perros = [Dog("pastor aleman,", "cafe"),Dog("pitbull", "negro")]

for i in range (len(perros)):
    print("raza", perros [i].raza)
    print("color", perros[i].color)
# #lista =[4,4,6,6,7,5]
# for i in lista:
#     print(i)