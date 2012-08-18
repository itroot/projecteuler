#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

upperLimit=10**6

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimit)
sieve=eratosthenesSieve.sieve()
sieveSet=set(sieve)
length=len(sieve)
#print sieve, length

primeSums=[0]*length

maxPrimesInSequence=1
while sum(sieve[0:maxPrimesInSequence])<upperLimit:
    maxPrimesInSequence+=1
#print maxPrimesInSequence

for consecuteveNum in reversed(range(0, maxPrimesInSequence)):
    for index in range(0, length):
        addendantIndex=index+consecuteveNum
        if addendantIndex>=length:
            continue
        primeSum=sum(sieve[index:addendantIndex])
# curiosity =)
#        if 997651==primeSum:
#            print sieve[index:addendantIndex]
        if (primeSum)>upperLimit:
            break
    	primeSums[index]=primeSum
    primes=filter(lambda e: e in sieveSet, primeSums[:-consecuteveNum])
    if len(primes)>0:
        print primes[0]
        break
    
