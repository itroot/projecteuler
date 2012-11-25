#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *
from EratosthenesSieve import *
import math

upperLimit=10**7

sieve=EratosthenesSieve()
sieve.growToNumber(2*int(math.ceil(math.sqrt(upperLimit))))
primeList=list(sieve.sieve())
#print primeList, len(primeList)

hashSort=lambda s: "".join(sorted([c for c in str(s)]))

results=[]

for prime1 in primeList:
    for prime2 in primeList:
        if prime2<prime1:
             continue
        number=prime1*prime2
        if number>upperLimit:
            continue
        phi=(prime1-1)*(prime2-1)
        #print number, phi
        if hashSort(number)==hashSort(phi):
            #print "#", number, phi, number/(1.0*phi), factorize(number)
            results.append((number, phi, number/(1.0*phi)))

results=sorted(results, key=lambda e: e[2])
print results[0][0]
sys.exit(0)


def eulerTotient(number):
    factorization=factorize(number)
    uniquePrimeList=list(set(factorization))
    return reduce(lambda a, b: a*(b-1), uniquePrimeList, 1)

print eulerTotient(87109)

for number in range(2, 10**5):
    phi=eulerTotient(number)
    if hashSort(number)==hashSort(phi):
        print number, phi, number/(1.0*phi), factorize(number)
    
