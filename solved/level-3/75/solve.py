#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from PythagoreanTriples import traverse, MN2ABC, pairMN

allTriples=[]
maxWireLength=1500000

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
