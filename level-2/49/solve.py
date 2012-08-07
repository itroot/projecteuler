#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *

import pprint

knownProgression=[1487, 4817, 8147]

fourDigitsPrimes=[]
sieve=EratosthenesSieve()
sieve.growToNumber(10000)
for prime in sieve.sieve():
    if prime>1000:
        fourDigitsPrimes.append(prime)
#print fourDigitsPrimes

uniqueSortedDigits2PrimeList={}
for prime in fourDigitsPrimes:
    uniqueSortedDigits="".join(sorted(list(set(list(str(prime))))))
    if not uniqueSortedDigits in uniqueSortedDigits2PrimeList:
        uniqueSortedDigits2PrimeList[uniqueSortedDigits]=[]
    uniqueSortedDigits2PrimeList[uniqueSortedDigits].append(prime)
#print uniqueSortedDigits2PrimeList

def findProgressionInDelta(delta, pairs):
    result=[]
    while len(pairs)>=2:
        currentProgressionIndex=[0]
        for (pairIndex, pair) in enumerate(pairs):
            if pairIndex in currentProgressionIndex:
                continue
            elif pairs[currentProgressionIndex[-1]][1]==pair[0]:
                currentProgressionIndex.append(pairIndex)
        if len(currentProgressionIndex)>1:
            result.append(map(lambda e: pairs[e][0], currentProgressionIndex))
            result[-1].append(pairs[currentProgressionIndex[-1]][1])
        for index in reversed(currentProgressionIndex):
            del pairs[index]
    return result
        

def findAllProgressions(sortedList):
    result=[]
    #print sortedList
    delta2pairs={}
    for (i, proposedStart) in enumerate(sortedList):
        for j in range(i+1, len(sortedList)):
            #print i, j
            proposedDelta=sortedList[j]-proposedStart
            if not proposedDelta in delta2pairs:
                delta2pairs[proposedDelta]=[]
            delta2pairs[proposedDelta].append([sortedList[i], sortedList[j]])
    #print delta2pairs
    #delta2pairs=dict((k, v) for k, v in delta2pairs.iteritems() if len(v)>1)
    #if len(delta2pairs)>0:
    #    pprint.pprint(delta2pairs)
    
    for delta, pairs in delta2pairs.iteritems():
        result+=findProgressionInDelta(delta, pairs)
    return result

for (uniqueSortedDigits, primeList) in uniqueSortedDigits2PrimeList.iteritems():
    if len(primeList)>2:
        sortedPrimeList=sorted(primeList)
        #print sortedPrimeList
        #sortedPrimeList.append(99999999)
        progressions=findAllProgressions(sortedPrimeList)
        if (0!=len(progressions)):
            for progression in progressions:
                if knownProgression!=progression:
                    print reduce(lambda a, b: 10000*a+b, progression)
    else:
        continue

#print findAllProgressions([1, 2, 3, 4, 6, 101, 102, 103])
