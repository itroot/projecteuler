#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import fractions

lowerLimit=10**12
blueDiscNumber=int(lowerLimit*math.sqrt(0.5))

print blueDiscNumber**2
print (blueDiscNumber+1)**2

def fractionize(blueDiscNumber, totalNumber):
    result=fractions.Fraction(blueDiscNumber, totalNumber)
    result=result*fractions.Fraction(blueDiscNumber-1, totalNumber-1)
    return result

number=lowerLimit
numberLimit=(blueDiscNumber+1)**2
print numberLimit
while number<numberLimit:
    result=fractionize(blueDiscNumber, number)
    #print result
    if (result.numerator==1 and result.denominator==2):
        break
    number+=1

print fractionize(blueDiscNumber, lowerLimit)
