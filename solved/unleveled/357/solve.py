#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")

from Factorize import Factorization as F11n
from Factorize import AllDivisors as AD

upper_limit = 10 ** 7
#upper_limit = 10 ** 3

f11n = F11n()

for i in xrange(2, upper_limit + 1):
    factors = f11n.factorize(i)
    ad = AD(factors)
    divisors = ad.divisors()
    blahs = list(set(map(lambda (d1, d2): d1 + d2 , zip(divisors, reversed(divisors)))))
    #print i, blahs
    if all(map(lambda e: len(f11n.factorize(e)) == 1, blahs)):
        print i, factors, divisors, blahs
