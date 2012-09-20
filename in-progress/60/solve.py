#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *


upperLimit=10**6

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimit)
primeList=eratosthenesSieve.sieve()
primeSet=set(primeList)

remarkableListList=[]

def isRemarkable(first, second):
   firstSecond=int(str(first)+str(second))
   secondFirst=int(str(second)+str(first))
   sieve=eratosthenesSieve
   return sieve.isPrime(firstSecond) and sieve.isPrime(secondFirst)

def isRemarkableAtList(prime, remarkableList):
    for otherPrime in remarkableList:
        if not isRemarkable(prime, otherPrime):
            return False
    return True

for prime in primeList:
    for remarkableList in remarkableListList:
        if (isRemarkableAtList(prime, remarkableList)):
            remarkableList.append(prime)
    if prime<100:
        remarkableListList.append([prime])

print filter(lambda e: len(e)>3, remarkableListList)
print
print filter(lambda e: len(e)>4, remarkableListList)
