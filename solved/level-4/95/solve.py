#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

# draw DAG graph for numbers < 100
# you can code any dag in numbers, any new dependnecy - just multiplication

upperLimit = 10**6+1

sieve = [None]*(upperLimit+1)
for number in range(0, upperLimit):
    if number<2:
        continue
    divisorTuple = sieve[number]
    if divisorTuple is None:
        for i in range(1, upperLimit/number+1):
            index = number*i
            if sieve[index] is None:
                sieve[index] = (number, i)

def getPrimeDivisors(number):
    divisorList = sieve[number]
    if number<2:
        return []
    if (divisorList[1]==1):
        return [divisorList[0]]
    else:
        return [divisorList[0]]+getPrimeDivisors(divisorList[1])

#"""
import sys
sys.path.append("../lib")
from Factorize import AllDivisors
def divisors(factorization):
    return AllDivisors(factorization).divisors()

# 2,2,2 -> 2,4,8 , choose one
# 3, 5 -> choose any
# (2, 3), (3, 1), (5, 2) -> (3+1)*(1+1)(2+1)
# (2, 4, 8), (3), (5, 25)


allDivisorsList = map(lambda e: divisors(getPrimeDivisors(e)), range(0, upperLimit))

#pprint.pprint(sieve[:100])
#pprint.pprint(allDivisorsList[:100])
sumList = map(lambda e: sum(e[:-1]), allDivisorsList)

visitedList = [False] * upperLimit
visitedList[0] = True
visitedList[1] = True

#pprint.pprint(sumList[:100])

cycleList = []
for i in range(0, upperLimit):
    if visitedList[i]:
        continue
    #print i
    possibleCycle = [i]
    visitedList[i] = True
    nextIndex = sumList[i]
    while True:
        if nextIndex>upperLimit:
            break
        if (visitedList[nextIndex]):
            break
        visitedList[nextIndex] = True
        possibleCycle.append(nextIndex)
        nextIndex = sumList[nextIndex]
        #print nextIndex
    if nextIndex in possibleCycle:
        cycleList.append(possibleCycle[possibleCycle.index(nextIndex):])
#import pprint
#pprint.pprint(cycleList)
print min(max(cycleList, key=lambda e: len(e)))