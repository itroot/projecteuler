#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let a, b, c - a dimensions of a cuboid.
Suppose that M>=a>=b>=c . Then a shortest cuboid route will be:
(a**2+(b+c)**2)**.5 , i.e. a hypo of triangle catetes: (a)<=M, (b+c)<=2*M.
Let x=b+c, then , a>=x (?) -> x/2 possibilities, a<x ?
"""

import sys
sys.path.append("../lib")
from IsSquare import isSquare

#print "test"
"""
Idea: we can generate all P-triplets under M, then calculate all
possible cuboid dimensions
TODO: We can generate primitive triplets only
"""
tripletList=[]
M=100
for m in range(1, M):
    for n in range(1, m):
        triplet=(m**2-n**2, 2*m*n) #, m**2+n**2)
        if not all(map(lambda e: e<=M, triplet)):
            break
        else:
            tripletList.append(triplet)
#print tripletList
#print len(tripletList)

import sys
#sys.exit()
#print "test"

def getSpecialCuboidsUnder(M):
    result=0
    for a in range(1, M+1):
        print "# a -> ", a
        for b in range(1, a+1):
            for c in range(1, b+1):
                if (isSquare(a**2+(b+c)**2)):
                    import math
                    print a, b, c, "->", a, b+c, int(math.sqrt(a**2+(b+c)**2))
                    result+=1
    return result

upperLimit=100

#sys.exit(0)
from PythagoreanTriples import traverse, MN2ABC, pairMN

isFit = lambda triple: min(triple) <= upperLimit

allPrimitiveTriples = []
def traverseCondition(pairMN):
    triple=MN2ABC(pairMN)
    result=isFit(triple)
    if result:
        allPrimitiveTriples.append(triple)
    return result

traverse(pairMN, traverseCondition)

# every primitive triple gives us number of primitive cuboibs ?

import pprint
#pprint.pprint(allPrimitiveTriples)

def expandTriple(triple):
    multipliedTriple = lambda triple, i: tuple(map(lambda e: e*i, triple))
    expansion = []
    index = 1
    newTriple = triple
    while isFit(newTriple):
        expansion.append(newTriple)
        newTriple = multipliedTriple(triple, index)
        index += 1
    return expansion

allTriples = list(set(reduce(lambda a, b : a+b, map(lambda e: expandTriple(tuple(sorted(e))), allPrimitiveTriples), [])))

#pprint.pprint(allTriples)
#print len(allTriples)

def solve(allTriples, M):
    result = 0
    for triple in allTriples:
        if (triple[1]<=M):
            number = triple[0]/2
            print "CASE1", triple, number
            result += number
        if (triple[0]<=M):
            number = triple[1]-triple[0]+1
            if (number<=triple[0]):
                print "CASE2", triple, number
                result += number;
    return result

currentNumber = 8
print getSpecialCuboidsUnder(currentNumber)
print "Solve:", solve(allTriples, currentNumber)
#print map(getSpecialCuboidsUnder, range(2, 80))
