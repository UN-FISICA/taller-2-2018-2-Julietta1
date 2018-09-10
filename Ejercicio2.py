# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:52:59 2018

@author: salvi
"""

from turtle import *
n=int(input("Digite el número de lados del polígono:  "))
title("Ejercicio 2")
screensize(1000,1000)
hideturtle()
if (n<=2):
    print ("Error, un polígono debe tener al menos 3 lados")
a=180-((n-2)*180)/n
pensize(3)
b=-1
c=-1
for j in range (4):
    penup()
    goto(b*200,c*200)
    pendown()
    if (j%2==0):
        b=b*-1
    else:
        c=c*-1
    for i in range(n):
        left(a)
        fd(30)
done()    

    
    
    

