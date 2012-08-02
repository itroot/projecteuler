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

def isCircular(number, sieve):
    digits=map(lambda e: int(e), str(number))
    length=len(digits)
    for i in range(0, length+1):
        first=digits[0]
        digits=digits[1:]
        digits.append(first)
        n=reduce(lambda a, b: 10*a+b, digits)
        if not n in sieve:
            return False
    return True
        
numCount=0
for number in sieveList:
    if (isCircular(number, sieveSet)):
        #print number
        numCount+=1
print numCount
