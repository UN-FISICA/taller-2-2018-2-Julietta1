# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:09:10 2018

@author: salvi
"""

from turtle import *
title("Ejercicio 1")
hideturtle()
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
    for i in range(4):
        left(90)
        fd(70)
done()    
