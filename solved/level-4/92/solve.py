#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nextStep(number):
    return sum(map(lambda e: int(e)**2, list(str(number))))

cache={89:89, 1:1}

def calculateArrival(number):
    sequence=[]
    while not number in cache:
        number=nextStep(number)
        sequence.append(number)
    for previousNumber in sequence:
        cache[previousNumber]=cache[number]
    return cache[number]

result=0
for i in range(1, 10**7):
    if (calculateArrival(i)==89):
        result+=1
print result
