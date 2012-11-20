#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction

def calculateFraction(prefix):
    if (1==len(prefix)):
        return Fraction(prefix[0], 1)
    denominator=calculateFraction(prefix[1:])
    fraction=prefix[0]+Fraction(denominator.denominator, denominator.numerator)
    return fraction

prefix=[1, 2, 2, 2]
print calculateFraction(prefix)