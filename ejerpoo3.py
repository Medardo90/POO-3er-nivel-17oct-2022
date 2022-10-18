# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:27:46 2022

@author: lab
"""
"""heerencia"""

class A():
    def __init__(self):
        self.a= "a"

class B(A):
    def __init__(self):
        A .__init__(self)
        self.b="b"

ob_b= B()
print("aa: ",ob_b.a , "bb: ", ob_b.b)

class C(B):
    def __init__(self):
        B .__init__(self)
        self.c ="c"
        
        
ob_c= C()
print("aa: ", ob_c.a ,"bb: ", ob_c.b, "cc: ",ob_c.c)




