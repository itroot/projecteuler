#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import gcd

upperLimit = 12000
result = 0
for d in range(3, upperLimit+1):
    for n in range(d/3-1, d/2+1):
        if gcd(n, d) == 1 and 2*n<d and 3*n>d:
            result+=1
print result
