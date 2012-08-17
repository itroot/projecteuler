#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

upperPrimeLimit=150000000

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperPrimeLimit)
primeList=eratosthenesSieve.sieve()
primeSet=set(primeList)

def getDiagonalNumbers(radius):
    basenumber=2*radius+1
    numberList=[]
    for i in range(0, 4):
        numberList.append(basenumber**2-i*(basenumber-1))
    return tuple(set(numberList))

#print getDiagonalNumbers(2)


radius=1
primeNumbers=3
totalNumbers=5

while (totalNumbers/primeNumbers<10):
    print radius, primeNumbers, totalNumbers
    radius+=1
    numbers=getDiagonalNumbers(radius)
    for number in numbers:
        if number in primeSet:
            primeNumbers+=1
        totalNumbers+=1

print (2*radius-1)**2
