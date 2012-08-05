#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

upperLimit=100000
length=4

for i in range(2, upperLimit):
    numbers=range(i, i+length)
    factorizations=map(lambda e: set(factorize(e)), numbers)
    if not reduce(lambda a, b: a and (len(b)==length), factorizations, True):
        continue
    #if min(map(lambda e: len(e), factorizations))==1:
    #    continue
    #a1=sum(map(lambda e: len(set(e)), factorizations))
    #a2=len(reduce(lambda a, b: a.union(b), factorizations))
    #print i, factorizations, a1, a2
    #if a1==a2:
    else:
        print i, factorizations
        break
