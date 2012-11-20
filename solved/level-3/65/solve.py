#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction

def calculateFraction(prefix):
    if (1==len(prefix)):
        return Fraction(prefix[0], 1)
    denominator=calculateFraction(prefix[1:])
    fraction=prefix[0]+Fraction(denominator.denominator, denominator.numerator)
    return fraction

def generateExpPrefix(number):
    result=[2]
    middleNumber=2
    while len(result)<number:
        result.append(1)
        result.append(middleNumber)
        result.append(1)
        middleNumber+=2
    return result[:number]

#prefix=[1, 2, 2, 2]
#print calculateFraction(prefix)
#print generateExpPrefix(10)

expPrefix=generateExpPrefix(100)
fraction=calculateFraction(expPrefix)
print sum(map(lambda e: int(e), list(str(fraction.numerator))))
