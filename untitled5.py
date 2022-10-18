# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:40:46 2022

@author: lab
"""

class Rueda:
    def __init__(self, color,marca):
        self.color= color
        self.marca =marca 

class Vehiculo:
    def __init__(self,numruedas):
        self.numruedas= numruedas
        
    def incorporarrueda(self):
        ruedas=[]
        ruedas.append(Rueda("negra","amarilla"))
        ruedas.append(Rueda("roja","continetal"))
        ruedas.append(Rueda("amarilla","gy"))
        ruedas.append(Rueda("roja","hamkot"))
        return  ruedas
    
    def generarRuedas(self):
        ruedas=[]
        for i in range(0, self.numruedas):
            ruedas
       