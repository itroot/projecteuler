#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import itertools

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(100)
primes = eratosthenesSieve.sieve()

upper_limit = 1000
#upper_limit = 10**16

count = 0

for prime4 in itertools.combinations(primes, 4):
    max_powers = map(lambda e: upper_limit / e + 1, prime4)
    print max_powers
    range_powers = map(lambda e: range(1, e + 1), max_powers)
    for powers in itertools.product(*range_powers):
        #print powers
        product1 = reduce(lambda a, (pr, pw) : a * pr ** pw, zip(prime4, powers), 1)
        if product1 < upper_limit:
            count += 1
print count
