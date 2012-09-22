#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import copy

upperLimit=(10**3)+100

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimit)
primeList=copy.copy(eratosthenesSieve.sieve())
primeSet=set(primeList)
print primeList
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
    print prime, len(remarkableListList), filter(lambda e: len(e)>3, remarkableListList)
    for remarkableList in remarkableListList:
        if (isRemarkableAtList(prime, remarkableList)):
            remarkableListNew=copy.copy(remarkableList)
            remarkableListNew.append(prime)
            remarkableListList.append(remarkableListNew)
    #if prime<100:
    remarkableListList.append([prime])

print filter(lambda e: len(e)>3, remarkableListList)
print
print filter(lambda e: len(e)>4, remarkableListList)
#print
#print remarkableListList

