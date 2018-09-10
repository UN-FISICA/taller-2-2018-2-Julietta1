# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:52:03 2018

@author: salvi
"""

from turtle import *
b=int(input("Número de filas de la pirámide: "))
a=3

title("Ejercicio 5")
screensize(4000,4000)
speed("fastest")
hideturtle()
penup()
sety(200)
setx(-10)
p=1
for j in range(b):
    n=180-((a-2)*180)/a
    sety(200-(6*a*j))
    setx(-10-(5*a*j))   
    for k in range(p):
        setx(-10-(5*a*j)+(10*a*k))    
        for i in range(a):
                pendown()
                left(n)
                fd(20)
                penup()
    a+=1       
    p+=1
done()    