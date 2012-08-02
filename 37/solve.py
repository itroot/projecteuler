#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

upperBound=10**6

sieve=EratosthenesSieve()
sieve.growToNumber(upperBound)
sieveList=sieve.sieve()
sieveSet=set(sieveList)

def isTruncatable(number, sieve):
    digits=map(lambda e: int(e), str(number))
    length=len(digits)
    for i in range(1, length):
        numberRight=reduce(lambda a, b: 10*a+b, digits[i:])
        #print numberRight
        numberLeft=reduce(lambda a, b: 10*a+b, digits[:-i])
        #print numberLeft
        if not numberRight in sieve or not numberLeft in sieve:
            return False
    return True
        

#print isTruncatable(3797, sieveSet)
truncatables=[]
for number in sieveList:
    if (isTruncatable(number, sieveSet)):
        if number>10:
            truncatables.append(number)
            #print number

print sum(truncatables)