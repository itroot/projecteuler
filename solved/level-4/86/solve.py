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
upperLimit=5000
from PythagoreanTriples import traverse, MN2ABC, pairMN

isFit = lambda triple: min(triple) <= upperLimit

allPrimitiveTriples = []
def traverseCondition(pairMN):
    triple=MN2ABC(pairMN)
    result=isFit(triple)
    if result:
        allPrimitiveTriples.append(triple)
    return result

sys.setrecursionlimit(10000)
traverse(pairMN, traverseCondition)

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

def solve(allTriples, M):
    result = 0
    for triple in allTriples:
        if (triple[1]<=M):
            number = triple[0]/2
            result += number
        if (triple[0]<=M):
            number = triple[0] - (triple[1]-1)/2
            if (number<=triple[0] and number>0):
                result += number;
    return result

for i in range(1000, 3000):
    if solve(allTriples, i)>10**6:
        print i
        break
