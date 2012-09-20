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
primeListLimited=filter(lambda e: e<upperLimit, primeList)

remarkableListList=[]

#for prime in primeListLimited:
#    for remarkableList in remarkableListList:


for i in range(0, len(primeListLimited)):
    for j in range(0, i):
        first=primeListLimited[i]
        second=primeListLimited[j]
        firstSecond=int(str(first)+str(second))
        secondFirst=int(str(second)+str(first))
        if (firstSecond in primeSet and secondFirst in primeSet):
            result.append((first, second))
print result

