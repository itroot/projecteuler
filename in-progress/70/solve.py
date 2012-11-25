#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

def eulerTotient(number):
    factorization=factorize(number)
    uniquePrimeList=list(set(factorization))
    return reduce(lambda a, b: a*(b-1), uniquePrimeList, 1)

print eulerTotient(87109)

for number in range(2, 10**5):
    hashSort=lambda s: "".join(sorted([c for c in str(s)]))
    phi=eulerTotient(number)
    if hashSort(number)==hashSort(phi):
        print number, phi, number/(1.0*phi), factorize(number)
    
