#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ContinuedFraction import *

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
