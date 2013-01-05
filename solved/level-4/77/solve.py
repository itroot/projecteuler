#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

sieve=EratosthenesSieve()
probablyEnough=10**5
sieve.growToNumber(probablyEnough)

primeList=sieve.sieve()

cache={}

def differentWaysWithMaximum(number, maximumIndex):
    #print number, maximumIndex
    numberSlashMaximum=str(number)+"/"+str(maximumIndex)
    if (numberSlashMaximum in cache):
        return cache[numberSlashMaximum]
    #result=(0, [])
    result=0
    if 0==number:
        result=(1, [[]])
        result=1
    else:
        for i in reversed(range(0, maximumIndex+1)):
            left=number-primeList[i]
            if (left>=0):
                #numberAndWays=differentWaysWithMaximum(left, i)
                #array=result[1]+[([primeList[i]]+x) for x in numberAndWays[1]]
                #result=(result[0]+numberAndWays[0], array)
                result+=differentWaysWithMaximum(left, i)
    #print (number, maximumIndex, result)
    cache[numberSlashMaximum]=result
    return result

def differentWays(number):
    return differentWaysWithMaximum(number, number-1)

#print differentWays(10)

upperLimit=5000

for i in range(1, 1000):
    result=differentWays(i)
    if result>upperLimit:
        print i
        break

