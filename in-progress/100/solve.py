#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
see: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Pell.27s_equation
"""


"""
Let A be number of blue discs, B - number of all discs
Than, (A/B)*((A-1)*(B-1) == 1/2 -> 2*A**2-2*A == B**2 - B
Than, B**2 - 2*A**2 == B - 2*A
Than, (2*B-1)**2 - 2*(2*A-1)**2 = -1
It's like a Pell's equation, only with -1 sign
"""

import math
import fractions

upperLimit = 10**12

exampleList = (
    (3, 4),
    (3*5, 3*7),
    (5*17, 5*24),
    (17*29, 17*41),
    (29*99, 29*140),
    (99*169, 99*239),
)

def printExample(example):
    (a, b) = example
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(a-1, b-1)
    print a, b, ":", f1, f2, f1*f2

for example in exampleList:
    printExample(example)

"""
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
"""
"""
currentRange = range(2, 1000)
for i in currentRange:
    for j in currentRange:
        #ourEquation = lambda i, j: i**2-2*j**2 == i - 2*j
        ourEquation = lambda i, j: (2*i-1)**2-2*(2*j-1)**2 == -1
        pellEquation = lambda i, j: i**2-2*j**2 in (-1, 1)
        data = (
            ("Our", ourEquation),
            #("Our", ourEquation)
            ("Pell", pellEquation),
        )
        for (name, equation) in data:
            if equation(i, j):
                gcdValue = fractions.gcd(i, j)
                print name, i, j, ":", i/gcdValue, j/gcdValue, gcdValue
"""
pellSolutionList = [
    (1, 0),
    (1, 1),
]

def addNextSolution(pellSolutionList):
    lastSolution = pellSolutionList[-1]
    prevLastSolution = pellSolutionList[-2]
    nextSolution = lambda l, p, i: 2*l[i]+p[i]
    newSolution = (nextSolution(lastSolution, prevLastSolution, 0), nextSolution(lastSolution, prevLastSolution, 1))
    pellSolutionList.append(newSolution)
import pprint
#pprint.pprint(pellSolutionList)
while True:
    addNextSolution(pellSolutionList)
    overallDiskNumber = (pellSolutionList[-1][0]+1)/2
    if overallDiskNumber > upperLimit:
        print (pellSolutionList[-1][1]+1)/2
        break
#pprint.pprint(pellSolutionList)
import sys
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
