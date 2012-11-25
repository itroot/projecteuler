#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *
from EratosthenesSieve import *
import math

upperLimit=10**7

sieve=EratosthenesSieve()
sieve.growToNumber(int(math.ceil(math.sqrt(upperLimit))))
primeList=list(sieve.sieve())
print primeList, len(primeList)

hashSort=lambda s: "".join(sorted([c for c in str(s)]))

for prime1 in primeList:
    for prime2 in primeList:
    #    if prime2<prime1:
    #        continue
        number=prime1*prime2
        phi=(prime1-1)*(prime2-1)
        #print number, phi
        if hashSort(number)==hashSort(phi):
            print "#", number, phi, number/(1.0*phi), factorize(number)



def eulerTotient(number):
    factorization=factorize(number)
    uniquePrimeList=list(set(factorization))
    return reduce(lambda a, b: a*(b-1), uniquePrimeList, 1)

print eulerTotient(87109)

for number in range(2, 10**5):
    phi=eulerTotient(number)
    if hashSort(number)==hashSort(phi):
        print number, phi, number/(1.0*phi), factorize(number)
    
