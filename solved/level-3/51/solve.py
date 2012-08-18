#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import itertools

upperLimit=10**6
patternFamilySize=8

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimit)
sieve=eratosthenesSieve.sieve()
sieveSet=set(sieve)
length=len(sieve)

#print sieve, length

def allSubsets(iterable):
    result=[[]]
    for i in range(1, len(iterable)+1):
        result+=list(itertools.combinations(iterable, i))
    return result

def emitPatterns(numberInText, digit):
    result=[]
    digitOffsetList=[]
    for (index, currentDigit) in enumerate(numberInText):
        if digit==currentDigit:
            digitOffsetList.append(index)
    for combination in allSubsets(digitOffsetList):
        #print combination
        if len(combination)!=0:
            pattern=list(numberInText)
            for position in combination:
                pattern[position]="*"
            result.append("".join(pattern))
    return result

def classifyNumber(number):
    numberInText=str(number)
    uniqueDigits=sorted(list(set(list(numberInText))))
    patterns=[]
    for digit in uniqueDigits:
        patterns+=emitPatterns(numberInText, digit)
    return patterns
#print emitPatterns("56333", "3")
#raise 1    
pattern2primeList={}
for prime in sieve:
    patterns=classifyNumber(prime)
    for pattern in patterns:
        value=[]
        if pattern in pattern2primeList:
            value=pattern2primeList[pattern]
        else:
            pattern2primeList[pattern]=value
        value.append(prime)
#print pattern2primeList
#print pattern2primeList["56**3"]
smallestPrimes=[]
for (pattern, primeList) in pattern2primeList.iteritems():
    if len(primeList)>=patternFamilySize:
        #print pattern, primeList
        smallestPrimes.append(min(primeList))
print min(smallestPrimes)
