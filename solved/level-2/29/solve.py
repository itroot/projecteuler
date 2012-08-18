#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

upperLimit=101
rangeA=range(2, upperLimit)
rangeB=range(2, upperLimit)

def powerFactorization(factorization, power):
    return sorted(factorization*power)

allTerms=set()
for a in rangeA:
    factorization=factorize(a)
    for b in rangeB:
        allTerms.add(str(powerFactorization(factorization, b)))
print len(allTerms)