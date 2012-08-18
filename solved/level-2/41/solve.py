#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Permutation import *
from EratosthenesSieve import *
import math

sieve=EratosthenesSieve()
sieve.growToNumber(7654321)
primeSet=set(sieve.sieve())

upperLimit=7
digits=range(1, upperLimit+1)

productSet=set()

pandigitalPrimes=[]

for i in range(0, math.factorial(upperLimit)):
    permutation=nth_permutation(digits, i)
    number=reduce(lambda a, b: 10*a+b, permutation)
    if number in primeSet:
        pandigitalPrimes.append(number)
print max(pandigitalPrimes)
        
