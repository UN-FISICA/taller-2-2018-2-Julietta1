# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 22:21:53 2018

@author: salvi
"""

from turtle import *
a=int(input("Número de lados del polígono: "))
b=int(input("Número de filas de la pirámide: "))
title("Ejercicio 4")
screensize(4000,4000)
speed("fastest")
hideturtle()
n=180-((a-2)*180)/a
penup()
sety(200)
setx(-10)
p=1
for j in range(b):
    sety(200-(6*a*j))
    setx(-10-(6*a*j))   
    for k in range(p):
        setx(-10-(6*a*j)+(12*a*k))    
        for i in range(a):
                pendown()
                left(n)
                fd(20)
                penup()
    p+=1
done()       