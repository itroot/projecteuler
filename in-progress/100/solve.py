#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
see: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Pell.27s_equation
"""

import math
import fractions

exampleList = (
    (3*5, 3*7),
    (5*17, 5*24),
    (17*29, 17*41),
#    (29*41, 29*58),
    (29*99, 29*140),
    (99*169, 99*239),
#    (169*408, 169*577),
)

def printExample(example):
    (a, b) = example
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(a-1, b-1)
    print a, b, ":", f1, f2, f1*f2

for example in exampleList:
    printExample(example)

import sys
sys.path.append("../lib")

from IsSquare import isSquare

def testNumber(origin, shift):
    number = (origin**2+shift)/2
    if (isSquare(number)):
        print int(math.sqrt(number)), "/", origin

for i in range(1, 1000000):
    testNumber(i, +1)
    #testNumber(i, +2)
    #testNumber(i, +3)
    testNumber(i, -1)
    #testNumber(i, -2)
    #testNumber(i, -3)
    if (i>20000):
        break

sys.exit(0)

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
