#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import *;
import math

# for x: 3/7 == y/x
# y=x*3/7

upperLimit=10**6
rightLimit=Fraction(3, 7)

lastFraction=Fraction(0, 1)
for i in range(1, upperLimit+1):
    if i==rightLimit.denominator:
        continue
    #if 0==i%10000:
    #    print i
    numeratorRound=i*rightLimit.numerator/rightLimit.denominator
    if 1==gcd(numeratorRound, i):
        fraction=Fraction(numeratorRound, i)
        if fraction>lastFraction:
            lastFraction=fraction
print lastFraction.numerator
