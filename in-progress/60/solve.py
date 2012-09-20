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

def isRemarkable(first, second):
   firstSecond=int(str(first)+str(second))
   secondFirst=int(str(second)+str(first))
   return firstSecond in primeSet and secondFirst in primeSet

def isRemarkableAtList(prime, remarkableList):
    for otherPrime in remarkableList:
        if not isRemarkable(prime, otherPrime):
            return False
    return True

for prime in primeListLimited:
    for remarkableList in remarkableListList:
        if (isRemarkableAtList(prime, remarkableList)):
            remarkableList.append(prime)
    if prime<100:
        remarkableListList.append([prime])

print filter(lambda e: len(e)>3, remarkableListList)

