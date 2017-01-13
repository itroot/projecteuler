#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

n2f = {}
d = defaultdict(list)

for line_n in open("../lib/data/minfactor-100000000.list"):
    n, p = map(int, line_n.rstrip("\n").split(" "))
    if n == 0:
        continue
    n2f[n] = p
    factors = []
    nc = n
    while nc != 1:
        divisor = n2f[nc]
        factors.append(divisor)
        nc /= divisor
    factor_set = set(factors)
    if len(factor_set) != 2:
        continue
    #print n, factors
    f1, f2 = list(sorted(factor_set))
    d[(f1, f2)].append(n)
    #if n == 100:
    #    break
    if n == 10000000:
        break

result = 0
for k, v in d.iteritems():
    #print k, v
    result += v[-1]
print result
