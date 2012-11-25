#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

sieve=EratosthenesSieve()
sieve.growToNumber(100)

primeList=list(sieve.sieve())

upperLimit=10**6
chosenPrimes=[]
primeProduct=1
for prime in primeList:
    primeProduct*=prime
    if primeProduct>upperLimit:
        break
    else:
        chosenPrimes.append(prime)
print reduce(lambda a, b: a*b, chosenPrimes, 1)
