#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nth triangle is n*(n-1)/2
# we need factorize n and n-1 and 

import sys
sys.path.append("../lib")
from Factorize import *

def factorization2power(factorization):
    result={}
    for factor in factorization:
        if factor in result:
            result[factor]+=1
        else:
            result[factor]=1
    return result

def numberOfDivisorsFromFactors(factorization):
    factor2power=factorization2power(factorization)
    result=1
    for factor in factor2power:
        result*=factor2power[factor]+1
    return result

factorization=[2]
for i in range(3, 90000):
    triangleNumber=i*(i-1)/2
    nextFactorization=factorize(i)
    mergeFactorization=sorted(factorization+nextFactorization)
    mergeFactorization=mergeFactorization[1:]
    divisorsNumber=numberOfDivisorsFromFactors(mergeFactorization)
    #print triangleNumber, mergeFactorization, divisorsNumber
    if (divisorsNumber>500):
        print triangleNumber
        break
    factorization=nextFactorization

