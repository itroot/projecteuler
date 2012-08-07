#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import bisect
import math

upperLimit=100000

sieve=EratosthenesSieve()
sieve.growToNumber(upperLimit)
primeList=sieve.sieve()
primesSet=set(primeList)

def isSquare(number):
    #print number
    assumedSqrt=int(math.sqrt(number))
    return assumedSqrt**2==number

for i in range(3, upperLimit, 2):
    if not i in primesSet:
        #print ">", i
        maxPrimePos=bisect.bisect_left(primeList, i)+2
        squareFound=False
        for primePos in range(1, maxPrimePos):
            squareAssumed=(i-primeList[primePos])/2
            if squareAssumed<=0:
                continue
            if isSquare(squareAssumed):
                squareFound=True
                break
        if not squareFound:
            print i
            sys.exit(0)
