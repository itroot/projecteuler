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

remarkableList=[]

primeCount=len(primeList)
for i in range(0, primeCount):
    for j in range(i, primeCount):
        primeI=primeList[i]
        primeJ=primeList[j]
        if isRemarkable(primeI, primeJ):
            remarkableList.append((primeI, primeJ))
            #print i, j
print remarkableList

