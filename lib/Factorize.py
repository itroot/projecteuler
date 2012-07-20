#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from EratosthenesSieve import *

def factorize(number):
    sqrtnumber=int(math.ceil(math.sqrt(number)))
    factorization=[]
    sieve=EratosthenesSieve()
    sieve.growToNumber(sqrtnumber)
    for prime in sieve.sieve():
        while True:
            if (0==number%prime):
                factorization.append(prime)
                number=number/prime
            else:
                break
    if (1!=number):
        factorization.append(number)
    return factorization
