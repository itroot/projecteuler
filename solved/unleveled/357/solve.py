#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")

from Factorize import Factorization as F11n
from Factorize import AllDivisors as AD

upper_limit = 10 ** 8
#upper_limit = 10 ** 3

f11n = F11n()

primes = map(int, open("../lib/data/primes-100000000.list").read().split())
primes_set = frozenset(primes)

result = 0

"""
o = open("../lib/data/minfactor-100000000.list", "w")
for i in xrange(upper_limit):
    if i in primes_set:
        o.write("%d %d\n" % (i, i))
    else:
        for p in primes:
            if i % p == 0:
                o.write("%d %d\n" % (i, p))
                break
o.close()
#sys.exit(0)
"""

for p in primes[1:]:
    i = p - 1
    if not (i/2 + 2) in primes_set:
        continue
    factors = f11n.factorize(i)
    ad = AD(factors)
    divisors = ad.divisors()
    blahs = list(set(map(lambda (d1, d2): d1 + d2 , zip(divisors, reversed(divisors)))))
    #print i, blahs
    if all(map(lambda e: e in primes_set, blahs)):
        print i, factors, divisors, blahs
        result += i

print result + 1
