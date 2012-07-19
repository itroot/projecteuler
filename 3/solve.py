#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import math

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
    
    

number=int(open("input.txt").read())


print factorize(number)[-1]
