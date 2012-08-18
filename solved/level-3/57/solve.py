#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction;

upperLimit=1000

square2Fractions=[Fraction(3, 2)]

for i in range(1, upperLimit):
    newFraction=1+1/(square2Fractions[-1]+1)
    square2Fractions.append(newFraction)

#print square2Fractions

result=0
for fraction in square2Fractions:
    if (len(str(fraction.numerator))>len(str(fraction.denominator))):
        result+=1
print result

