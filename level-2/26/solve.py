#!/usr/bin/env python
# -*- coding: utf-8 -*-

def divide1by(number, accuracy):
    my1=10**accuracy
    return str(my1/number)

def findDividePeriod(numbers, dividerLength):
    array=numbers[2*dividerLength+1:]
    pattern=array[0:dividerLength]
    array=array[dividerLength:]
    return array.index(pattern)+1

def periodLength(number):
    numbers=divide1by(number, 10000)
    return findDividePeriod(numbers, len(str(number)))

value=2
maxPeriod=1
for i in range(2, 1000):
    period=periodLength(i)
    if period>maxPeriod:
        maxPeriod=period
        value=i
print value
