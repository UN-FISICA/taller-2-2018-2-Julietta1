# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:35:27 2018

@author: salvi
"""
import math as m
from turtle import *

N=int(input("Digite el número de lados del polígono:  "))
n=int(input("Digite el numero de lados del polígono de alineación:  "))
title("Ejercicio 3")
screensize(4000,4000)
speed("fastest")
hideturtle()
if (n<=2):
    print ("Error, un polígono debe tener al menos 3 lados")
a=180-((n-2)*180)/n
b=180-((N-2)*180)/N
penup()
f=m.radians(180/n)
apotema=200/(2*m.tan(f))
goto(100,-apotema)
for i in range(n):
    penup()
    left(a)
    fd(200)
    seth(0)
    pendown()
    for j in range(N):
        left(b)
        fd(30)
    seth(a*(i+1))
 
done()
