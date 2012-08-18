#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *


upperLimit=10**3
upperLimitSquare=upperLimit**2

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimitSquare)
primeList=eratosthenesSieve.sieve()
primeSet=set(primeList)

result=[]
result.append(filter(lambda e: e<upperLimit, primeList))
result.append([])

for i in range(0, len(result[0])):
    for j in range(0, i):
        first=result[0][i]
        second=result[0][j]
        firstSecond=int(str(first)+str(second))
        secondFirst=int(str(second)+str(first))
        if (firstSecond in primeSet and secondFirst in primeSet):
            result[1].append((first, second))
print result

