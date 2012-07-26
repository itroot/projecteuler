#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Factorize import *

def isAmicable(number):
    other=sum(getAllDivisors(number)[:-1])
    if (0==other):
        return False
    otherSum=sum(getAllDivisors(other)[:-1])
    return number==otherSum

amicables=set()
for i in range(1, 10000):
    if isAmicable(i):
        opposite=sum(getAllDivisors(i)[:-1])
        if i!=opposite:
            amicables.add(tuple(sorted([i, opposite])))

result=0
for amicable in amicables:
    result+=sum(amicable)
print result