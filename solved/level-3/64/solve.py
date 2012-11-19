#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from fractions import Fraction
import math

# on every level a+k(sqrt+b)/d

fields=["a", "k", "b", "d", "number"]
FractionLevel=namedtuple("FractionLevel", fields)

def nextLevel(fractionLevel):
    f=fractionLevel
    a=int(math.floor(f.k*(math.sqrt(f.number)+f.b)/f.d))
    if (f.number==a*a):
        raise Exception("Full square: "+str(f.number))
    minusB=f.b-a*f.d*f.k
    naiveD=f.k*(f.number-minusB**2)
    naiveK=f.d
    b=-minusB
    kd=Fraction(naiveK, naiveD)
    k=kd.numerator
    d=kd.denominator
    return FractionLevel(a, k, b, d, f.number)

def calculateSquareFraction(number):
    fractionLevel=FractionLevel(0, 1, 0, 1, number)
    levels=[]
    while True:
        fractionLevel=nextLevel(fractionLevel)
        if fractionLevel in levels:
            position=levels.index(fractionLevel)
            onlyA=lambda e: e.a
            prefix=map(onlyA, levels[:position])
            period=map(onlyA, levels[position:])
            return (prefix, period)
        else:
            levels.append(fractionLevel)

upperLimit=10000
squares=set(i*i for i in range(0, upperLimit+1))
result=0
for i in range(0, upperLimit+1):
    if (not i in squares):
        notation=calculateSquareFraction(i)
        if (1==len(notation[1])%2):
            result+=1
print result
