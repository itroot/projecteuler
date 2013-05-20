#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import math

upperLimit=50*10**6

sieve=EratosthenesSieve()
sieve.growToNumber(int(math.ceil(math.sqrt(upperLimit))))

primeList2=list(sieve.sieve())
primeList3=filter(lambda e: e<upperLimit**(0.34), primeList2)
primeList4=filter(lambda e: e<upperLimit**(0.26), primeList2)

result=0
cache=set()
for prime2 in primeList2:
#    print prime2
    for prime3 in primeList3:
        for prime4 in primeList4:
            number=prime2**2+prime3**3+prime4**4
            if number<upperLimit:
                if not number in cache:
                    result+=1
                    cache.add(number)

print result
