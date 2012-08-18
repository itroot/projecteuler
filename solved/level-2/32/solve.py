#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
from Permutation import *
import math

upperLimit=9
digits=range(1, upperLimit+1)

productSet=set()

for i in range(0, math.factorial(upperLimit)):
    permutation=nth_permutation(digits, i)
    for b in range(2, 9):
        for a in range(1, b):
            multiplierLeft=reduce(lambda a, b: 10*a+b, permutation[:a])
            multiplierRight=reduce(lambda a, b: 10*a+b, permutation[a:b])
            product=reduce(lambda a, b: 10*a+b, permutation[b:])
            if (multiplierLeft*multiplierRight==product):
                #print multiplierLeft, multiplierRight, product
                productSet.add(product)
print reduce(lambda a, b: a+b, productSet)
