# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:23:31 2022

@author: lab
"""

# perros=[]

# for i in range (3):
#   perros.append(3)
  
class Dog:
    def __init__(self, raza,color):
        self.raza = raza
        self.color = color 
        
perros=[]

for i in range (3):
    razaD= input("in : ")
    perros.append(Dog(razaD,"b"))
   
for i in range (len(perros)):
    print("raza", perros [i].raza)
    print("color", perros[i].color)
