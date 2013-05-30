#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=10**6+1

import sys
sys.path.append("../lib/")
import Factorize


f=Factorize.Factorization()
for i in range(2, upperLimit):
    factorization=f.factorize(i)
    properDivisors=Factorize.AllDivisors(factorization).divisors()[:-1]
    print i, properDivisors
    # taking too long
    if i==300000:
        break
