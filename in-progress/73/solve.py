#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *
from fractions import *

upperLimit=12000


f=Factorization()
print f.eulerTotient(upperLimit+1)
totient=sum(f.eulerTotient(i) for i in range(2, upperLimit+1))
print "Before 1/2: ", (totient-1)/2
print "Guess: ", (totient-1)/2 -(totient-1)/3

def generateFareySequenceLevel(upperLimit):
    result=set()
    for i in range(1, upperLimit-1):
        result.add(Fraction(i, upperLimit))
    return sorted(list(result))

allSequence=[]
for i in range(2, 200):
    sequence=generateFareySequenceLevel(i)
    allSequence=sorted(list(set(allSequence+sequence)))
    #print allSequence
    totient=sum(f.eulerTotient(i) for i in range(2, i+1))
    print i, len(filter(lambda e: e<Fraction(1, 3), allSequence)), (totient-1)/3
