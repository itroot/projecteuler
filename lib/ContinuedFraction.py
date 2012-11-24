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

def calculateSquareFractionNotation(number):
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


def calculateFraction(prefix):
    if (1==len(prefix)):
        return Fraction(prefix[0], 1)
    denominator=calculateFraction(prefix[1:])
    fraction=prefix[0]+Fraction(denominator.denominator, denominator.numerator)
    return fraction
