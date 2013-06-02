#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=1000#10**6+1

import sys
sys.path.append("../lib/")
import Factorize


f=Factorize.Factorization()
for i in range(2, upperLimit):
    factorization=f.factorize(i)
    properDivisors=Factorize.AllDivisors(factorization).divisors()[:-1]
    divisorsSum = sum(properDivisors)
    if divisorsSum>=i:
        print i, divisorsSum
    # taking too long
    if i==300000:
        break
