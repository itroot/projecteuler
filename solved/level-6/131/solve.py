#!/usr/bin/env python
# -*- coding: utf-8 -*-

cubic_roots = set(map(lambda e: e**3, range(1000)))

result = 0

for line in open("../lib/data/primes-100000000.list"):
    p = int(line)
    if p > 1000000:
        break
    for root in cubic_roots:
        n = root + p
        if n in cubic_roots:
            result += 1
print result            
