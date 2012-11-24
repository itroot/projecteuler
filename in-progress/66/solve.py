#!/usr/bin/env python
# -*- coding: utf-8 -*-

# see: http://en.wikipedia.org/wiki/Pell%27s_equation

import sys
sys.path.append("../lib")
from ContinuedFraction import *

def getNotationApproximation(notation, length):
    (prefix, period)=notation
    result=[]
    result+=prefix
    while (len(result)<length):
        result+=period
    return result[:length]

for i in (2, 3, 5, 6, 7):
    notation=calculateSquareFractionNotation(i)
    approximation=getNotationApproximation(notation, 10)
    fraction=calculateFraction(approximation)
    print i, notation, approximation, fraction
