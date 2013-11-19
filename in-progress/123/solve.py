#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import EratosthenesSieve

sieve = EratosthenesSieve()
sieve.growToNumber(10**6)

for (index, prime) in enumerate(sieve.sieve()):
    primeIndex = index + 1
    r = 2*primeIndex*prime % prime**2
    if r>10**10:
        print r, "->", primeIndex, prime
        break
