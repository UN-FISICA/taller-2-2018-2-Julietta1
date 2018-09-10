# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:20:13 2018

@author: salvi
"""

from turtle import *
import math as m
b=int(input("Número de filas de la pirámide: "))
a=3
title("Ejercicio 6")
screensize(4000,4000)
speed("fastest")
hideturtle()
penup()
sety(200)
setx(-10)
p=1
r=30
for j in range(b):
    s=2*r*m.sin(m.radians(180/a))
    apotema=s/(2*m.tan(m.radians(180/a)))
    n=180-((a-2)*180)/a
    sety(200-(2.5*r*j))
    setx(-(apotema/2)-(2*apotema*j))   
    for k in range(p):
        setx(-(apotema/2)-(2.5*apotema*j)+(5*apotema*k))    
        for i in range(a):
                pendown()
                left(n)
                fd(s)
                penup()
    a+=1       
    p+=1
done()   