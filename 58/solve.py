#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import math

upperPrimeLimit=5000000

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
    #print radius, primeNumbers, totalNumbers
    radius+=1
    numbers=getDiagonalNumbers(radius)
    for number in numbers:
        isPrime=True
        sqrtNumberPlusOne=math.sqrt(number)+1
        for prime in primeList:
            if prime>=sqrtNumberPlusOne:
                break
            if 0==number%prime:
                isPrime=False
                break
        if isPrime:
            primeNumbers+=1
        totalNumbers+=1

#print radius, primeNumbers, totalNumbers
print 2*radius+1

