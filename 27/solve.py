#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

#80*80+80*10000+10000<100000

primesUpperLimit=100000
coefficientRange=range(-999, 1000)

class Polynom():
    def __init__(self, coefficients):
        self.__coefficients=coefficients
    def evaluate(self, number):
        result=0
        for (counter, coefficient) in enumerate(reversed(self.__coefficients)):
            result+=coefficient*number**counter
        return result

sieve=EratosthenesSieve()
sieve.growToNumber(primesUpperLimit)
primeSet=set(sieve.sieve())

maxPrimesCount=0
maxA=0
maxB=0
for a in coefficientRange:
    for b in coefficientRange:
        polynom=Polynom([1, a, b])
        primesCount=0
        for i in range(0, 81):
            if (polynom.evaluate(i) in primeSet):
                primesCount+=1
            else:
                if (primesCount>maxPrimesCount):
                    maxPrimesCount=primesCount
                    maxA=a
                    maxB=b
                break
print maxA*maxB