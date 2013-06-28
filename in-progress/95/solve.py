#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

# draw DAG graph for numbers < 100

upperLimit = 10**3+1
#upperLimit = 10**6+1

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

"""
import sys
sys.path.append("../lib")
from Factorize import getAllDivisors
"""
# 2,2,2 -> 2,4,8 , choose one
# 3, 5 -> choose any
primeDivisors = map(getPrimeDivisors, range(0, upperLimit))

pprint.pprint(sieve[:100])
pprint.pprint(primeDivisors[:100])