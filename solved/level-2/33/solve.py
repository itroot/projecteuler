#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction
fractions=[]
for numerator in range(10, 100):
    for denominator in range(numerator, 100):
        if (0==numerator%10 and 0==denominator%10):
            continue
        if (0==numerator%11 and 0==denominator%11):
            continue
        if (numerator==denominator):
            continue
        fraction=Fraction(numerator, denominator)
        for i in (0, 1):
            for j in (0, 1):
                if (str(numerator)[1-i]!=str(denominator)[1-j]):
                    continue
                dummyNumerator=int(str(numerator)[i])
                dummyDenominator=int(str(denominator)[j])
                if (0==dummyDenominator):
                    continue
                dummyCancelledFraction=Fraction(dummyNumerator, dummyDenominator)
                if fraction==dummyCancelledFraction:
                    fractions.append(fraction)
                    #print "%s/%s" % (numerator, denominator)

fractionProduct=reduce(lambda a, b: a*b, fractions)
print fractionProduct.denominator

