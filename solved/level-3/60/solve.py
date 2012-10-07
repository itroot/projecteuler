#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from EratosthenesSieve import *
import copy

upperLimit=(10**4)+100

eratosthenesSieve=EratosthenesSieve()
eratosthenesSieve.growToNumber(upperLimit)
primeList=copy.copy(eratosthenesSieve.sieve())
primeSet=set(primeList)
#print primeList
remarkableListList=[]

def isRemarkable(first, second):
   firstSecond=int(str(first)+str(second))
   secondFirst=int(str(second)+str(first))
   sieve=eratosthenesSieve
   return sieve.isPrime(firstSecond) and sieve.isPrime(secondFirst)

remarkableList=[]

primeCount=len(primeList)
for i in range(0, primeCount):
    for j in range(i, primeCount):
        primeI=primeList[i]
        primeJ=primeList[j]
        if isRemarkable(primeI, primeJ):
            remarkableList.append((primeI, primeJ))
            #print i, j
#print remarkableList

from collections import defaultdict
import pprint

graph=defaultdict(set)
for remarkable in remarkableList:
    (first, second)=remarkable
    graph[first].add(second)
    graph[second].add(first)
    
#pprint.pprint(graph)

def NotContains(_not, candidates, graph):
    for vertice in _not:
        #FIXME
        if graph[vertice]==candidates:
            return True
    return False
# http://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%91%D1%80%D0%BE%D0%BD%D0%B0_%E2%80%94_%D0%9A%D0%B5%D1%80%D0%B1%D0%BE%D1%88%D0%B0
def BronKerbosh(compsub, candidates, _not, graph):
    while (len(candidates)!=0 and not NotContains(_not, candidates, graph)):
        vertice=candidates.pop()
        candidates.add(vertice)
        compsub.add(vertice)
        new_candidates=candidates.intersection(graph[vertice])
        new_not=_not.intersection(graph[vertice])
        if (0==len(new_candidates) and 0==len(new_not)):
            if (len(compsub)>4):
                print sum(compsub)
        else:
            BronKerbosh(compsub, new_candidates, new_not, graph)
        _not.add(vertice)
        compsub.remove(vertice)
        candidates.remove(vertice)

BronKerbosh(set(), primeSet, set(), graph)
        
            
    

