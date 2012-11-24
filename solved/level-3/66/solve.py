#!/usr/bin/env python
# -*- coding: utf-8 -*-

# see: http://en.wikipedia.org/wiki/Pell%27s_equation

import sys
sys.path.append("../lib")
from ContinuedFraction import *

def getNotationApproximation(notation, length):
    (prefix, period)=notation
    result=[]
    result+=prefix
    while (len(result)<length):
        result+=period
    return result[:length]

def isSolvingPellsEquation(D, x, y):
    return x**2-D*y**2==1

upperLimit=1000
squares=set(i*i for i in range(0, upperLimit+1))

solutions=[]

for D in range(2, upperLimit+1):
    if (D in squares):
        continue
    notation=calculateSquareFractionNotation(D)
    i=0
    while True:
        i+=1
        approximation=getNotationApproximation(notation, i)
        fraction=calculateFraction(approximation)
        x=fraction.numerator
        y=fraction.denominator
        if (isSolvingPellsEquation(D, x, y)):
            solution=(D, x, y)
            #print solution
            solutions.append(solution)
            break
        #print i, notation, approximation, fraction
print max(solutions, key=lambda e: e[1])[0]