#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction

def generateLevel(number):
    result=[]
    for i in range(1, number):
        result.append(Fraction(i, number))
    return result

def generate(upperBound):
    result=[]
    for i in range(2, upperBound+1):
        result+=generateLevel(i)
    return sorted(list(set(result)))

for i in range(2, 30):
    result=generate(i)
    #print result
    print i, len(result)
