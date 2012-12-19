#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

precomputedFactorials=[math.factorial(i) for i in range (0, 10)]
#print precomputedFactorials
def factorial10(number):
    return precomputedFactorials[number]

upperLimit=10**6

precomputedNumbers={}

def nextInChain(number):
    if (number in precomputedNumbers):
        return precomputedNumbers[number]
    else:
        result=sum(map(lambda e: factorial10(int(e)), list(str(number))))
        precomputedNumbers[number]=result
        return result

def constructChain(number):
    sequence=[]
    numberToIndex={}
    while True:
        if number in numberToIndex:
            index=numberToIndex[number]
            return (sequence[:index], sequence[index:])
            #return len(sequence)
        else:
            sequence.append(number)
            numberToIndex[number]=len(sequence)
            number=nextInChain(number)

result=0
for i in range(1, upperLimit):
    chain=constructChain(i)
    nonRepeatingItemsCount=len(chain[0])+len(chain[1])
    if (60==nonRepeatingItemsCount):
        result+=1
    if (0==i%10000):
        print i, result
