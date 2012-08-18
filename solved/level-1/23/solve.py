#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

maxNotSumOfTwoAbundant=28123

def isAbundant(number):
    properDivisors=getAllDivisors(number)[:-1]
    return sum(properDivisors)>number

def getLowerAbundantNumbers(number):
    result=[]
    for i in range(1, number):
        if isAbundant(i):
            result.append(i)
    return result

abundantNumbers=getLowerAbundantNumbers(maxNotSumOfTwoAbundant+1)
abundantNumbersSet=set(abundantNumbers)

def isSumOfTwoFromSetList(number, alist, aset):
    for a in alist:
        if a>number:
            return False
        else:
            if (number-a) in aset:
                return True
        
result=0
for i in range(1, maxNotSumOfTwoAbundant+1):
    if not isSumOfTwoFromSetList(i, abundantNumbers, abundantNumbersSet):
        result+=i
print result
