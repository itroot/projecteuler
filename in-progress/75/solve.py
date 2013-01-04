#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triples
"""
import sys
sys.path.append("../lib")
import Factorize
import math

def isGeneratingPrimitiveTriple(m, n):
    if (n>m):
        (m, n)=(n, m)
    difference=m-n
    if (0==difference%2):
        return False
    if 1==n:
        return True
    f=Factorize.Factorization()
    nFactors=set(f.factorize(n))
    mFactors=set(f.factorize(m))
    return 0==len(mFactors.intersection(nFactors))

#print isGeneratingPrimitiveTriple(21, 3)
#sys.exit(0)
maxWireLength=1000#1500000

maxHypoLength=int(math.ceil(maxWireLength/2))
maxGenerativeNumber=int(math.ceil(math.sqrt(maxHypoLength)))
#print maxGenerativeNumber

#tripleList=[]
sumList=[]
result=0
for m in range(1, maxGenerativeNumber+1):
    print m
    for n in range(1, m):
        a=m**2-n**2
        b=2*m*n
        c=m**2+n**2
        if (a+b+c)<=maxWireLength and isGeneratingPrimitiveTriple(m, n):
            #tripleList.append((a, b, c))
            sumList.append(a+b+c)
            result+=1
#print tripleList
sumList=sorted(sumList)
uniqueList=[sumList[0]]
for (i, number) in enumerate(sumList):
    print i
    isUnique=True
    for uniqueNumber in uniqueList:
        if number%uniqueNumber==0:
            isUnique=False
            break
    if isUnique:
        uniqueList.append(number)
#print sumList
print uniqueList, len(uniqueList)
#print result