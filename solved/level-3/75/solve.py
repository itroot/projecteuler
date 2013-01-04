#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
"""

allTriples=[]
maxWireLength=1500000
pairMN=(2, 1)

def nextLevel(pairMN):
    (m, n)=pairMN
    return ((2*m-n, m), (2*m+n, m), (m+2*n, n))

def MN2ABC(pairMN):
    (m, n)=pairMN
    return (m**2-n**2, 2*m*n, m**2+n**2)

def traverse(pairMN, condition):
    if (condition(pairMN)):
        threePairMN=nextLevel(pairMN)
        for pairMN in threePairMN:
            traverse(pairMN, condition)

def traverseCondition(pairMN):
    triple=MN2ABC(pairMN)
    result=sum(triple)<=maxWireLength
    if result:
        allTriples.append(triple)
    return result

traverse(pairMN, traverseCondition)
lengthList=sorted(map(lambda e: sum(e), allTriples))

def generateSet(number):
    result=set()
    for i in range(0, maxWireLength/number):
        result.add((i+1)*number)
    #print result
    return result

result=set()
compromised=set()

for length in lengthList:
    newSet=generateSet(length)
    newSet=newSet-compromised
    compromised|=newSet&result
    result^=newSet
print len(result)
