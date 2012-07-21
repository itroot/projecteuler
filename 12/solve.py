#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nth triangle is n*(n-1)/2
# we need factorize n and n-1 and 

import sys
sys.path.append("../lib")
from Factorize import *

def numberOfDivisorsFromFactors(factorization):

factorization=[2]
for i in range(3, 10):
    nextFactorization=factorize(i)
    mergeFactorization=sorted(factorization+nextFactorization)
    factorization=nextFactorization

