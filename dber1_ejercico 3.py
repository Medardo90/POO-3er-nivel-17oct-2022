# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:03:46 2022

@author: Patricio Haro
"""
print("      *********** BUENOS DIAS ESTIMADO CLIENTE ***********\n")
print("                ------ MENU DE PRODUCTOS ------\n")
print("                  [dfsadf, aasdfdasf, asfdsf,]")

class MaquinaExpendedora:
    pass
    def __init__(self):#, codigo, datos):#, precio, nombre):
        # self.c_p = codigo
        # self.precio_p= precio
        # self.nombre_p= nombre 
        # self.prod1=producto1
        # self.dato = datos     # [0 for i in range(codigo)]#, precio, nombre)]
        
    def ingresodatos(self):
        self.datos = int(input("ingrese el codigo del producto:"))
        # if datos == datos:
        #     print("codigo ", codigo)
        #     print("nombre ",nombre )
        # else:
        #     print("codigo incorrecto" )
                         
     
class Cliente(MaquinaExpendedora):
    pass
    def __init__(self):
        MaquinaExpendedora .__init__(self,1)
        
    def ci(self):
        self.identificacion= int(input("ingrese numero de cedula:"))
    def name(self):
        self.nombre= int(input("ingrese nmnbre:"))
        
        
vender=MaquinaExpendedora()
print(vender.ingresodatos())
        
        
        
        
        
        
        
