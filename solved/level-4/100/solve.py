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

upperLimit = 10**12

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

while True:
    addNextSolution(pellSolutionList)
    overallDiskNumber = (pellSolutionList[-1][0]+1)/2
    if overallDiskNumber > upperLimit:
        print (pellSolutionList[-1][1]+1)/2
        break

